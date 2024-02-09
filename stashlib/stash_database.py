import os
import re
from .common import get_checksum, get_checksum_bytes, get_timestamp, image_to_base64, parse_part, optional_nonalphanum_regex
from .logger import logger as log
from .stash_database_base import StashDatabaseBase
from .stash_tables import *
from .stash_models import *

class StashDatabase(StashDatabaseBase):

    def __init__(self, db_path, blobs_path, blobs_storage):
        super().__init__(db_path)
        self.blobs_path = blobs_path
        self.blobs_storage = blobs_storage
        row = self.schema_migrations.selectone()
        if not row:
            raise Exception(f'schema version not found')
        schema_migration = SchemaMigrationsRow().from_sqliterow(row)
        if schema_migration.version != StashDatabase.SCHEMA_VERSION:
            raise Exception(f'schema version mismatch. schema version is {schema_migration.version}, expected {StashDatabase.SCHEMA_VERSION}')
        elif schema_migration.dirty:
            raise Exception(f'schema migration not completed')

    def performers_from_scene_id(self, scene_id):
        rows = self.fetchall("""SELECT c.* FROM scenes a JOIN performers_scenes b ON a.id = b.scene_id JOIN performers c ON c.id = b.performer_id WHERE a.id = ?""", (scene_id, ))
        return [PerformersRow().from_sqliterow(row) for row in rows]

    def query_performer_url(self, url):
        result = self.fetchone(f"""SELECT * FROM performers WHERE url LIKE ?""", (url, ))
        if result:
            return PerformersRow().from_sqliterow(result)
        return None

    def query_performer_name(self, name):
        rows = self.fetchall(f"""SELECT * FROM performers WHERE name LIKE ?""", (name, ))
        return [PerformersRow().from_sqliterow(row) for row in rows]

    def query_performer_name_disambiguated(self, name, disambiguation):
        if disambiguation is None:
            disambiguation = ''
        result = self.fetchone(f"""SELECT * FROM performers WHERE name LIKE ? AND COALESCE(disambiguation, '') LIKE ?""", (name, disambiguation))
        if result:
            return PerformersRow().from_sqliterow(result)
        return None

    def query_performer_name_regex(self, name):
        name_regex = optional_nonalphanum_regex(name)
        rows = self.fetchall(f"""SELECT * FROM performers WHERE name REGEXP ?""", (name_regex, ))
        return [PerformersRow().from_sqliterow(row) for row in rows]

    def query_studio_name(self, name):
        result = self.fetchone(f"""SELECT * FROM studios WHERE name LIKE ?""", (name, ))
        if result:
            return StudiosRow().from_sqliterow(result)
        return None

    def query_studio_name_regex(self, name):
        rows = self.fetchall(f"""SELECT * FROM studios WHERE STUDIOMATCHER(name, ?)""", (name, ))
        return [StudiosRow().from_sqliterow(row) for row in rows]

    def query_performer_alias(self, name):
        rows = self.fetchall(f"""SELECT * FROM performers WHERE aliases LIKE ?""", ('%' + name + '%', ))
        performers = [PerformersRow().from_sqliterow(row) for row in rows]
        results = []
        name_key = re.sub(r'[^a-zA-Z0-9\s]+', '', name.lower()).strip()
        for performer in performers:
            aliases = [x.split('(')[0].lower().strip() for x in performer.aliases.split(',')]
            aliases = [re.sub(r'[^a-zA-Z0-9\s]+', '', x).strip() for x in aliases]
            for alias in aliases:
                if alias == name_key:
                    results.append(performer)
                    match_found = True
                    break
        return results

    def query_similar_studio_name(self, name):
        result = self.fetchone(f"""SELECT * FROM studios WHERE REPLACE(REPLACE(name, ' ', ''), '-', '') LIKE ?""", (name.replace(' ', '').replace('-', ''), ))
        if result:
            return StudiosRow().from_sqliterow(result)
        return None

    def insert_performer(self, performer: PerformersRow, commit=True):
        performer.created_at = get_timestamp()
        performer.updated_at = get_timestamp()
        c = self.performers.insert_model(performer, commit)
        if c.rowcount:
            return self.performers.selectone_name(performer.name)
        return None

    def create_performer_from_url(self, name, disambiguation, url, commit=True):
        performer = self.performers.selectone_url(url)
        if performer:
            return performer

        results = self.query_performer_name(name)
        if results:
            return None

        performer = PerformersRow()
        performer.name = name
        performer.disambiguation = disambiguation
        performer.gender = 'FEMALE'
        performer.url = url
        performer.favorite = 0
        performer.details = None
        performer.ignore_auto_tag = False

        return self.insert_performer(performer, commit)

    def get_blobpath(self, checksum: str):
        return os.path.join(self.blobs_path, checksum[0:2], checksum[2:4], checksum)

    def remove_blobpath(self, checksum: str):
        try:
            if self.blobs_storage == 'FILESYSTEM':
                blobpath = self.get_blobpath(checksum)
                if os.path.exists(blobpath):
                    os.remove(blobpath)
        except Exception as e:
            log.LogError(str(e))
            return False
        return True

    def save_blob(self, image_bytes: bytes, commit=True):
        checksum = get_checksum_bytes(image_bytes)
        if self.blobs.selectone_checksum(checksum):
            return None
        image_blob = BlobsRow()
        image_blob.checksum = checksum
        if self.blobs_storage == 'FILESYSTEM':
            blobpath = self.get_blobpath(checksum)
            dirpath = os.path.dirname(blobpath)
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)
            with open(blobpath, 'wb') as f:
                f.write(image_bytes)
        elif self.blobs_storage == 'DATABASE':
            image_blob.blob = image_bytes
        try:
            self.blobs.insert_model(image_blob, commit)
        except Exception as e:
            log.LogError(str(e))
            if self.blobs_storage == 'FILESYSTEM':
                os.remove(blobpath)
            return None
        return checksum

    def insert_performer_image(self, performer: PerformersRow, image_bytes: bytes, commit=True):
        self.performers.update_image_blob_by_id(performer.id, None, False)
        if performer.image_blob:
            self.blobs.delete_by_checksum(performer.image_blob, False)
            if not self.remove_blobpath(performer.image_blob):
                self.rollback()
                return None
        checksum = self.save_blob(image_bytes, False)
        if checksum is None:
            return None
        self.performers.update_image_blob_by_id(performer.id, checksum, False)
        if commit:
            self.commit()
        return checksum

    def insert_movie_front_image(self, movie: MoviesRow, image_bytes: bytes, commit=True):
        self.movies.update_front_image_blob_by_id(movie.id, None, False)
        if movie.front_image_blob:
            self.blobs.delete_by_checksum(movie.front_image_blob, False)
            if not self.remove_blobpath(movie.front_image_blob):
                self.rollback()
                return None
        checksum = self.save_blob(image_bytes, False)
        if checksum is None:
            return None
        self.movies.update_front_image_blob_by_id(movie.id, checksum, False)
        if commit:
            self.commit()
        return checksum

    def insert_movie_back_image(self, movie: MoviesRow, image_bytes: bytes, commit=True):
        self.movies.update_back_image_blob_by_id(movie.id, None, False)
        if movie.back_image_blob:
            self.blobs.delete_by_checksum(movie.back_image_blob, False)
            if not self.remove_blobpath(movie.back_image_blob):
                self.rollback()
                return None
        checksum = self.save_blob(image_bytes, False)
        if checksum is None:
            return None
        self.movies.update_back_image_blob_by_id(movie.id, checksum, False)
        if commit:
            self.commit()
        return checksum

    def add_performers_to_scene(self, scene: ScenesRow, performers: list[PerformersRow], commit=True):
        existing_performer_ids = [performer_scene.performer_id for performer_scene in self.performers_scenes.select_scene_id(scene.id)]
        for performer in performers:
            if performer.id in existing_performer_ids:
                continue
            performers_scenes = PerformersScenesRow()
            performers_scenes.performer_id = performer.id
            performers_scenes.scene_id = scene.id
            try:
                self.performers_scenes.insert_model(performers_scenes, commit=False)
            except Exception as e:
                log.LogError(str(e))
        if commit:
            self.commit()

    def add_tag_to_scene(self, scene: ScenesRow, tag: TagsRow, commit=True):
        scenes_tags = ScenesTagsRow()
        scenes_tags.scene_id = scene.id
        scenes_tags.tag_id = tag.id
        existing_scene_tag = self.scenes_tags.selectone({'scene_id': scene.id, 'tag_id': tag.id})
        if not existing_scene_tag:
            self.scenes_tags.insert_model(scenes_tags, commit)

    def add_tag_name_to_scene(self, scene: ScenesRow, tag_name, commit=True):
        tag = self.tags.selectone_name(tag_name)
        if not tag:
            return False
        scenes_tags = ScenesTagsRow()
        scenes_tags.scene_id = scene.id
        scenes_tags.tag_id = tag.id
        existing_scene_tag = self.scenes_tags.selectone({'scene_id': scene.id, 'tag_id': tag.id})
        if not existing_scene_tag:
            self.scenes_tags.insert_model(scenes_tags, commit)
        return True

    def add_scenes_to_movie(self, movie: MoviesRow, scenes: list[ScenesRow], scene_index=None, commit=True):
        movies_scenes_rows = self.movies_scenes.select_movie_id(movie.id)
        movies_scenes_dict = {}
        for row in movies_scenes_rows:
            movies_scenes_dict[row.scene_id] = row

        for i, scene in enumerate(scenes):
            scene = scenes[i]
            if scene.id in movies_scenes_dict:
                continue
            movies_scenes = MoviesScenesRow()
            movies_scenes.movie_id = movie.id
            movies_scenes.scene_id = scene.id
            if scene_index:
                movies_scenes.scene_index = scene_index[i]
            try:
                self.movies_scenes.insert_model(movies_scenes, commit=False)
            except Exception as e:
                log.LogError(str(e))
        if commit:
            self.commit()

    def get_scenes_from_filepath(self, filepath):
        dirpath, filename = os.path.split(filepath)
        rows = self.fetchall("""SELECT a.*
FROM scenes a
JOIN scenes_files b
ON a.id = b.scene_id
JOIN files c
ON c.id = b.file_id
JOIN folders d
ON c.parent_folder_id = d.id
WHERE d.path = ? AND c.basename = ?""", (dirpath, filename))
        return [ScenesRow().from_sqliterow(row) for row in rows]

    def create_movie(self, name, url, front_path, back_path):
        # get existing movie by name
        movie = self.movies.selectone_name(name)

        # insert new movie if does not exist
        if not movie:
            movie = MoviesRow()
            movie.name = name
            movie.url = url
            movie.created_at = get_timestamp()
            movie.updated_at = get_timestamp()
            self.movies.insert_model(movie)
            movie = self.movies.selectone_name(name)

        # insert front and back images
        if front_path:
            front_image = open(front_path, 'rb').read()
            if front_image:
                self.insert_movie_front_image(movie, front_image)
        if back_path:
            back_image = open(back_path, 'rb').read()
            if back_image:
                self.insert_movie_back_image(movie, back_image)

        return self.movies.selectone_name(name)

    def create_movie_from_folder(self, dirpath, url, front_path, back_path, front_only=False, name=None):
        if not name:
            name = os.path.basename(dirpath)

        # get front/back image paths
        if not front_path:
            front_path = os.path.join(dirpath, 'front.jpg')
        if not back_path and not front_only:
            back_path = os.path.join(dirpath, 'back.jpg')

        movie = self.create_movie(name, url, front_path, back_path)

        # add scene from files in folder to movie
        filepaths = [os.path.join(dirpath, file) for file in os.listdir(dirpath)]
        scenes = []
        for filepath in filepaths:
            scenes += self.get_scenes_from_filepath(filepath)
        scenes = [scene for scene in scenes if scene]
        self.add_scenes_to_movie(movie, scenes)

    def create_movie_from_file(self, filepath, url, front_path, back_path, name=None, scene_index=1):
        filename = os.path.basename(filepath)
        if not name:
            name = os.path.splitext(filename)[0]

        movie = self.create_movie(name, url, front_path, back_path)

        # add scene from file to movie
        scenes = self.get_scenes_from_filepath(filepath)
        for scene in scenes:
            self.add_scenes_to_movie(movie, [scene], scene_index=[scene_index])

    def add_performers_to_gallery(self, gallery: GalleriesRow, performers: list[PerformersRow], commit=True):
        existing_performer_ids = [performer_gallery.performer_id for performer_gallery in self.performers_galleries.select_gallery_id(gallery.id)]
        for performer in performers:
            if performer.id in existing_performer_ids:
                continue
            performers_galleries = PerformersGalleriesRow()
            performers_galleries.performer_id = performer.id
            performers_galleries.gallery_id = gallery.id
            try:
                self.performers_galleries.insert_model(performers_galleries, commit=False)
            except Exception as e:
                log.LogError(str(e))
        if commit:
            self.commit()
