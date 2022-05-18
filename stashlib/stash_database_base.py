from . import sqlite_wrapper as sq
from .database import Database
from .stash_tables import *

class StashDatabaseBase(Database):

	SCHEMA_VERSION = 30

	def __init__(self, db_path):
		super().__init__(db_path)
		self.schema_migrations = SchemaMigrations(self.conn)
		self.tags = Tags(self.conn)
		self.sqlite_sequence = SqliteSequence(self.conn)
		self.studios = Studios(self.conn)
		self.performers = Performers(self.conn)
		self.movies = Movies(self.conn)
		self.scraped_items = ScrapedItems(self.conn)
		self.performers_image = PerformersImage(self.conn)
		self.studios_image = StudiosImage(self.conn)
		self.movies_images = MoviesImages(self.conn)
		self.tags_image = TagsImage(self.conn)
		self.scenes = Scenes(self.conn)
		self.performers_scenes = PerformersScenes(self.conn)
		self.scene_markers = SceneMarkers(self.conn)
		self.scene_markers_tags = SceneMarkersTags(self.conn)
		self.scenes_tags = ScenesTags(self.conn)
		self.movies_scenes = MoviesScenes(self.conn)
		self.scenes_cover = ScenesCover(self.conn)
		self.images = Images(self.conn)
		self.performers_images = PerformersImages(self.conn)
		self.images_tags = ImagesTags(self.conn)
		self.scene_stash_ids = SceneStashIds(self.conn)
		self.performer_stash_ids = PerformerStashIds(self.conn)
		self.studio_stash_ids = StudioStashIds(self.conn)
		self.galleries = Galleries(self.conn)
		self.scenes_galleries = ScenesGalleries(self.conn)
		self.galleries_images = GalleriesImages(self.conn)
		self.performers_galleries = PerformersGalleries(self.conn)
		self.galleries_tags = GalleriesTags(self.conn)
		self.performers_tags = PerformersTags(self.conn)
		self.tag_aliases = TagAliases(self.conn)
		self.saved_filters = SavedFilters(self.conn)
		self.tags_relations = TagsRelations(self.conn)
		self.studio_aliases = StudioAliases(self.conn)
