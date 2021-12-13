import os
import re
from .common import get_checksum, get_timestamp, image_to_base64, parse_part, optional_nonalphanum_regex
from .logger import logger as log
from .stash_database_base import StashDatabaseBase
from .stash_tables import *
from .stash_models import *

class StashDatabase(StashDatabaseBase):

    def __init__(self, db_path):
        super().__init__(db_path)
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
        result = self.fetchone(f"""SELECT * FROM performers WHERE name LIKE ?""", (name, ))
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

    def query_studio_name(self, name):
        result = self.fetchone(f"""SELECT * FROM studios WHERE REPLACE(REPLACE(name, ' ', ''), '-', '') LIKE ?""", (name.replace(' ', '').replace('-', ''), ))
        if result:
            return StudiosRow().from_sqliterow(result)
        return None

    def insert_performer(self, performer: PerformersRow, commit=True):
        performer.checksum = get_checksum(performer.name)
        performer.created_at = get_timestamp()
        performer.updated_at = get_timestamp()
        c = self.performers.insert_model(performer, commit)
        if c.rowcount:
            return self.performers.selectone_name(performer.name)
        return None

    def create_performer_from_url(self, name, url):
        performer = self.performers.selectone_url(url)
        if performer:
            return performer

        results = self.query_performer_name(name)
        if results:
            return None

        performer = PerformersRow()
        performer.name = name
        performer.gender = 'FEMALE'
        performer.url = url
        performer.favorite = 0
        performer.details = None

        performer = self.insert_performer(performer)
        if performer:
            return performer
        return None


    def insert_performer_image(self, performer: PerformersRow, image_bytes: bytes, commit=True):
        performer_image = self.performers_image.selectone_performer_id(performer.id)
        if not performer_image:
            performer_image = PerformersImageRow()
            performer_image.performer_id = performer.id
            performer_image.image = image_bytes
            c = self.performers_image.insert_model(performer_image, commit)
            if c.rowcount:
                return self.performers_image.selectone_performer_id(performer.id)
            return None
        else:
            return performer_image

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
                pass
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

    def add_scenes_to_movie(self, movie: MoviesRow, scenes: list[ScenesRow], scene_index=[], commit=True):
        for i in range(0, len(scenes)):
            scene = scenes[i]
            movies_scenes = MoviesScenesRow()
            movies_scenes.movie_id = movie.id
            movies_scenes.scene_id = scene.id
            if scene_index:
                movies_scenes.scene_index = scene_index[i]
            try:
                self.movies_scenes.insert_model(movies_scenes, commit=False)
            except Exception as e:
                log.LogError(str(e))
                pass
        if commit:
            self.commit()

    def create_movie(self, name, url, front_path, back_path):
        # get existing movie by name
        movie = self.movies.selectone_name(name)

        # insert new movie if does not exist
        if not movie:
            movie = MoviesRow()
            movie.name = name
            movie.checksum = get_checksum(name)
            movie.url = url
            movie.created_at = get_timestamp()
            movie.updated_at = get_timestamp()
            self.movies.insert_model(movie)
            movie = self.movies.selectone_name(name)

        # get front/back image contents
        front_image = None
        if front_path:
            front_image = open(front_path, 'rb').read()
        back_image = None
        if back_path:
            back_image = open(back_path, 'rb').read()

        # insert or update front/back images
        movies_images = self.movies_images.selectone_movie_id(movie.id)
        if not movies_images:
            movies_images = MoviesImagesRow()
            movies_images.movie_id = movie.id
            movies_images.front_image = front_image
            movies_images.back_image = back_image
            self.movies_images.insert_model(movies_images)
        else:
            self.movies_images.update_front_image_by_movie_id(movie.id, front_image, commit=False)
            self.movies_images.update_back_image_by_movie_id(movie.id, back_image, commit=False)
            self.commit()

        return movie

    def create_movie_from_folder(self, dirpath, url, front_path, back_path, front_only=False):
        name = os.path.basename(dirpath)
        name = re.sub(' \[.*?\]', '', name)
        name = re.sub(' \(\d{4}\)', '', name)
        name = re.sub(' DISC\d', '', name)

        # get front/back image paths
        if not front_path:
            front_path = os.path.join(dirpath, 'front.jpg')
        if not back_path and not front_only:
            back_path = os.path.join(dirpath, 'back.jpg')

        movie = self.create_movie(name, url, front_path, back_path)

        # add scene from files in folder to movie
        filepaths = [os.path.join(dirpath, file) for file in os.listdir(dirpath)]
        scenes = [self.scenes.selectone_path(filepath) for filepath in filepaths]
        scenes = [scene for scene in scenes if scene]
        self.add_scenes_to_movie(movie, scenes)

    def create_movie_from_file(self, filepath, url, front_path, back_path):
        filename = os.path.basename(filepath)
        part, name = parse_part(os.path.splitext(filename)[0])

        movie = self.create_movie(name, url, front_path, back_path)

        # add scene from file to movie
        scene = self.scenes.selectone_path(filepath)
        if scene:
            self.add_scenes_to_movie(movie, [scene], scene_index=[part])

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
                pass
        if commit:
            self.commit()
