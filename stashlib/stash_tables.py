import sqlite3
from .table import Table
from .stash_models import *

class SchemaMigrations(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'schema_migrations')

	def select_version(self, version, colvalues={}, selectcols=['*']):
		colvalues['version'] = version
		return [SchemaMigrationsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_dirty(self, dirty, colvalues={}, selectcols=['*']):
		colvalues['dirty'] = dirty
		return [SchemaMigrationsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_version(self, version, colvalues={}, selectcols=['*']):
		colvalues['version'] = version
		row = self.selectone(colvalues, selectcols)
		if row:
			return SchemaMigrationsRow().from_sqliterow(row)
		else:
			return None

	def selectone_dirty(self, dirty, colvalues={}, selectcols=['*']):
		colvalues['dirty'] = dirty
		row = self.selectone(colvalues, selectcols)
		if row:
			return SchemaMigrationsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, version, dirty, commit=True):
		return self.execute("INSERT INTO schema_migrations (version, dirty) VALUES (?, ?)", [version, dirty], commit)

	def insert_model(self, model: SchemaMigrationsRow, commit=True):
		return self.execute("INSERT INTO schema_migrations (version, dirty) VALUES (?, ?)", model.values_list(False), commit)

class Tags(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'tags')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [TagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
		return [TagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [TagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [TagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_ignore_auto_tag(self, ignore_auto_tag, colvalues={}, selectcols=['*']):
		colvalues['ignore_auto_tag'] = ignore_auto_tag
		return [TagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_description(self, description, colvalues={}, selectcols=['*']):
		colvalues['description'] = description
		return [TagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_image_blob(self, image_blob, colvalues={}, selectcols=['*']):
		colvalues['image_blob'] = image_blob
		return [TagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagsRow().from_sqliterow(row)
		else:
			return None

	def selectone_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagsRow().from_sqliterow(row)
		else:
			return None

	def selectone_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagsRow().from_sqliterow(row)
		else:
			return None

	def selectone_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagsRow().from_sqliterow(row)
		else:
			return None

	def selectone_ignore_auto_tag(self, ignore_auto_tag, colvalues={}, selectcols=['*']):
		colvalues['ignore_auto_tag'] = ignore_auto_tag
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagsRow().from_sqliterow(row)
		else:
			return None

	def selectone_description(self, description, colvalues={}, selectcols=['*']):
		colvalues['description'] = description
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagsRow().from_sqliterow(row)
		else:
			return None

	def selectone_image_blob(self, image_blob, colvalues={}, selectcols=['*']):
		colvalues['image_blob'] = image_blob
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, name, created_at, updated_at, ignore_auto_tag, description, image_blob, commit=True):
		return self.execute("INSERT INTO tags (name, created_at, updated_at, ignore_auto_tag, description, image_blob) VALUES (?, ?, ?, ?, ?, ?)", [name, created_at, updated_at, ignore_auto_tag, description, image_blob], commit)

	def insert_model(self, model: TagsRow, commit=True):
		return self.execute("INSERT INTO tags (name, created_at, updated_at, ignore_auto_tag, description, image_blob) VALUES (?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_id(self, id, commit=True):
		return self.execute("DELETE FROM tags WHERE id = ?", [id, ], commit)

	def delete_by_name(self, name, commit=True):
		return self.execute("DELETE FROM tags WHERE name = ?", [name, ], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE tags SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE tags SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE tags SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE tags SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_ignore_auto_tag_by_id(self, id, value, commit=True):
		return self.execute("UPDATE tags SET ignore_auto_tag = ? WHERE id = ?", [value, id], commit)

	def update_empty_ignore_auto_tag_by_id(self, id, value, commit=True):
		return self.execute("UPDATE tags SET ignore_auto_tag = ? WHERE id = ? AND (ignore_auto_tag IS NULL OR ignore_auto_tag = '' OR ignore_auto_tag = 0)", [value, id], commit)

	def update_description_by_id(self, id, value, commit=True):
		return self.execute("UPDATE tags SET description = ? WHERE id = ?", [value, id], commit)

	def update_empty_description_by_id(self, id, value, commit=True):
		return self.execute("UPDATE tags SET description = ? WHERE id = ? AND (description IS NULL OR description = '' OR description = 0)", [value, id], commit)

	def update_image_blob_by_id(self, id, value, commit=True):
		return self.execute("UPDATE tags SET image_blob = ? WHERE id = ?", [value, id], commit)

	def update_empty_image_blob_by_id(self, id, value, commit=True):
		return self.execute("UPDATE tags SET image_blob = ? WHERE id = ? AND (image_blob IS NULL OR image_blob = '' OR image_blob = 0)", [value, id], commit)

	def update_created_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE tags SET created_at = ? WHERE name = ?", [value, name], commit)

	def update_empty_created_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE tags SET created_at = ? WHERE name = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, name], commit)

	def update_updated_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE tags SET updated_at = ? WHERE name = ?", [value, name], commit)

	def update_empty_updated_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE tags SET updated_at = ? WHERE name = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, name], commit)

	def update_ignore_auto_tag_by_name(self, name, value, commit=True):
		return self.execute("UPDATE tags SET ignore_auto_tag = ? WHERE name = ?", [value, name], commit)

	def update_empty_ignore_auto_tag_by_name(self, name, value, commit=True):
		return self.execute("UPDATE tags SET ignore_auto_tag = ? WHERE name = ? AND (ignore_auto_tag IS NULL OR ignore_auto_tag = '' OR ignore_auto_tag = 0)", [value, name], commit)

	def update_description_by_name(self, name, value, commit=True):
		return self.execute("UPDATE tags SET description = ? WHERE name = ?", [value, name], commit)

	def update_empty_description_by_name(self, name, value, commit=True):
		return self.execute("UPDATE tags SET description = ? WHERE name = ? AND (description IS NULL OR description = '' OR description = 0)", [value, name], commit)

	def update_image_blob_by_name(self, name, value, commit=True):
		return self.execute("UPDATE tags SET image_blob = ? WHERE name = ?", [value, name], commit)

	def update_empty_image_blob_by_name(self, name, value, commit=True):
		return self.execute("UPDATE tags SET image_blob = ? WHERE name = ? AND (image_blob IS NULL OR image_blob = '' OR image_blob = 0)", [value, name], commit)

class SqliteSequence(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'sqlite_sequence')

	def select_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
		return [SqliteSequenceRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_seq(self, seq, colvalues={}, selectcols=['*']):
		colvalues['seq'] = seq
		return [SqliteSequenceRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
		row = self.selectone(colvalues, selectcols)
		if row:
			return SqliteSequenceRow().from_sqliterow(row)
		else:
			return None

	def selectone_seq(self, seq, colvalues={}, selectcols=['*']):
		colvalues['seq'] = seq
		row = self.selectone(colvalues, selectcols)
		if row:
			return SqliteSequenceRow().from_sqliterow(row)
		else:
			return None

	def insert(self, name, seq, commit=True):
		return self.execute("INSERT INTO sqlite_sequence (name, seq) VALUES (?, ?)", [name, seq], commit)

	def insert_model(self, model: SqliteSequenceRow, commit=True):
		return self.execute("INSERT INTO sqlite_sequence (name, seq) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_name(self, name, commit=True):
		return self.execute("DELETE FROM sqlite_sequence WHERE name = ?", [name, ], commit)

	def update_seq_by_name(self, name, value, commit=True):
		return self.execute("UPDATE sqlite_sequence SET seq = ? WHERE name = ?", [value, name], commit)

	def update_empty_seq_by_name(self, name, value, commit=True):
		return self.execute("UPDATE sqlite_sequence SET seq = ? WHERE name = ? AND (seq IS NULL OR seq = '' OR seq = 0)", [value, name], commit)

class PerformerStashIds(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'performer_stash_ids')

	def select_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		return [PerformerStashIdsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_endpoint(self, endpoint, colvalues={}, selectcols=['*']):
		colvalues['endpoint'] = endpoint
		return [PerformerStashIdsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_stash_id(self, stash_id, colvalues={}, selectcols=['*']):
		colvalues['stash_id'] = stash_id
		return [PerformerStashIdsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformerStashIdsRow().from_sqliterow(row)
		else:
			return None

	def selectone_endpoint(self, endpoint, colvalues={}, selectcols=['*']):
		colvalues['endpoint'] = endpoint
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformerStashIdsRow().from_sqliterow(row)
		else:
			return None

	def selectone_stash_id(self, stash_id, colvalues={}, selectcols=['*']):
		colvalues['stash_id'] = stash_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformerStashIdsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, performer_id, endpoint, stash_id, commit=True):
		return self.execute("INSERT INTO performer_stash_ids (performer_id, endpoint, stash_id) VALUES (?, ?, ?)", [performer_id, endpoint, stash_id], commit)

	def insert_model(self, model: PerformerStashIdsRow, commit=True):
		return self.execute("INSERT INTO performer_stash_ids (performer_id, endpoint, stash_id) VALUES (?, ?, ?)", model.values_list(False), commit)

	def delete_by_performer_id(self, performer_id, commit=True):
		return self.execute("DELETE FROM performer_stash_ids WHERE performer_id = ?", [performer_id, ], commit)

	def delete_by_stash_id(self, stash_id, commit=True):
		return self.execute("DELETE FROM performer_stash_ids WHERE stash_id = ?", [stash_id, ], commit)

	def update_endpoint_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performer_stash_ids SET endpoint = ? WHERE performer_id = ?", [value, performer_id], commit)

	def update_empty_endpoint_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performer_stash_ids SET endpoint = ? WHERE performer_id = ? AND (endpoint IS NULL OR endpoint = '' OR endpoint = 0)", [value, performer_id], commit)

	def update_stash_id_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performer_stash_ids SET stash_id = ? WHERE performer_id = ?", [value, performer_id], commit)

	def update_empty_stash_id_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performer_stash_ids SET stash_id = ? WHERE performer_id = ? AND (stash_id IS NULL OR stash_id = '' OR stash_id = 0)", [value, performer_id], commit)

	def update_performer_id_by_stash_id(self, stash_id, value, commit=True):
		return self.execute("UPDATE performer_stash_ids SET performer_id = ? WHERE stash_id = ?", [value, stash_id], commit)

	def update_empty_performer_id_by_stash_id(self, stash_id, value, commit=True):
		return self.execute("UPDATE performer_stash_ids SET performer_id = ? WHERE stash_id = ? AND (performer_id IS NULL OR performer_id = '' OR performer_id = 0)", [value, stash_id], commit)

	def update_endpoint_by_stash_id(self, stash_id, value, commit=True):
		return self.execute("UPDATE performer_stash_ids SET endpoint = ? WHERE stash_id = ?", [value, stash_id], commit)

	def update_empty_endpoint_by_stash_id(self, stash_id, value, commit=True):
		return self.execute("UPDATE performer_stash_ids SET endpoint = ? WHERE stash_id = ? AND (endpoint IS NULL OR endpoint = '' OR endpoint = 0)", [value, stash_id], commit)

class StudioStashIds(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'studio_stash_ids')

	def select_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		return [StudioStashIdsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_endpoint(self, endpoint, colvalues={}, selectcols=['*']):
		colvalues['endpoint'] = endpoint
		return [StudioStashIdsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_stash_id(self, stash_id, colvalues={}, selectcols=['*']):
		colvalues['stash_id'] = stash_id
		return [StudioStashIdsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudioStashIdsRow().from_sqliterow(row)
		else:
			return None

	def selectone_endpoint(self, endpoint, colvalues={}, selectcols=['*']):
		colvalues['endpoint'] = endpoint
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudioStashIdsRow().from_sqliterow(row)
		else:
			return None

	def selectone_stash_id(self, stash_id, colvalues={}, selectcols=['*']):
		colvalues['stash_id'] = stash_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudioStashIdsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, studio_id, endpoint, stash_id, commit=True):
		return self.execute("INSERT INTO studio_stash_ids (studio_id, endpoint, stash_id) VALUES (?, ?, ?)", [studio_id, endpoint, stash_id], commit)

	def insert_model(self, model: StudioStashIdsRow, commit=True):
		return self.execute("INSERT INTO studio_stash_ids (studio_id, endpoint, stash_id) VALUES (?, ?, ?)", model.values_list(False), commit)

	def delete_by_studio_id(self, studio_id, commit=True):
		return self.execute("DELETE FROM studio_stash_ids WHERE studio_id = ?", [studio_id, ], commit)

	def delete_by_stash_id(self, stash_id, commit=True):
		return self.execute("DELETE FROM studio_stash_ids WHERE stash_id = ?", [stash_id, ], commit)

	def update_endpoint_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE studio_stash_ids SET endpoint = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_endpoint_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE studio_stash_ids SET endpoint = ? WHERE studio_id = ? AND (endpoint IS NULL OR endpoint = '' OR endpoint = 0)", [value, studio_id], commit)

	def update_stash_id_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE studio_stash_ids SET stash_id = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_stash_id_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE studio_stash_ids SET stash_id = ? WHERE studio_id = ? AND (stash_id IS NULL OR stash_id = '' OR stash_id = 0)", [value, studio_id], commit)

	def update_studio_id_by_stash_id(self, stash_id, value, commit=True):
		return self.execute("UPDATE studio_stash_ids SET studio_id = ? WHERE stash_id = ?", [value, stash_id], commit)

	def update_empty_studio_id_by_stash_id(self, stash_id, value, commit=True):
		return self.execute("UPDATE studio_stash_ids SET studio_id = ? WHERE stash_id = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, stash_id], commit)

	def update_endpoint_by_stash_id(self, stash_id, value, commit=True):
		return self.execute("UPDATE studio_stash_ids SET endpoint = ? WHERE stash_id = ?", [value, stash_id], commit)

	def update_empty_endpoint_by_stash_id(self, stash_id, value, commit=True):
		return self.execute("UPDATE studio_stash_ids SET endpoint = ? WHERE stash_id = ? AND (endpoint IS NULL OR endpoint = '' OR endpoint = 0)", [value, stash_id], commit)

class TagsRelations(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'tags_relations')

	def select_parent_id(self, parent_id, colvalues={}, selectcols=['*']):
		colvalues['parent_id'] = parent_id
		return [TagsRelationsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_child_id(self, child_id, colvalues={}, selectcols=['*']):
		colvalues['child_id'] = child_id
		return [TagsRelationsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_parent_id(self, parent_id, colvalues={}, selectcols=['*']):
		colvalues['parent_id'] = parent_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagsRelationsRow().from_sqliterow(row)
		else:
			return None

	def selectone_child_id(self, child_id, colvalues={}, selectcols=['*']):
		colvalues['child_id'] = child_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagsRelationsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, parent_id, child_id, commit=True):
		return self.execute("INSERT INTO tags_relations (parent_id, child_id) VALUES (?, ?)", [parent_id, child_id], commit)

	def insert_model(self, model: TagsRelationsRow, commit=True):
		return self.execute("INSERT INTO tags_relations (parent_id, child_id) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_parent_id(self, parent_id, commit=True):
		return self.execute("DELETE FROM tags_relations WHERE parent_id = ?", [parent_id, ], commit)

	def delete_by_child_id(self, child_id, commit=True):
		return self.execute("DELETE FROM tags_relations WHERE child_id = ?", [child_id, ], commit)

	def update_child_id_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE tags_relations SET child_id = ? WHERE parent_id = ?", [value, parent_id], commit)

	def update_empty_child_id_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE tags_relations SET child_id = ? WHERE parent_id = ? AND (child_id IS NULL OR child_id = '' OR child_id = 0)", [value, parent_id], commit)

	def update_parent_id_by_child_id(self, child_id, value, commit=True):
		return self.execute("UPDATE tags_relations SET parent_id = ? WHERE child_id = ?", [value, child_id], commit)

	def update_empty_parent_id_by_child_id(self, child_id, value, commit=True):
		return self.execute("UPDATE tags_relations SET parent_id = ? WHERE child_id = ? AND (parent_id IS NULL OR parent_id = '' OR parent_id = 0)", [value, child_id], commit)

class Folders(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'folders')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [FoldersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_path(self, path, colvalues={}, selectcols=['*']):
		colvalues['path'] = path
		return [FoldersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_parent_folder_id(self, parent_folder_id, colvalues={}, selectcols=['*']):
		colvalues['parent_folder_id'] = parent_folder_id
		return [FoldersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_mod_time(self, mod_time, colvalues={}, selectcols=['*']):
		colvalues['mod_time'] = mod_time
		return [FoldersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [FoldersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [FoldersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_zip_file_id(self, zip_file_id, colvalues={}, selectcols=['*']):
		colvalues['zip_file_id'] = zip_file_id
		return [FoldersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return FoldersRow().from_sqliterow(row)
		else:
			return None

	def selectone_path(self, path, colvalues={}, selectcols=['*']):
		colvalues['path'] = path
		row = self.selectone(colvalues, selectcols)
		if row:
			return FoldersRow().from_sqliterow(row)
		else:
			return None

	def selectone_parent_folder_id(self, parent_folder_id, colvalues={}, selectcols=['*']):
		colvalues['parent_folder_id'] = parent_folder_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return FoldersRow().from_sqliterow(row)
		else:
			return None

	def selectone_mod_time(self, mod_time, colvalues={}, selectcols=['*']):
		colvalues['mod_time'] = mod_time
		row = self.selectone(colvalues, selectcols)
		if row:
			return FoldersRow().from_sqliterow(row)
		else:
			return None

	def selectone_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return FoldersRow().from_sqliterow(row)
		else:
			return None

	def selectone_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return FoldersRow().from_sqliterow(row)
		else:
			return None

	def selectone_zip_file_id(self, zip_file_id, colvalues={}, selectcols=['*']):
		colvalues['zip_file_id'] = zip_file_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return FoldersRow().from_sqliterow(row)
		else:
			return None

	def insert(self, path, parent_folder_id, mod_time, created_at, updated_at, zip_file_id, commit=True):
		return self.execute("INSERT INTO folders (path, parent_folder_id, mod_time, created_at, updated_at, zip_file_id) VALUES (?, ?, ?, ?, ?, ?)", [path, parent_folder_id, mod_time, created_at, updated_at, zip_file_id], commit)

	def insert_model(self, model: FoldersRow, commit=True):
		return self.execute("INSERT INTO folders (path, parent_folder_id, mod_time, created_at, updated_at, zip_file_id) VALUES (?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_id(self, id, commit=True):
		return self.execute("DELETE FROM folders WHERE id = ?", [id, ], commit)

	def delete_by_path(self, path, commit=True):
		return self.execute("DELETE FROM folders WHERE path = ?", [path, ], commit)

	def delete_by_parent_folder_id(self, parent_folder_id, commit=True):
		return self.execute("DELETE FROM folders WHERE parent_folder_id = ?", [parent_folder_id, ], commit)

	def delete_by_zip_file_id(self, zip_file_id, commit=True):
		return self.execute("DELETE FROM folders WHERE zip_file_id = ?", [zip_file_id, ], commit)

	def update_parent_folder_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE folders SET parent_folder_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_parent_folder_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE folders SET parent_folder_id = ? WHERE id = ? AND (parent_folder_id IS NULL OR parent_folder_id = '' OR parent_folder_id = 0)", [value, id], commit)

	def update_mod_time_by_id(self, id, value, commit=True):
		return self.execute("UPDATE folders SET mod_time = ? WHERE id = ?", [value, id], commit)

	def update_empty_mod_time_by_id(self, id, value, commit=True):
		return self.execute("UPDATE folders SET mod_time = ? WHERE id = ? AND (mod_time IS NULL OR mod_time = '' OR mod_time = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE folders SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE folders SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE folders SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE folders SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_zip_file_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE folders SET zip_file_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_zip_file_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE folders SET zip_file_id = ? WHERE id = ? AND (zip_file_id IS NULL OR zip_file_id = '' OR zip_file_id = 0)", [value, id], commit)

	def update_parent_folder_id_by_path(self, path, value, commit=True):
		return self.execute("UPDATE folders SET parent_folder_id = ? WHERE path = ?", [value, path], commit)

	def update_empty_parent_folder_id_by_path(self, path, value, commit=True):
		return self.execute("UPDATE folders SET parent_folder_id = ? WHERE path = ? AND (parent_folder_id IS NULL OR parent_folder_id = '' OR parent_folder_id = 0)", [value, path], commit)

	def update_mod_time_by_path(self, path, value, commit=True):
		return self.execute("UPDATE folders SET mod_time = ? WHERE path = ?", [value, path], commit)

	def update_empty_mod_time_by_path(self, path, value, commit=True):
		return self.execute("UPDATE folders SET mod_time = ? WHERE path = ? AND (mod_time IS NULL OR mod_time = '' OR mod_time = 0)", [value, path], commit)

	def update_created_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE folders SET created_at = ? WHERE path = ?", [value, path], commit)

	def update_empty_created_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE folders SET created_at = ? WHERE path = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, path], commit)

	def update_updated_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE folders SET updated_at = ? WHERE path = ?", [value, path], commit)

	def update_empty_updated_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE folders SET updated_at = ? WHERE path = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, path], commit)

	def update_zip_file_id_by_path(self, path, value, commit=True):
		return self.execute("UPDATE folders SET zip_file_id = ? WHERE path = ?", [value, path], commit)

	def update_empty_zip_file_id_by_path(self, path, value, commit=True):
		return self.execute("UPDATE folders SET zip_file_id = ? WHERE path = ? AND (zip_file_id IS NULL OR zip_file_id = '' OR zip_file_id = 0)", [value, path], commit)

	def update_mod_time_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE folders SET mod_time = ? WHERE parent_folder_id = ?", [value, parent_folder_id], commit)

	def update_empty_mod_time_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE folders SET mod_time = ? WHERE parent_folder_id = ? AND (mod_time IS NULL OR mod_time = '' OR mod_time = 0)", [value, parent_folder_id], commit)

	def update_created_at_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE folders SET created_at = ? WHERE parent_folder_id = ?", [value, parent_folder_id], commit)

	def update_empty_created_at_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE folders SET created_at = ? WHERE parent_folder_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, parent_folder_id], commit)

	def update_updated_at_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE folders SET updated_at = ? WHERE parent_folder_id = ?", [value, parent_folder_id], commit)

	def update_empty_updated_at_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE folders SET updated_at = ? WHERE parent_folder_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, parent_folder_id], commit)

	def update_zip_file_id_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE folders SET zip_file_id = ? WHERE parent_folder_id = ?", [value, parent_folder_id], commit)

	def update_empty_zip_file_id_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE folders SET zip_file_id = ? WHERE parent_folder_id = ? AND (zip_file_id IS NULL OR zip_file_id = '' OR zip_file_id = 0)", [value, parent_folder_id], commit)

	def update_parent_folder_id_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE folders SET parent_folder_id = ? WHERE zip_file_id = ?", [value, zip_file_id], commit)

	def update_empty_parent_folder_id_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE folders SET parent_folder_id = ? WHERE zip_file_id = ? AND (parent_folder_id IS NULL OR parent_folder_id = '' OR parent_folder_id = 0)", [value, zip_file_id], commit)

	def update_mod_time_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE folders SET mod_time = ? WHERE zip_file_id = ?", [value, zip_file_id], commit)

	def update_empty_mod_time_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE folders SET mod_time = ? WHERE zip_file_id = ? AND (mod_time IS NULL OR mod_time = '' OR mod_time = 0)", [value, zip_file_id], commit)

	def update_created_at_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE folders SET created_at = ? WHERE zip_file_id = ?", [value, zip_file_id], commit)

	def update_empty_created_at_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE folders SET created_at = ? WHERE zip_file_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, zip_file_id], commit)

	def update_updated_at_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE folders SET updated_at = ? WHERE zip_file_id = ?", [value, zip_file_id], commit)

	def update_empty_updated_at_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE folders SET updated_at = ? WHERE zip_file_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, zip_file_id], commit)

class Files(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'files')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [FilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_basename(self, basename, colvalues={}, selectcols=['*']):
		colvalues['basename'] = basename
		return [FilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_zip_file_id(self, zip_file_id, colvalues={}, selectcols=['*']):
		colvalues['zip_file_id'] = zip_file_id
		return [FilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_parent_folder_id(self, parent_folder_id, colvalues={}, selectcols=['*']):
		colvalues['parent_folder_id'] = parent_folder_id
		return [FilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_size(self, size, colvalues={}, selectcols=['*']):
		colvalues['size'] = size
		return [FilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_mod_time(self, mod_time, colvalues={}, selectcols=['*']):
		colvalues['mod_time'] = mod_time
		return [FilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [FilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [FilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return FilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_basename(self, basename, colvalues={}, selectcols=['*']):
		colvalues['basename'] = basename
		row = self.selectone(colvalues, selectcols)
		if row:
			return FilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_zip_file_id(self, zip_file_id, colvalues={}, selectcols=['*']):
		colvalues['zip_file_id'] = zip_file_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return FilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_parent_folder_id(self, parent_folder_id, colvalues={}, selectcols=['*']):
		colvalues['parent_folder_id'] = parent_folder_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return FilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_size(self, size, colvalues={}, selectcols=['*']):
		colvalues['size'] = size
		row = self.selectone(colvalues, selectcols)
		if row:
			return FilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_mod_time(self, mod_time, colvalues={}, selectcols=['*']):
		colvalues['mod_time'] = mod_time
		row = self.selectone(colvalues, selectcols)
		if row:
			return FilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return FilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return FilesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, basename, zip_file_id, parent_folder_id, size, mod_time, created_at, updated_at, commit=True):
		return self.execute("INSERT INTO files (basename, zip_file_id, parent_folder_id, size, mod_time, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)", [basename, zip_file_id, parent_folder_id, size, mod_time, created_at, updated_at], commit)

	def insert_model(self, model: FilesRow, commit=True):
		return self.execute("INSERT INTO files (basename, zip_file_id, parent_folder_id, size, mod_time, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_id(self, id, commit=True):
		return self.execute("DELETE FROM files WHERE id = ?", [id, ], commit)

	def delete_by_zip_file_id(self, zip_file_id, commit=True):
		return self.execute("DELETE FROM files WHERE zip_file_id = ?", [zip_file_id, ], commit)

	def delete_by_parent_folder_id(self, parent_folder_id, commit=True):
		return self.execute("DELETE FROM files WHERE parent_folder_id = ?", [parent_folder_id, ], commit)

	def update_basename_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET basename = ? WHERE id = ?", [value, id], commit)

	def update_empty_basename_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET basename = ? WHERE id = ? AND (basename IS NULL OR basename = '' OR basename = 0)", [value, id], commit)

	def update_zip_file_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET zip_file_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_zip_file_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET zip_file_id = ? WHERE id = ? AND (zip_file_id IS NULL OR zip_file_id = '' OR zip_file_id = 0)", [value, id], commit)

	def update_parent_folder_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET parent_folder_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_parent_folder_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET parent_folder_id = ? WHERE id = ? AND (parent_folder_id IS NULL OR parent_folder_id = '' OR parent_folder_id = 0)", [value, id], commit)

	def update_size_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET size = ? WHERE id = ?", [value, id], commit)

	def update_empty_size_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET size = ? WHERE id = ? AND (size IS NULL OR size = '' OR size = 0)", [value, id], commit)

	def update_mod_time_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET mod_time = ? WHERE id = ?", [value, id], commit)

	def update_empty_mod_time_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET mod_time = ? WHERE id = ? AND (mod_time IS NULL OR mod_time = '' OR mod_time = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE files SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_basename_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE files SET basename = ? WHERE zip_file_id = ?", [value, zip_file_id], commit)

	def update_empty_basename_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE files SET basename = ? WHERE zip_file_id = ? AND (basename IS NULL OR basename = '' OR basename = 0)", [value, zip_file_id], commit)

	def update_parent_folder_id_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE files SET parent_folder_id = ? WHERE zip_file_id = ?", [value, zip_file_id], commit)

	def update_empty_parent_folder_id_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE files SET parent_folder_id = ? WHERE zip_file_id = ? AND (parent_folder_id IS NULL OR parent_folder_id = '' OR parent_folder_id = 0)", [value, zip_file_id], commit)

	def update_size_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE files SET size = ? WHERE zip_file_id = ?", [value, zip_file_id], commit)

	def update_empty_size_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE files SET size = ? WHERE zip_file_id = ? AND (size IS NULL OR size = '' OR size = 0)", [value, zip_file_id], commit)

	def update_mod_time_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE files SET mod_time = ? WHERE zip_file_id = ?", [value, zip_file_id], commit)

	def update_empty_mod_time_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE files SET mod_time = ? WHERE zip_file_id = ? AND (mod_time IS NULL OR mod_time = '' OR mod_time = 0)", [value, zip_file_id], commit)

	def update_created_at_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE files SET created_at = ? WHERE zip_file_id = ?", [value, zip_file_id], commit)

	def update_empty_created_at_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE files SET created_at = ? WHERE zip_file_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, zip_file_id], commit)

	def update_updated_at_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE files SET updated_at = ? WHERE zip_file_id = ?", [value, zip_file_id], commit)

	def update_empty_updated_at_by_zip_file_id(self, zip_file_id, value, commit=True):
		return self.execute("UPDATE files SET updated_at = ? WHERE zip_file_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, zip_file_id], commit)

	def update_basename_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE files SET basename = ? WHERE parent_folder_id = ?", [value, parent_folder_id], commit)

	def update_empty_basename_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE files SET basename = ? WHERE parent_folder_id = ? AND (basename IS NULL OR basename = '' OR basename = 0)", [value, parent_folder_id], commit)

	def update_zip_file_id_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE files SET zip_file_id = ? WHERE parent_folder_id = ?", [value, parent_folder_id], commit)

	def update_empty_zip_file_id_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE files SET zip_file_id = ? WHERE parent_folder_id = ? AND (zip_file_id IS NULL OR zip_file_id = '' OR zip_file_id = 0)", [value, parent_folder_id], commit)

	def update_size_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE files SET size = ? WHERE parent_folder_id = ?", [value, parent_folder_id], commit)

	def update_empty_size_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE files SET size = ? WHERE parent_folder_id = ? AND (size IS NULL OR size = '' OR size = 0)", [value, parent_folder_id], commit)

	def update_mod_time_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE files SET mod_time = ? WHERE parent_folder_id = ?", [value, parent_folder_id], commit)

	def update_empty_mod_time_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE files SET mod_time = ? WHERE parent_folder_id = ? AND (mod_time IS NULL OR mod_time = '' OR mod_time = 0)", [value, parent_folder_id], commit)

	def update_created_at_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE files SET created_at = ? WHERE parent_folder_id = ?", [value, parent_folder_id], commit)

	def update_empty_created_at_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE files SET created_at = ? WHERE parent_folder_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, parent_folder_id], commit)

	def update_updated_at_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE files SET updated_at = ? WHERE parent_folder_id = ?", [value, parent_folder_id], commit)

	def update_empty_updated_at_by_parent_folder_id(self, parent_folder_id, value, commit=True):
		return self.execute("UPDATE files SET updated_at = ? WHERE parent_folder_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, parent_folder_id], commit)

class FilesFingerprints(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'files_fingerprints')

	def select_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		return [FilesFingerprintsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_type(self, type, colvalues={}, selectcols=['*']):
		colvalues['type'] = type
		return [FilesFingerprintsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_fingerprint(self, fingerprint, colvalues={}, selectcols=['*']):
		colvalues['fingerprint'] = fingerprint
		return [FilesFingerprintsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return FilesFingerprintsRow().from_sqliterow(row)
		else:
			return None

	def selectone_type(self, type, colvalues={}, selectcols=['*']):
		colvalues['type'] = type
		row = self.selectone(colvalues, selectcols)
		if row:
			return FilesFingerprintsRow().from_sqliterow(row)
		else:
			return None

	def selectone_fingerprint(self, fingerprint, colvalues={}, selectcols=['*']):
		colvalues['fingerprint'] = fingerprint
		row = self.selectone(colvalues, selectcols)
		if row:
			return FilesFingerprintsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, file_id, type, fingerprint, commit=True):
		return self.execute("INSERT INTO files_fingerprints (file_id, type, fingerprint) VALUES (?, ?, ?)", [file_id, type, fingerprint], commit)

	def insert_model(self, model: FilesFingerprintsRow, commit=True):
		return self.execute("INSERT INTO files_fingerprints (file_id, type, fingerprint) VALUES (?, ?, ?)", model.values_list(False), commit)

	def delete_by_file_id(self, file_id, commit=True):
		return self.execute("DELETE FROM files_fingerprints WHERE file_id = ?", [file_id, ], commit)

	def update_type_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE files_fingerprints SET type = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_type_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE files_fingerprints SET type = ? WHERE file_id = ? AND (type IS NULL OR type = '' OR type = 0)", [value, file_id], commit)

	def update_fingerprint_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE files_fingerprints SET fingerprint = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_fingerprint_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE files_fingerprints SET fingerprint = ? WHERE file_id = ? AND (fingerprint IS NULL OR fingerprint = '' OR fingerprint = 0)", [value, file_id], commit)

class VideoFiles(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'video_files')

	def select_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		return [VideoFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_duration(self, duration, colvalues={}, selectcols=['*']):
		colvalues['duration'] = duration
		return [VideoFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_video_codec(self, video_codec, colvalues={}, selectcols=['*']):
		colvalues['video_codec'] = video_codec
		return [VideoFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_format(self, format, colvalues={}, selectcols=['*']):
		colvalues['format'] = format
		return [VideoFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_audio_codec(self, audio_codec, colvalues={}, selectcols=['*']):
		colvalues['audio_codec'] = audio_codec
		return [VideoFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_width(self, width, colvalues={}, selectcols=['*']):
		colvalues['width'] = width
		return [VideoFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_height(self, height, colvalues={}, selectcols=['*']):
		colvalues['height'] = height
		return [VideoFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_frame_rate(self, frame_rate, colvalues={}, selectcols=['*']):
		colvalues['frame_rate'] = frame_rate
		return [VideoFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_bit_rate(self, bit_rate, colvalues={}, selectcols=['*']):
		colvalues['bit_rate'] = bit_rate
		return [VideoFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_interactive(self, interactive, colvalues={}, selectcols=['*']):
		colvalues['interactive'] = interactive
		return [VideoFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_interactive_speed(self, interactive_speed, colvalues={}, selectcols=['*']):
		colvalues['interactive_speed'] = interactive_speed
		return [VideoFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_duration(self, duration, colvalues={}, selectcols=['*']):
		colvalues['duration'] = duration
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_video_codec(self, video_codec, colvalues={}, selectcols=['*']):
		colvalues['video_codec'] = video_codec
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_format(self, format, colvalues={}, selectcols=['*']):
		colvalues['format'] = format
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_audio_codec(self, audio_codec, colvalues={}, selectcols=['*']):
		colvalues['audio_codec'] = audio_codec
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_width(self, width, colvalues={}, selectcols=['*']):
		colvalues['width'] = width
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_height(self, height, colvalues={}, selectcols=['*']):
		colvalues['height'] = height
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_frame_rate(self, frame_rate, colvalues={}, selectcols=['*']):
		colvalues['frame_rate'] = frame_rate
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_bit_rate(self, bit_rate, colvalues={}, selectcols=['*']):
		colvalues['bit_rate'] = bit_rate
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_interactive(self, interactive, colvalues={}, selectcols=['*']):
		colvalues['interactive'] = interactive
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_interactive_speed(self, interactive_speed, colvalues={}, selectcols=['*']):
		colvalues['interactive_speed'] = interactive_speed
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoFilesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, file_id, duration, video_codec, format, audio_codec, width, height, frame_rate, bit_rate, interactive, interactive_speed, commit=True):
		return self.execute("INSERT INTO video_files (file_id, duration, video_codec, format, audio_codec, width, height, frame_rate, bit_rate, interactive, interactive_speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [file_id, duration, video_codec, format, audio_codec, width, height, frame_rate, bit_rate, interactive, interactive_speed], commit)

	def insert_model(self, model: VideoFilesRow, commit=True):
		return self.execute("INSERT INTO video_files (file_id, duration, video_codec, format, audio_codec, width, height, frame_rate, bit_rate, interactive, interactive_speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_file_id(self, file_id, commit=True):
		return self.execute("DELETE FROM video_files WHERE file_id = ?", [file_id, ], commit)

	def update_duration_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET duration = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_duration_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET duration = ? WHERE file_id = ? AND (duration IS NULL OR duration = '' OR duration = 0)", [value, file_id], commit)

	def update_video_codec_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET video_codec = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_video_codec_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET video_codec = ? WHERE file_id = ? AND (video_codec IS NULL OR video_codec = '' OR video_codec = 0)", [value, file_id], commit)

	def update_format_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET format = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_format_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET format = ? WHERE file_id = ? AND (format IS NULL OR format = '' OR format = 0)", [value, file_id], commit)

	def update_audio_codec_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET audio_codec = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_audio_codec_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET audio_codec = ? WHERE file_id = ? AND (audio_codec IS NULL OR audio_codec = '' OR audio_codec = 0)", [value, file_id], commit)

	def update_width_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET width = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_width_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET width = ? WHERE file_id = ? AND (width IS NULL OR width = '' OR width = 0)", [value, file_id], commit)

	def update_height_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET height = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_height_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET height = ? WHERE file_id = ? AND (height IS NULL OR height = '' OR height = 0)", [value, file_id], commit)

	def update_frame_rate_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET frame_rate = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_frame_rate_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET frame_rate = ? WHERE file_id = ? AND (frame_rate IS NULL OR frame_rate = '' OR frame_rate = 0)", [value, file_id], commit)

	def update_bit_rate_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET bit_rate = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_bit_rate_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET bit_rate = ? WHERE file_id = ? AND (bit_rate IS NULL OR bit_rate = '' OR bit_rate = 0)", [value, file_id], commit)

	def update_interactive_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET interactive = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_interactive_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET interactive = ? WHERE file_id = ? AND (interactive IS NULL OR interactive = '' OR interactive = 0)", [value, file_id], commit)

	def update_interactive_speed_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET interactive_speed = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_interactive_speed_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_files SET interactive_speed = ? WHERE file_id = ? AND (interactive_speed IS NULL OR interactive_speed = '' OR interactive_speed = 0)", [value, file_id], commit)

class VideoCaptions(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'video_captions')

	def select_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		return [VideoCaptionsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_language_code(self, language_code, colvalues={}, selectcols=['*']):
		colvalues['language_code'] = language_code
		return [VideoCaptionsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_filename(self, filename, colvalues={}, selectcols=['*']):
		colvalues['filename'] = filename
		return [VideoCaptionsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_caption_type(self, caption_type, colvalues={}, selectcols=['*']):
		colvalues['caption_type'] = caption_type
		return [VideoCaptionsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoCaptionsRow().from_sqliterow(row)
		else:
			return None

	def selectone_language_code(self, language_code, colvalues={}, selectcols=['*']):
		colvalues['language_code'] = language_code
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoCaptionsRow().from_sqliterow(row)
		else:
			return None

	def selectone_filename(self, filename, colvalues={}, selectcols=['*']):
		colvalues['filename'] = filename
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoCaptionsRow().from_sqliterow(row)
		else:
			return None

	def selectone_caption_type(self, caption_type, colvalues={}, selectcols=['*']):
		colvalues['caption_type'] = caption_type
		row = self.selectone(colvalues, selectcols)
		if row:
			return VideoCaptionsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, file_id, language_code, filename, caption_type, commit=True):
		return self.execute("INSERT INTO video_captions (file_id, language_code, filename, caption_type) VALUES (?, ?, ?, ?)", [file_id, language_code, filename, caption_type], commit)

	def insert_model(self, model: VideoCaptionsRow, commit=True):
		return self.execute("INSERT INTO video_captions (file_id, language_code, filename, caption_type) VALUES (?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_file_id(self, file_id, commit=True):
		return self.execute("DELETE FROM video_captions WHERE file_id = ?", [file_id, ], commit)

	def update_language_code_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_captions SET language_code = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_language_code_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_captions SET language_code = ? WHERE file_id = ? AND (language_code IS NULL OR language_code = '' OR language_code = 0)", [value, file_id], commit)

	def update_filename_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_captions SET filename = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_filename_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_captions SET filename = ? WHERE file_id = ? AND (filename IS NULL OR filename = '' OR filename = 0)", [value, file_id], commit)

	def update_caption_type_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_captions SET caption_type = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_caption_type_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE video_captions SET caption_type = ? WHERE file_id = ? AND (caption_type IS NULL OR caption_type = '' OR caption_type = 0)", [value, file_id], commit)

class ImageFiles(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'image_files')

	def select_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		return [ImageFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_format(self, format, colvalues={}, selectcols=['*']):
		colvalues['format'] = format
		return [ImageFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_width(self, width, colvalues={}, selectcols=['*']):
		colvalues['width'] = width
		return [ImageFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_height(self, height, colvalues={}, selectcols=['*']):
		colvalues['height'] = height
		return [ImageFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImageFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_format(self, format, colvalues={}, selectcols=['*']):
		colvalues['format'] = format
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImageFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_width(self, width, colvalues={}, selectcols=['*']):
		colvalues['width'] = width
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImageFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_height(self, height, colvalues={}, selectcols=['*']):
		colvalues['height'] = height
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImageFilesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, file_id, format, width, height, commit=True):
		return self.execute("INSERT INTO image_files (file_id, format, width, height) VALUES (?, ?, ?, ?)", [file_id, format, width, height], commit)

	def insert_model(self, model: ImageFilesRow, commit=True):
		return self.execute("INSERT INTO image_files (file_id, format, width, height) VALUES (?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_file_id(self, file_id, commit=True):
		return self.execute("DELETE FROM image_files WHERE file_id = ?", [file_id, ], commit)

	def update_format_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE image_files SET format = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_format_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE image_files SET format = ? WHERE file_id = ? AND (format IS NULL OR format = '' OR format = 0)", [value, file_id], commit)

	def update_width_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE image_files SET width = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_width_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE image_files SET width = ? WHERE file_id = ? AND (width IS NULL OR width = '' OR width = 0)", [value, file_id], commit)

	def update_height_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE image_files SET height = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_height_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE image_files SET height = ? WHERE file_id = ? AND (height IS NULL OR height = '' OR height = 0)", [value, file_id], commit)

class ImagesFiles(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'images_files')

	def select_image_id(self, image_id, colvalues={}, selectcols=['*']):
		colvalues['image_id'] = image_id
		return [ImagesFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		return [ImagesFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_primary(self, primary, colvalues={}, selectcols=['*']):
		colvalues['primary'] = primary
		return [ImagesFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_image_id(self, image_id, colvalues={}, selectcols=['*']):
		colvalues['image_id'] = image_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_primary(self, primary, colvalues={}, selectcols=['*']):
		colvalues['primary'] = primary
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesFilesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, image_id, file_id, primary, commit=True):
		return self.execute("INSERT INTO images_files (image_id, file_id, primary) VALUES (?, ?, ?)", [image_id, file_id, primary], commit)

	def insert_model(self, model: ImagesFilesRow, commit=True):
		return self.execute("INSERT INTO images_files (image_id, file_id, primary) VALUES (?, ?, ?)", model.values_list(False), commit)

	def delete_by_image_id(self, image_id, commit=True):
		return self.execute("DELETE FROM images_files WHERE image_id = ?", [image_id, ], commit)

	def delete_by_file_id(self, file_id, commit=True):
		return self.execute("DELETE FROM images_files WHERE file_id = ?", [file_id, ], commit)

	def update_file_id_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE images_files SET file_id = ? WHERE image_id = ?", [value, image_id], commit)

	def update_empty_file_id_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE images_files SET file_id = ? WHERE image_id = ? AND (file_id IS NULL OR file_id = '' OR file_id = 0)", [value, image_id], commit)

	def update_primary_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE images_files SET primary = ? WHERE image_id = ?", [value, image_id], commit)

	def update_empty_primary_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE images_files SET primary = ? WHERE image_id = ? AND (primary IS NULL OR primary = '' OR primary = 0)", [value, image_id], commit)

	def update_image_id_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE images_files SET image_id = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_image_id_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE images_files SET image_id = ? WHERE file_id = ? AND (image_id IS NULL OR image_id = '' OR image_id = 0)", [value, file_id], commit)

	def update_primary_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE images_files SET primary = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_primary_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE images_files SET primary = ? WHERE file_id = ? AND (primary IS NULL OR primary = '' OR primary = 0)", [value, file_id], commit)

class GalleriesFiles(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'galleries_files')

	def select_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		return [GalleriesFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		return [GalleriesFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_primary(self, primary, colvalues={}, selectcols=['*']):
		colvalues['primary'] = primary
		return [GalleriesFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_primary(self, primary, colvalues={}, selectcols=['*']):
		colvalues['primary'] = primary
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesFilesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, gallery_id, file_id, primary, commit=True):
		return self.execute("INSERT INTO galleries_files (gallery_id, file_id, primary) VALUES (?, ?, ?)", [gallery_id, file_id, primary], commit)

	def insert_model(self, model: GalleriesFilesRow, commit=True):
		return self.execute("INSERT INTO galleries_files (gallery_id, file_id, primary) VALUES (?, ?, ?)", model.values_list(False), commit)

	def delete_by_gallery_id(self, gallery_id, commit=True):
		return self.execute("DELETE FROM galleries_files WHERE gallery_id = ?", [gallery_id, ], commit)

	def delete_by_file_id(self, file_id, commit=True):
		return self.execute("DELETE FROM galleries_files WHERE file_id = ?", [file_id, ], commit)

	def update_file_id_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_files SET file_id = ? WHERE gallery_id = ?", [value, gallery_id], commit)

	def update_empty_file_id_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_files SET file_id = ? WHERE gallery_id = ? AND (file_id IS NULL OR file_id = '' OR file_id = 0)", [value, gallery_id], commit)

	def update_primary_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_files SET primary = ? WHERE gallery_id = ?", [value, gallery_id], commit)

	def update_empty_primary_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_files SET primary = ? WHERE gallery_id = ? AND (primary IS NULL OR primary = '' OR primary = 0)", [value, gallery_id], commit)

	def update_gallery_id_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE galleries_files SET gallery_id = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_gallery_id_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE galleries_files SET gallery_id = ? WHERE file_id = ? AND (gallery_id IS NULL OR gallery_id = '' OR gallery_id = 0)", [value, file_id], commit)

	def update_primary_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE galleries_files SET primary = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_primary_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE galleries_files SET primary = ? WHERE file_id = ? AND (primary IS NULL OR primary = '' OR primary = 0)", [value, file_id], commit)

class ScenesFiles(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'scenes_files')

	def select_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		return [ScenesFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		return [ScenesFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_primary(self, primary, colvalues={}, selectcols=['*']):
		colvalues['primary'] = primary
		return [ScenesFilesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_file_id(self, file_id, colvalues={}, selectcols=['*']):
		colvalues['file_id'] = file_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesFilesRow().from_sqliterow(row)
		else:
			return None

	def selectone_primary(self, primary, colvalues={}, selectcols=['*']):
		colvalues['primary'] = primary
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesFilesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, scene_id, file_id, primary, commit=True):
		return self.execute("INSERT INTO scenes_files (scene_id, file_id, primary) VALUES (?, ?, ?)", [scene_id, file_id, primary], commit)

	def insert_model(self, model: ScenesFilesRow, commit=True):
		return self.execute("INSERT INTO scenes_files (scene_id, file_id, primary) VALUES (?, ?, ?)", model.values_list(False), commit)

	def delete_by_scene_id(self, scene_id, commit=True):
		return self.execute("DELETE FROM scenes_files WHERE scene_id = ?", [scene_id, ], commit)

	def delete_by_file_id(self, file_id, commit=True):
		return self.execute("DELETE FROM scenes_files WHERE file_id = ?", [file_id, ], commit)

	def update_file_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scenes_files SET file_id = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_file_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scenes_files SET file_id = ? WHERE scene_id = ? AND (file_id IS NULL OR file_id = '' OR file_id = 0)", [value, scene_id], commit)

	def update_primary_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scenes_files SET primary = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_primary_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scenes_files SET primary = ? WHERE scene_id = ? AND (primary IS NULL OR primary = '' OR primary = 0)", [value, scene_id], commit)

	def update_scene_id_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE scenes_files SET scene_id = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_scene_id_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE scenes_files SET scene_id = ? WHERE file_id = ? AND (scene_id IS NULL OR scene_id = '' OR scene_id = 0)", [value, file_id], commit)

	def update_primary_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE scenes_files SET primary = ? WHERE file_id = ?", [value, file_id], commit)

	def update_empty_primary_by_file_id(self, file_id, value, commit=True):
		return self.execute("UPDATE scenes_files SET primary = ? WHERE file_id = ? AND (primary IS NULL OR primary = '' OR primary = 0)", [value, file_id], commit)

class SqliteStat1(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'sqlite_stat1')

	def select_tbl(self, tbl, colvalues={}, selectcols=['*']):
		colvalues['tbl'] = tbl
		return [SqliteStat1Row().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_idx(self, idx, colvalues={}, selectcols=['*']):
		colvalues['idx'] = idx
		return [SqliteStat1Row().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_stat(self, stat, colvalues={}, selectcols=['*']):
		colvalues['stat'] = stat
		return [SqliteStat1Row().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_tbl(self, tbl, colvalues={}, selectcols=['*']):
		colvalues['tbl'] = tbl
		row = self.selectone(colvalues, selectcols)
		if row:
			return SqliteStat1Row().from_sqliterow(row)
		else:
			return None

	def selectone_idx(self, idx, colvalues={}, selectcols=['*']):
		colvalues['idx'] = idx
		row = self.selectone(colvalues, selectcols)
		if row:
			return SqliteStat1Row().from_sqliterow(row)
		else:
			return None

	def selectone_stat(self, stat, colvalues={}, selectcols=['*']):
		colvalues['stat'] = stat
		row = self.selectone(colvalues, selectcols)
		if row:
			return SqliteStat1Row().from_sqliterow(row)
		else:
			return None

	def insert(self, tbl, idx, stat, commit=True):
		return self.execute("INSERT INTO sqlite_stat1 (tbl, idx, stat) VALUES (?, ?, ?)", [tbl, idx, stat], commit)

	def insert_model(self, model: SqliteStat1Row, commit=True):
		return self.execute("INSERT INTO sqlite_stat1 (tbl, idx, stat) VALUES (?, ?, ?)", model.values_list(False), commit)

class SqliteStat4(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'sqlite_stat4')

	def select_tbl(self, tbl, colvalues={}, selectcols=['*']):
		colvalues['tbl'] = tbl
		return [SqliteStat4Row().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_idx(self, idx, colvalues={}, selectcols=['*']):
		colvalues['idx'] = idx
		return [SqliteStat4Row().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_neq(self, neq, colvalues={}, selectcols=['*']):
		colvalues['neq'] = neq
		return [SqliteStat4Row().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_nlt(self, nlt, colvalues={}, selectcols=['*']):
		colvalues['nlt'] = nlt
		return [SqliteStat4Row().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_ndlt(self, ndlt, colvalues={}, selectcols=['*']):
		colvalues['ndlt'] = ndlt
		return [SqliteStat4Row().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_sample(self, sample, colvalues={}, selectcols=['*']):
		colvalues['sample'] = sample
		return [SqliteStat4Row().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_tbl(self, tbl, colvalues={}, selectcols=['*']):
		colvalues['tbl'] = tbl
		row = self.selectone(colvalues, selectcols)
		if row:
			return SqliteStat4Row().from_sqliterow(row)
		else:
			return None

	def selectone_idx(self, idx, colvalues={}, selectcols=['*']):
		colvalues['idx'] = idx
		row = self.selectone(colvalues, selectcols)
		if row:
			return SqliteStat4Row().from_sqliterow(row)
		else:
			return None

	def selectone_neq(self, neq, colvalues={}, selectcols=['*']):
		colvalues['neq'] = neq
		row = self.selectone(colvalues, selectcols)
		if row:
			return SqliteStat4Row().from_sqliterow(row)
		else:
			return None

	def selectone_nlt(self, nlt, colvalues={}, selectcols=['*']):
		colvalues['nlt'] = nlt
		row = self.selectone(colvalues, selectcols)
		if row:
			return SqliteStat4Row().from_sqliterow(row)
		else:
			return None

	def selectone_ndlt(self, ndlt, colvalues={}, selectcols=['*']):
		colvalues['ndlt'] = ndlt
		row = self.selectone(colvalues, selectcols)
		if row:
			return SqliteStat4Row().from_sqliterow(row)
		else:
			return None

	def selectone_sample(self, sample, colvalues={}, selectcols=['*']):
		colvalues['sample'] = sample
		row = self.selectone(colvalues, selectcols)
		if row:
			return SqliteStat4Row().from_sqliterow(row)
		else:
			return None

	def insert(self, tbl, idx, neq, nlt, ndlt, sample, commit=True):
		return self.execute("INSERT INTO sqlite_stat4 (tbl, idx, neq, nlt, ndlt, sample) VALUES (?, ?, ?, ?, ?, ?)", [tbl, idx, neq, nlt, ndlt, sample], commit)

	def insert_model(self, model: SqliteStat4Row, commit=True):
		return self.execute("INSERT INTO sqlite_stat4 (tbl, idx, neq, nlt, ndlt, sample) VALUES (?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

class PerformersScenes(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'performers_scenes')

	def select_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		return [PerformersScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		return [PerformersScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersScenesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, performer_id, scene_id, commit=True):
		return self.execute("INSERT INTO performers_scenes (performer_id, scene_id) VALUES (?, ?)", [performer_id, scene_id], commit)

	def insert_model(self, model: PerformersScenesRow, commit=True):
		return self.execute("INSERT INTO performers_scenes (performer_id, scene_id) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_performer_id(self, performer_id, commit=True):
		return self.execute("DELETE FROM performers_scenes WHERE performer_id = ?", [performer_id, ], commit)

	def delete_by_scene_id(self, scene_id, commit=True):
		return self.execute("DELETE FROM performers_scenes WHERE scene_id = ?", [scene_id, ], commit)

	def update_scene_id_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performers_scenes SET scene_id = ? WHERE performer_id = ?", [value, performer_id], commit)

	def update_empty_scene_id_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performers_scenes SET scene_id = ? WHERE performer_id = ? AND (scene_id IS NULL OR scene_id = '' OR scene_id = 0)", [value, performer_id], commit)

	def update_performer_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE performers_scenes SET performer_id = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_performer_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE performers_scenes SET performer_id = ? WHERE scene_id = ? AND (performer_id IS NULL OR performer_id = '' OR performer_id = 0)", [value, scene_id], commit)

class SceneMarkersTags(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'scene_markers_tags')

	def select_scene_marker_id(self, scene_marker_id, colvalues={}, selectcols=['*']):
		colvalues['scene_marker_id'] = scene_marker_id
		return [SceneMarkersTagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		return [SceneMarkersTagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_scene_marker_id(self, scene_marker_id, colvalues={}, selectcols=['*']):
		colvalues['scene_marker_id'] = scene_marker_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneMarkersTagsRow().from_sqliterow(row)
		else:
			return None

	def selectone_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneMarkersTagsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, scene_marker_id, tag_id, commit=True):
		return self.execute("INSERT INTO scene_markers_tags (scene_marker_id, tag_id) VALUES (?, ?)", [scene_marker_id, tag_id], commit)

	def insert_model(self, model: SceneMarkersTagsRow, commit=True):
		return self.execute("INSERT INTO scene_markers_tags (scene_marker_id, tag_id) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_scene_marker_id(self, scene_marker_id, commit=True):
		return self.execute("DELETE FROM scene_markers_tags WHERE scene_marker_id = ?", [scene_marker_id, ], commit)

	def delete_by_tag_id(self, tag_id, commit=True):
		return self.execute("DELETE FROM scene_markers_tags WHERE tag_id = ?", [tag_id, ], commit)

	def update_tag_id_by_scene_marker_id(self, scene_marker_id, value, commit=True):
		return self.execute("UPDATE scene_markers_tags SET tag_id = ? WHERE scene_marker_id = ?", [value, scene_marker_id], commit)

	def update_empty_tag_id_by_scene_marker_id(self, scene_marker_id, value, commit=True):
		return self.execute("UPDATE scene_markers_tags SET tag_id = ? WHERE scene_marker_id = ? AND (tag_id IS NULL OR tag_id = '' OR tag_id = 0)", [value, scene_marker_id], commit)

	def update_scene_marker_id_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE scene_markers_tags SET scene_marker_id = ? WHERE tag_id = ?", [value, tag_id], commit)

	def update_empty_scene_marker_id_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE scene_markers_tags SET scene_marker_id = ? WHERE tag_id = ? AND (scene_marker_id IS NULL OR scene_marker_id = '' OR scene_marker_id = 0)", [value, tag_id], commit)

class ScenesTags(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'scenes_tags')

	def select_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		return [ScenesTagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		return [ScenesTagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesTagsRow().from_sqliterow(row)
		else:
			return None

	def selectone_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesTagsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, scene_id, tag_id, commit=True):
		return self.execute("INSERT INTO scenes_tags (scene_id, tag_id) VALUES (?, ?)", [scene_id, tag_id], commit)

	def insert_model(self, model: ScenesTagsRow, commit=True):
		return self.execute("INSERT INTO scenes_tags (scene_id, tag_id) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_scene_id(self, scene_id, commit=True):
		return self.execute("DELETE FROM scenes_tags WHERE scene_id = ?", [scene_id, ], commit)

	def delete_by_tag_id(self, tag_id, commit=True):
		return self.execute("DELETE FROM scenes_tags WHERE tag_id = ?", [tag_id, ], commit)

	def update_tag_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scenes_tags SET tag_id = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_tag_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scenes_tags SET tag_id = ? WHERE scene_id = ? AND (tag_id IS NULL OR tag_id = '' OR tag_id = 0)", [value, scene_id], commit)

	def update_scene_id_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE scenes_tags SET scene_id = ? WHERE tag_id = ?", [value, tag_id], commit)

	def update_empty_scene_id_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE scenes_tags SET scene_id = ? WHERE tag_id = ? AND (scene_id IS NULL OR scene_id = '' OR scene_id = 0)", [value, tag_id], commit)

class MoviesScenes(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'movies_scenes')

	def select_movie_id(self, movie_id, colvalues={}, selectcols=['*']):
		colvalues['movie_id'] = movie_id
		return [MoviesScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		return [MoviesScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_scene_index(self, scene_index, colvalues={}, selectcols=['*']):
		colvalues['scene_index'] = scene_index
		return [MoviesScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_movie_id(self, movie_id, colvalues={}, selectcols=['*']):
		colvalues['movie_id'] = movie_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_scene_index(self, scene_index, colvalues={}, selectcols=['*']):
		colvalues['scene_index'] = scene_index
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesScenesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, movie_id, scene_id, scene_index, commit=True):
		return self.execute("INSERT INTO movies_scenes (movie_id, scene_id, scene_index) VALUES (?, ?, ?)", [movie_id, scene_id, scene_index], commit)

	def insert_model(self, model: MoviesScenesRow, commit=True):
		return self.execute("INSERT INTO movies_scenes (movie_id, scene_id, scene_index) VALUES (?, ?, ?)", model.values_list(False), commit)

	def delete_by_movie_id(self, movie_id, commit=True):
		return self.execute("DELETE FROM movies_scenes WHERE movie_id = ?", [movie_id, ], commit)

	def delete_by_scene_id(self, scene_id, commit=True):
		return self.execute("DELETE FROM movies_scenes WHERE scene_id = ?", [scene_id, ], commit)

	def update_scene_id_by_movie_id(self, movie_id, value, commit=True):
		return self.execute("UPDATE movies_scenes SET scene_id = ? WHERE movie_id = ?", [value, movie_id], commit)

	def update_empty_scene_id_by_movie_id(self, movie_id, value, commit=True):
		return self.execute("UPDATE movies_scenes SET scene_id = ? WHERE movie_id = ? AND (scene_id IS NULL OR scene_id = '' OR scene_id = 0)", [value, movie_id], commit)

	def update_scene_index_by_movie_id(self, movie_id, value, commit=True):
		return self.execute("UPDATE movies_scenes SET scene_index = ? WHERE movie_id = ?", [value, movie_id], commit)

	def update_empty_scene_index_by_movie_id(self, movie_id, value, commit=True):
		return self.execute("UPDATE movies_scenes SET scene_index = ? WHERE movie_id = ? AND (scene_index IS NULL OR scene_index = '' OR scene_index = 0)", [value, movie_id], commit)

	def update_movie_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE movies_scenes SET movie_id = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_movie_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE movies_scenes SET movie_id = ? WHERE scene_id = ? AND (movie_id IS NULL OR movie_id = '' OR movie_id = 0)", [value, scene_id], commit)

	def update_scene_index_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE movies_scenes SET scene_index = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_scene_index_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE movies_scenes SET scene_index = ? WHERE scene_id = ? AND (scene_index IS NULL OR scene_index = '' OR scene_index = 0)", [value, scene_id], commit)

class PerformersImages(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'performers_images')

	def select_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		return [PerformersImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_image_id(self, image_id, colvalues={}, selectcols=['*']):
		colvalues['image_id'] = image_id
		return [PerformersImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_image_id(self, image_id, colvalues={}, selectcols=['*']):
		colvalues['image_id'] = image_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersImagesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, performer_id, image_id, commit=True):
		return self.execute("INSERT INTO performers_images (performer_id, image_id) VALUES (?, ?)", [performer_id, image_id], commit)

	def insert_model(self, model: PerformersImagesRow, commit=True):
		return self.execute("INSERT INTO performers_images (performer_id, image_id) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_performer_id(self, performer_id, commit=True):
		return self.execute("DELETE FROM performers_images WHERE performer_id = ?", [performer_id, ], commit)

	def delete_by_image_id(self, image_id, commit=True):
		return self.execute("DELETE FROM performers_images WHERE image_id = ?", [image_id, ], commit)

	def update_image_id_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performers_images SET image_id = ? WHERE performer_id = ?", [value, performer_id], commit)

	def update_empty_image_id_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performers_images SET image_id = ? WHERE performer_id = ? AND (image_id IS NULL OR image_id = '' OR image_id = 0)", [value, performer_id], commit)

	def update_performer_id_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE performers_images SET performer_id = ? WHERE image_id = ?", [value, image_id], commit)

	def update_empty_performer_id_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE performers_images SET performer_id = ? WHERE image_id = ? AND (performer_id IS NULL OR performer_id = '' OR performer_id = 0)", [value, image_id], commit)

class ImagesTags(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'images_tags')

	def select_image_id(self, image_id, colvalues={}, selectcols=['*']):
		colvalues['image_id'] = image_id
		return [ImagesTagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		return [ImagesTagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_image_id(self, image_id, colvalues={}, selectcols=['*']):
		colvalues['image_id'] = image_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesTagsRow().from_sqliterow(row)
		else:
			return None

	def selectone_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesTagsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, image_id, tag_id, commit=True):
		return self.execute("INSERT INTO images_tags (image_id, tag_id) VALUES (?, ?)", [image_id, tag_id], commit)

	def insert_model(self, model: ImagesTagsRow, commit=True):
		return self.execute("INSERT INTO images_tags (image_id, tag_id) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_image_id(self, image_id, commit=True):
		return self.execute("DELETE FROM images_tags WHERE image_id = ?", [image_id, ], commit)

	def delete_by_tag_id(self, tag_id, commit=True):
		return self.execute("DELETE FROM images_tags WHERE tag_id = ?", [tag_id, ], commit)

	def update_tag_id_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE images_tags SET tag_id = ? WHERE image_id = ?", [value, image_id], commit)

	def update_empty_tag_id_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE images_tags SET tag_id = ? WHERE image_id = ? AND (tag_id IS NULL OR tag_id = '' OR tag_id = 0)", [value, image_id], commit)

	def update_image_id_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE images_tags SET image_id = ? WHERE tag_id = ?", [value, tag_id], commit)

	def update_empty_image_id_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE images_tags SET image_id = ? WHERE tag_id = ? AND (image_id IS NULL OR image_id = '' OR image_id = 0)", [value, tag_id], commit)

class SceneStashIds(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'scene_stash_ids')

	def select_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		return [SceneStashIdsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_endpoint(self, endpoint, colvalues={}, selectcols=['*']):
		colvalues['endpoint'] = endpoint
		return [SceneStashIdsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_stash_id(self, stash_id, colvalues={}, selectcols=['*']):
		colvalues['stash_id'] = stash_id
		return [SceneStashIdsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneStashIdsRow().from_sqliterow(row)
		else:
			return None

	def selectone_endpoint(self, endpoint, colvalues={}, selectcols=['*']):
		colvalues['endpoint'] = endpoint
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneStashIdsRow().from_sqliterow(row)
		else:
			return None

	def selectone_stash_id(self, stash_id, colvalues={}, selectcols=['*']):
		colvalues['stash_id'] = stash_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneStashIdsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, scene_id, endpoint, stash_id, commit=True):
		return self.execute("INSERT INTO scene_stash_ids (scene_id, endpoint, stash_id) VALUES (?, ?, ?)", [scene_id, endpoint, stash_id], commit)

	def insert_model(self, model: SceneStashIdsRow, commit=True):
		return self.execute("INSERT INTO scene_stash_ids (scene_id, endpoint, stash_id) VALUES (?, ?, ?)", model.values_list(False), commit)

	def delete_by_scene_id(self, scene_id, commit=True):
		return self.execute("DELETE FROM scene_stash_ids WHERE scene_id = ?", [scene_id, ], commit)

	def delete_by_stash_id(self, stash_id, commit=True):
		return self.execute("DELETE FROM scene_stash_ids WHERE stash_id = ?", [stash_id, ], commit)

	def update_endpoint_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_stash_ids SET endpoint = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_endpoint_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_stash_ids SET endpoint = ? WHERE scene_id = ? AND (endpoint IS NULL OR endpoint = '' OR endpoint = 0)", [value, scene_id], commit)

	def update_stash_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_stash_ids SET stash_id = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_stash_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_stash_ids SET stash_id = ? WHERE scene_id = ? AND (stash_id IS NULL OR stash_id = '' OR stash_id = 0)", [value, scene_id], commit)

	def update_scene_id_by_stash_id(self, stash_id, value, commit=True):
		return self.execute("UPDATE scene_stash_ids SET scene_id = ? WHERE stash_id = ?", [value, stash_id], commit)

	def update_empty_scene_id_by_stash_id(self, stash_id, value, commit=True):
		return self.execute("UPDATE scene_stash_ids SET scene_id = ? WHERE stash_id = ? AND (scene_id IS NULL OR scene_id = '' OR scene_id = 0)", [value, stash_id], commit)

	def update_endpoint_by_stash_id(self, stash_id, value, commit=True):
		return self.execute("UPDATE scene_stash_ids SET endpoint = ? WHERE stash_id = ?", [value, stash_id], commit)

	def update_empty_endpoint_by_stash_id(self, stash_id, value, commit=True):
		return self.execute("UPDATE scene_stash_ids SET endpoint = ? WHERE stash_id = ? AND (endpoint IS NULL OR endpoint = '' OR endpoint = 0)", [value, stash_id], commit)

class ScenesGalleries(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'scenes_galleries')

	def select_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		return [ScenesGalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		return [ScenesGalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesGalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesGalleriesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, scene_id, gallery_id, commit=True):
		return self.execute("INSERT INTO scenes_galleries (scene_id, gallery_id) VALUES (?, ?)", [scene_id, gallery_id], commit)

	def insert_model(self, model: ScenesGalleriesRow, commit=True):
		return self.execute("INSERT INTO scenes_galleries (scene_id, gallery_id) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_scene_id(self, scene_id, commit=True):
		return self.execute("DELETE FROM scenes_galleries WHERE scene_id = ?", [scene_id, ], commit)

	def delete_by_gallery_id(self, gallery_id, commit=True):
		return self.execute("DELETE FROM scenes_galleries WHERE gallery_id = ?", [gallery_id, ], commit)

	def update_gallery_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scenes_galleries SET gallery_id = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_gallery_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scenes_galleries SET gallery_id = ? WHERE scene_id = ? AND (gallery_id IS NULL OR gallery_id = '' OR gallery_id = 0)", [value, scene_id], commit)

	def update_scene_id_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE scenes_galleries SET scene_id = ? WHERE gallery_id = ?", [value, gallery_id], commit)

	def update_empty_scene_id_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE scenes_galleries SET scene_id = ? WHERE gallery_id = ? AND (scene_id IS NULL OR scene_id = '' OR scene_id = 0)", [value, gallery_id], commit)

class GalleriesImages(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'galleries_images')

	def select_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		return [GalleriesImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_image_id(self, image_id, colvalues={}, selectcols=['*']):
		colvalues['image_id'] = image_id
		return [GalleriesImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_image_id(self, image_id, colvalues={}, selectcols=['*']):
		colvalues['image_id'] = image_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesImagesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, gallery_id, image_id, commit=True):
		return self.execute("INSERT INTO galleries_images (gallery_id, image_id) VALUES (?, ?)", [gallery_id, image_id], commit)

	def insert_model(self, model: GalleriesImagesRow, commit=True):
		return self.execute("INSERT INTO galleries_images (gallery_id, image_id) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_gallery_id(self, gallery_id, commit=True):
		return self.execute("DELETE FROM galleries_images WHERE gallery_id = ?", [gallery_id, ], commit)

	def delete_by_image_id(self, image_id, commit=True):
		return self.execute("DELETE FROM galleries_images WHERE image_id = ?", [image_id, ], commit)

	def update_image_id_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_images SET image_id = ? WHERE gallery_id = ?", [value, gallery_id], commit)

	def update_empty_image_id_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_images SET image_id = ? WHERE gallery_id = ? AND (image_id IS NULL OR image_id = '' OR image_id = 0)", [value, gallery_id], commit)

	def update_gallery_id_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE galleries_images SET gallery_id = ? WHERE image_id = ?", [value, image_id], commit)

	def update_empty_gallery_id_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE galleries_images SET gallery_id = ? WHERE image_id = ? AND (gallery_id IS NULL OR gallery_id = '' OR gallery_id = 0)", [value, image_id], commit)

class PerformersGalleries(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'performers_galleries')

	def select_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		return [PerformersGalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		return [PerformersGalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersGalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersGalleriesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, performer_id, gallery_id, commit=True):
		return self.execute("INSERT INTO performers_galleries (performer_id, gallery_id) VALUES (?, ?)", [performer_id, gallery_id], commit)

	def insert_model(self, model: PerformersGalleriesRow, commit=True):
		return self.execute("INSERT INTO performers_galleries (performer_id, gallery_id) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_performer_id(self, performer_id, commit=True):
		return self.execute("DELETE FROM performers_galleries WHERE performer_id = ?", [performer_id, ], commit)

	def delete_by_gallery_id(self, gallery_id, commit=True):
		return self.execute("DELETE FROM performers_galleries WHERE gallery_id = ?", [gallery_id, ], commit)

	def update_gallery_id_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performers_galleries SET gallery_id = ? WHERE performer_id = ?", [value, performer_id], commit)

	def update_empty_gallery_id_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performers_galleries SET gallery_id = ? WHERE performer_id = ? AND (gallery_id IS NULL OR gallery_id = '' OR gallery_id = 0)", [value, performer_id], commit)

	def update_performer_id_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE performers_galleries SET performer_id = ? WHERE gallery_id = ?", [value, gallery_id], commit)

	def update_empty_performer_id_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE performers_galleries SET performer_id = ? WHERE gallery_id = ? AND (performer_id IS NULL OR performer_id = '' OR performer_id = 0)", [value, gallery_id], commit)

class GalleriesTags(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'galleries_tags')

	def select_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		return [GalleriesTagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		return [GalleriesTagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesTagsRow().from_sqliterow(row)
		else:
			return None

	def selectone_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesTagsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, gallery_id, tag_id, commit=True):
		return self.execute("INSERT INTO galleries_tags (gallery_id, tag_id) VALUES (?, ?)", [gallery_id, tag_id], commit)

	def insert_model(self, model: GalleriesTagsRow, commit=True):
		return self.execute("INSERT INTO galleries_tags (gallery_id, tag_id) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_gallery_id(self, gallery_id, commit=True):
		return self.execute("DELETE FROM galleries_tags WHERE gallery_id = ?", [gallery_id, ], commit)

	def delete_by_tag_id(self, tag_id, commit=True):
		return self.execute("DELETE FROM galleries_tags WHERE tag_id = ?", [tag_id, ], commit)

	def update_tag_id_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_tags SET tag_id = ? WHERE gallery_id = ?", [value, gallery_id], commit)

	def update_empty_tag_id_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_tags SET tag_id = ? WHERE gallery_id = ? AND (tag_id IS NULL OR tag_id = '' OR tag_id = 0)", [value, gallery_id], commit)

	def update_gallery_id_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE galleries_tags SET gallery_id = ? WHERE tag_id = ?", [value, tag_id], commit)

	def update_empty_gallery_id_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE galleries_tags SET gallery_id = ? WHERE tag_id = ? AND (gallery_id IS NULL OR gallery_id = '' OR gallery_id = 0)", [value, tag_id], commit)

class PerformersTags(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'performers_tags')

	def select_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		return [PerformersTagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		return [PerformersTagsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersTagsRow().from_sqliterow(row)
		else:
			return None

	def selectone_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersTagsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, performer_id, tag_id, commit=True):
		return self.execute("INSERT INTO performers_tags (performer_id, tag_id) VALUES (?, ?)", [performer_id, tag_id], commit)

	def insert_model(self, model: PerformersTagsRow, commit=True):
		return self.execute("INSERT INTO performers_tags (performer_id, tag_id) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_performer_id(self, performer_id, commit=True):
		return self.execute("DELETE FROM performers_tags WHERE performer_id = ?", [performer_id, ], commit)

	def delete_by_tag_id(self, tag_id, commit=True):
		return self.execute("DELETE FROM performers_tags WHERE tag_id = ?", [tag_id, ], commit)

	def update_tag_id_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performers_tags SET tag_id = ? WHERE performer_id = ?", [value, performer_id], commit)

	def update_empty_tag_id_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performers_tags SET tag_id = ? WHERE performer_id = ? AND (tag_id IS NULL OR tag_id = '' OR tag_id = 0)", [value, performer_id], commit)

	def update_performer_id_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE performers_tags SET performer_id = ? WHERE tag_id = ?", [value, tag_id], commit)

	def update_empty_performer_id_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE performers_tags SET performer_id = ? WHERE tag_id = ? AND (performer_id IS NULL OR performer_id = '' OR performer_id = 0)", [value, tag_id], commit)

class TagAliases(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'tag_aliases')

	def select_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		return [TagAliasesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_alias(self, alias, colvalues={}, selectcols=['*']):
		colvalues['alias'] = alias
		return [TagAliasesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagAliasesRow().from_sqliterow(row)
		else:
			return None

	def selectone_alias(self, alias, colvalues={}, selectcols=['*']):
		colvalues['alias'] = alias
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagAliasesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, tag_id, alias, commit=True):
		return self.execute("INSERT INTO tag_aliases (tag_id, alias) VALUES (?, ?)", [tag_id, alias], commit)

	def insert_model(self, model: TagAliasesRow, commit=True):
		return self.execute("INSERT INTO tag_aliases (tag_id, alias) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_tag_id(self, tag_id, commit=True):
		return self.execute("DELETE FROM tag_aliases WHERE tag_id = ?", [tag_id, ], commit)

	def update_alias_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE tag_aliases SET alias = ? WHERE tag_id = ?", [value, tag_id], commit)

	def update_empty_alias_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE tag_aliases SET alias = ? WHERE tag_id = ? AND (alias IS NULL OR alias = '' OR alias = 0)", [value, tag_id], commit)

class StudioAliases(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'studio_aliases')

	def select_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		return [StudioAliasesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_alias(self, alias, colvalues={}, selectcols=['*']):
		colvalues['alias'] = alias
		return [StudioAliasesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudioAliasesRow().from_sqliterow(row)
		else:
			return None

	def selectone_alias(self, alias, colvalues={}, selectcols=['*']):
		colvalues['alias'] = alias
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudioAliasesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, studio_id, alias, commit=True):
		return self.execute("INSERT INTO studio_aliases (studio_id, alias) VALUES (?, ?)", [studio_id, alias], commit)

	def insert_model(self, model: StudioAliasesRow, commit=True):
		return self.execute("INSERT INTO studio_aliases (studio_id, alias) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_studio_id(self, studio_id, commit=True):
		return self.execute("DELETE FROM studio_aliases WHERE studio_id = ?", [studio_id, ], commit)

	def update_alias_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE studio_aliases SET alias = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_alias_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE studio_aliases SET alias = ? WHERE studio_id = ? AND (alias IS NULL OR alias = '' OR alias = 0)", [value, studio_id], commit)

class PerformerAliases(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'performer_aliases')

	def select_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		return [PerformerAliasesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_alias(self, alias, colvalues={}, selectcols=['*']):
		colvalues['alias'] = alias
		return [PerformerAliasesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformerAliasesRow().from_sqliterow(row)
		else:
			return None

	def selectone_alias(self, alias, colvalues={}, selectcols=['*']):
		colvalues['alias'] = alias
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformerAliasesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, performer_id, alias, commit=True):
		return self.execute("INSERT INTO performer_aliases (performer_id, alias) VALUES (?, ?)", [performer_id, alias], commit)

	def insert_model(self, model: PerformerAliasesRow, commit=True):
		return self.execute("INSERT INTO performer_aliases (performer_id, alias) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_performer_id(self, performer_id, commit=True):
		return self.execute("DELETE FROM performer_aliases WHERE performer_id = ?", [performer_id, ], commit)

	def update_alias_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performer_aliases SET alias = ? WHERE performer_id = ?", [value, performer_id], commit)

	def update_empty_alias_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performer_aliases SET alias = ? WHERE performer_id = ? AND (alias IS NULL OR alias = '' OR alias = 0)", [value, performer_id], commit)

class Performers(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'performers')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_disambiguation(self, disambiguation, colvalues={}, selectcols=['*']):
		colvalues['disambiguation'] = disambiguation
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_gender(self, gender, colvalues={}, selectcols=['*']):
		colvalues['gender'] = gender
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_twitter(self, twitter, colvalues={}, selectcols=['*']):
		colvalues['twitter'] = twitter
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_instagram(self, instagram, colvalues={}, selectcols=['*']):
		colvalues['instagram'] = instagram
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_birthdate(self, birthdate, colvalues={}, selectcols=['*']):
		colvalues['birthdate'] = birthdate
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_ethnicity(self, ethnicity, colvalues={}, selectcols=['*']):
		colvalues['ethnicity'] = ethnicity
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_country(self, country, colvalues={}, selectcols=['*']):
		colvalues['country'] = country
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_eye_color(self, eye_color, colvalues={}, selectcols=['*']):
		colvalues['eye_color'] = eye_color
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_height(self, height, colvalues={}, selectcols=['*']):
		colvalues['height'] = height
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_measurements(self, measurements, colvalues={}, selectcols=['*']):
		colvalues['measurements'] = measurements
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_fake_tits(self, fake_tits, colvalues={}, selectcols=['*']):
		colvalues['fake_tits'] = fake_tits
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_career_length(self, career_length, colvalues={}, selectcols=['*']):
		colvalues['career_length'] = career_length
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_tattoos(self, tattoos, colvalues={}, selectcols=['*']):
		colvalues['tattoos'] = tattoos
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_piercings(self, piercings, colvalues={}, selectcols=['*']):
		colvalues['piercings'] = piercings
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_favorite(self, favorite, colvalues={}, selectcols=['*']):
		colvalues['favorite'] = favorite
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_details(self, details, colvalues={}, selectcols=['*']):
		colvalues['details'] = details
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_death_date(self, death_date, colvalues={}, selectcols=['*']):
		colvalues['death_date'] = death_date
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_hair_color(self, hair_color, colvalues={}, selectcols=['*']):
		colvalues['hair_color'] = hair_color
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_weight(self, weight, colvalues={}, selectcols=['*']):
		colvalues['weight'] = weight
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_ignore_auto_tag(self, ignore_auto_tag, colvalues={}, selectcols=['*']):
		colvalues['ignore_auto_tag'] = ignore_auto_tag
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_image_blob(self, image_blob, colvalues={}, selectcols=['*']):
		colvalues['image_blob'] = image_blob
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_penis_length(self, penis_length, colvalues={}, selectcols=['*']):
		colvalues['penis_length'] = penis_length
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_circumcised(self, circumcised, colvalues={}, selectcols=['*']):
		colvalues['circumcised'] = circumcised
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_disambiguation(self, disambiguation, colvalues={}, selectcols=['*']):
		colvalues['disambiguation'] = disambiguation
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_gender(self, gender, colvalues={}, selectcols=['*']):
		colvalues['gender'] = gender
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_twitter(self, twitter, colvalues={}, selectcols=['*']):
		colvalues['twitter'] = twitter
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_instagram(self, instagram, colvalues={}, selectcols=['*']):
		colvalues['instagram'] = instagram
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_birthdate(self, birthdate, colvalues={}, selectcols=['*']):
		colvalues['birthdate'] = birthdate
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_ethnicity(self, ethnicity, colvalues={}, selectcols=['*']):
		colvalues['ethnicity'] = ethnicity
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_country(self, country, colvalues={}, selectcols=['*']):
		colvalues['country'] = country
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_eye_color(self, eye_color, colvalues={}, selectcols=['*']):
		colvalues['eye_color'] = eye_color
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_height(self, height, colvalues={}, selectcols=['*']):
		colvalues['height'] = height
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_measurements(self, measurements, colvalues={}, selectcols=['*']):
		colvalues['measurements'] = measurements
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_fake_tits(self, fake_tits, colvalues={}, selectcols=['*']):
		colvalues['fake_tits'] = fake_tits
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_career_length(self, career_length, colvalues={}, selectcols=['*']):
		colvalues['career_length'] = career_length
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_tattoos(self, tattoos, colvalues={}, selectcols=['*']):
		colvalues['tattoos'] = tattoos
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_piercings(self, piercings, colvalues={}, selectcols=['*']):
		colvalues['piercings'] = piercings
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_favorite(self, favorite, colvalues={}, selectcols=['*']):
		colvalues['favorite'] = favorite
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_details(self, details, colvalues={}, selectcols=['*']):
		colvalues['details'] = details
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_death_date(self, death_date, colvalues={}, selectcols=['*']):
		colvalues['death_date'] = death_date
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_hair_color(self, hair_color, colvalues={}, selectcols=['*']):
		colvalues['hair_color'] = hair_color
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_weight(self, weight, colvalues={}, selectcols=['*']):
		colvalues['weight'] = weight
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_ignore_auto_tag(self, ignore_auto_tag, colvalues={}, selectcols=['*']):
		colvalues['ignore_auto_tag'] = ignore_auto_tag
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_image_blob(self, image_blob, colvalues={}, selectcols=['*']):
		colvalues['image_blob'] = image_blob
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_penis_length(self, penis_length, colvalues={}, selectcols=['*']):
		colvalues['penis_length'] = penis_length
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_circumcised(self, circumcised, colvalues={}, selectcols=['*']):
		colvalues['circumcised'] = circumcised
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def insert(self, name, disambiguation, gender, url, twitter, instagram, birthdate, ethnicity, country, eye_color, height, measurements, fake_tits, career_length, tattoos, piercings, favorite, created_at, updated_at, details, death_date, hair_color, weight, rating, ignore_auto_tag, image_blob, penis_length, circumcised, commit=True):
		return self.execute("INSERT INTO performers (name, disambiguation, gender, url, twitter, instagram, birthdate, ethnicity, country, eye_color, height, measurements, fake_tits, career_length, tattoos, piercings, favorite, created_at, updated_at, details, death_date, hair_color, weight, rating, ignore_auto_tag, image_blob, penis_length, circumcised) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [name, disambiguation, gender, url, twitter, instagram, birthdate, ethnicity, country, eye_color, height, measurements, fake_tits, career_length, tattoos, piercings, favorite, created_at, updated_at, details, death_date, hair_color, weight, rating, ignore_auto_tag, image_blob, penis_length, circumcised], commit)

	def insert_model(self, model: PerformersRow, commit=True):
		return self.execute("INSERT INTO performers (name, disambiguation, gender, url, twitter, instagram, birthdate, ethnicity, country, eye_color, height, measurements, fake_tits, career_length, tattoos, piercings, favorite, created_at, updated_at, details, death_date, hair_color, weight, rating, ignore_auto_tag, image_blob, penis_length, circumcised) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_id(self, id, commit=True):
		return self.execute("DELETE FROM performers WHERE id = ?", [id, ], commit)

	def delete_by_name(self, name, commit=True):
		return self.execute("DELETE FROM performers WHERE name = ?", [name, ], commit)

	def update_disambiguation_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET disambiguation = ? WHERE id = ?", [value, id], commit)

	def update_empty_disambiguation_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET disambiguation = ? WHERE id = ? AND (disambiguation IS NULL OR disambiguation = '' OR disambiguation = 0)", [value, id], commit)

	def update_gender_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET gender = ? WHERE id = ?", [value, id], commit)

	def update_empty_gender_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET gender = ? WHERE id = ? AND (gender IS NULL OR gender = '' OR gender = 0)", [value, id], commit)

	def update_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET url = ? WHERE id = ?", [value, id], commit)

	def update_empty_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET url = ? WHERE id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, id], commit)

	def update_twitter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET twitter = ? WHERE id = ?", [value, id], commit)

	def update_empty_twitter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET twitter = ? WHERE id = ? AND (twitter IS NULL OR twitter = '' OR twitter = 0)", [value, id], commit)

	def update_instagram_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET instagram = ? WHERE id = ?", [value, id], commit)

	def update_empty_instagram_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET instagram = ? WHERE id = ? AND (instagram IS NULL OR instagram = '' OR instagram = 0)", [value, id], commit)

	def update_birthdate_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET birthdate = ? WHERE id = ?", [value, id], commit)

	def update_empty_birthdate_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET birthdate = ? WHERE id = ? AND (birthdate IS NULL OR birthdate = '' OR birthdate = 0)", [value, id], commit)

	def update_ethnicity_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET ethnicity = ? WHERE id = ?", [value, id], commit)

	def update_empty_ethnicity_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET ethnicity = ? WHERE id = ? AND (ethnicity IS NULL OR ethnicity = '' OR ethnicity = 0)", [value, id], commit)

	def update_country_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET country = ? WHERE id = ?", [value, id], commit)

	def update_empty_country_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET country = ? WHERE id = ? AND (country IS NULL OR country = '' OR country = 0)", [value, id], commit)

	def update_eye_color_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET eye_color = ? WHERE id = ?", [value, id], commit)

	def update_empty_eye_color_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET eye_color = ? WHERE id = ? AND (eye_color IS NULL OR eye_color = '' OR eye_color = 0)", [value, id], commit)

	def update_height_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET height = ? WHERE id = ?", [value, id], commit)

	def update_empty_height_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET height = ? WHERE id = ? AND (height IS NULL OR height = '' OR height = 0)", [value, id], commit)

	def update_measurements_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET measurements = ? WHERE id = ?", [value, id], commit)

	def update_empty_measurements_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET measurements = ? WHERE id = ? AND (measurements IS NULL OR measurements = '' OR measurements = 0)", [value, id], commit)

	def update_fake_tits_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET fake_tits = ? WHERE id = ?", [value, id], commit)

	def update_empty_fake_tits_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET fake_tits = ? WHERE id = ? AND (fake_tits IS NULL OR fake_tits = '' OR fake_tits = 0)", [value, id], commit)

	def update_career_length_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET career_length = ? WHERE id = ?", [value, id], commit)

	def update_empty_career_length_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET career_length = ? WHERE id = ? AND (career_length IS NULL OR career_length = '' OR career_length = 0)", [value, id], commit)

	def update_tattoos_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET tattoos = ? WHERE id = ?", [value, id], commit)

	def update_empty_tattoos_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET tattoos = ? WHERE id = ? AND (tattoos IS NULL OR tattoos = '' OR tattoos = 0)", [value, id], commit)

	def update_piercings_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET piercings = ? WHERE id = ?", [value, id], commit)

	def update_empty_piercings_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET piercings = ? WHERE id = ? AND (piercings IS NULL OR piercings = '' OR piercings = 0)", [value, id], commit)

	def update_favorite_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET favorite = ? WHERE id = ?", [value, id], commit)

	def update_empty_favorite_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET favorite = ? WHERE id = ? AND (favorite IS NULL OR favorite = '' OR favorite = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_details_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET details = ? WHERE id = ?", [value, id], commit)

	def update_empty_details_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET details = ? WHERE id = ? AND (details IS NULL OR details = '' OR details = 0)", [value, id], commit)

	def update_death_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET death_date = ? WHERE id = ?", [value, id], commit)

	def update_empty_death_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET death_date = ? WHERE id = ? AND (death_date IS NULL OR death_date = '' OR death_date = 0)", [value, id], commit)

	def update_hair_color_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET hair_color = ? WHERE id = ?", [value, id], commit)

	def update_empty_hair_color_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET hair_color = ? WHERE id = ? AND (hair_color IS NULL OR hair_color = '' OR hair_color = 0)", [value, id], commit)

	def update_weight_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET weight = ? WHERE id = ?", [value, id], commit)

	def update_empty_weight_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET weight = ? WHERE id = ? AND (weight IS NULL OR weight = '' OR weight = 0)", [value, id], commit)

	def update_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET rating = ? WHERE id = ?", [value, id], commit)

	def update_empty_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET rating = ? WHERE id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, id], commit)

	def update_ignore_auto_tag_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET ignore_auto_tag = ? WHERE id = ?", [value, id], commit)

	def update_empty_ignore_auto_tag_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET ignore_auto_tag = ? WHERE id = ? AND (ignore_auto_tag IS NULL OR ignore_auto_tag = '' OR ignore_auto_tag = 0)", [value, id], commit)

	def update_image_blob_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET image_blob = ? WHERE id = ?", [value, id], commit)

	def update_empty_image_blob_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET image_blob = ? WHERE id = ? AND (image_blob IS NULL OR image_blob = '' OR image_blob = 0)", [value, id], commit)

	def update_penis_length_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET penis_length = ? WHERE id = ?", [value, id], commit)

	def update_empty_penis_length_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET penis_length = ? WHERE id = ? AND (penis_length IS NULL OR penis_length = '' OR penis_length = 0)", [value, id], commit)

	def update_circumcised_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET circumcised = ? WHERE id = ?", [value, id], commit)

	def update_empty_circumcised_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET circumcised = ? WHERE id = ? AND (circumcised IS NULL OR circumcised = '' OR circumcised = 0)", [value, id], commit)

	def update_disambiguation_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET disambiguation = ? WHERE name = ?", [value, name], commit)

	def update_empty_disambiguation_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET disambiguation = ? WHERE name = ? AND (disambiguation IS NULL OR disambiguation = '' OR disambiguation = 0)", [value, name], commit)

	def update_gender_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET gender = ? WHERE name = ?", [value, name], commit)

	def update_empty_gender_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET gender = ? WHERE name = ? AND (gender IS NULL OR gender = '' OR gender = 0)", [value, name], commit)

	def update_url_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET url = ? WHERE name = ?", [value, name], commit)

	def update_empty_url_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET url = ? WHERE name = ? AND (url IS NULL OR url = '' OR url = 0)", [value, name], commit)

	def update_twitter_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET twitter = ? WHERE name = ?", [value, name], commit)

	def update_empty_twitter_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET twitter = ? WHERE name = ? AND (twitter IS NULL OR twitter = '' OR twitter = 0)", [value, name], commit)

	def update_instagram_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET instagram = ? WHERE name = ?", [value, name], commit)

	def update_empty_instagram_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET instagram = ? WHERE name = ? AND (instagram IS NULL OR instagram = '' OR instagram = 0)", [value, name], commit)

	def update_birthdate_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET birthdate = ? WHERE name = ?", [value, name], commit)

	def update_empty_birthdate_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET birthdate = ? WHERE name = ? AND (birthdate IS NULL OR birthdate = '' OR birthdate = 0)", [value, name], commit)

	def update_ethnicity_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET ethnicity = ? WHERE name = ?", [value, name], commit)

	def update_empty_ethnicity_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET ethnicity = ? WHERE name = ? AND (ethnicity IS NULL OR ethnicity = '' OR ethnicity = 0)", [value, name], commit)

	def update_country_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET country = ? WHERE name = ?", [value, name], commit)

	def update_empty_country_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET country = ? WHERE name = ? AND (country IS NULL OR country = '' OR country = 0)", [value, name], commit)

	def update_eye_color_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET eye_color = ? WHERE name = ?", [value, name], commit)

	def update_empty_eye_color_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET eye_color = ? WHERE name = ? AND (eye_color IS NULL OR eye_color = '' OR eye_color = 0)", [value, name], commit)

	def update_height_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET height = ? WHERE name = ?", [value, name], commit)

	def update_empty_height_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET height = ? WHERE name = ? AND (height IS NULL OR height = '' OR height = 0)", [value, name], commit)

	def update_measurements_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET measurements = ? WHERE name = ?", [value, name], commit)

	def update_empty_measurements_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET measurements = ? WHERE name = ? AND (measurements IS NULL OR measurements = '' OR measurements = 0)", [value, name], commit)

	def update_fake_tits_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET fake_tits = ? WHERE name = ?", [value, name], commit)

	def update_empty_fake_tits_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET fake_tits = ? WHERE name = ? AND (fake_tits IS NULL OR fake_tits = '' OR fake_tits = 0)", [value, name], commit)

	def update_career_length_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET career_length = ? WHERE name = ?", [value, name], commit)

	def update_empty_career_length_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET career_length = ? WHERE name = ? AND (career_length IS NULL OR career_length = '' OR career_length = 0)", [value, name], commit)

	def update_tattoos_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET tattoos = ? WHERE name = ?", [value, name], commit)

	def update_empty_tattoos_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET tattoos = ? WHERE name = ? AND (tattoos IS NULL OR tattoos = '' OR tattoos = 0)", [value, name], commit)

	def update_piercings_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET piercings = ? WHERE name = ?", [value, name], commit)

	def update_empty_piercings_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET piercings = ? WHERE name = ? AND (piercings IS NULL OR piercings = '' OR piercings = 0)", [value, name], commit)

	def update_favorite_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET favorite = ? WHERE name = ?", [value, name], commit)

	def update_empty_favorite_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET favorite = ? WHERE name = ? AND (favorite IS NULL OR favorite = '' OR favorite = 0)", [value, name], commit)

	def update_created_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET created_at = ? WHERE name = ?", [value, name], commit)

	def update_empty_created_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET created_at = ? WHERE name = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, name], commit)

	def update_updated_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET updated_at = ? WHERE name = ?", [value, name], commit)

	def update_empty_updated_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET updated_at = ? WHERE name = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, name], commit)

	def update_details_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET details = ? WHERE name = ?", [value, name], commit)

	def update_empty_details_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET details = ? WHERE name = ? AND (details IS NULL OR details = '' OR details = 0)", [value, name], commit)

	def update_death_date_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET death_date = ? WHERE name = ?", [value, name], commit)

	def update_empty_death_date_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET death_date = ? WHERE name = ? AND (death_date IS NULL OR death_date = '' OR death_date = 0)", [value, name], commit)

	def update_hair_color_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET hair_color = ? WHERE name = ?", [value, name], commit)

	def update_empty_hair_color_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET hair_color = ? WHERE name = ? AND (hair_color IS NULL OR hair_color = '' OR hair_color = 0)", [value, name], commit)

	def update_weight_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET weight = ? WHERE name = ?", [value, name], commit)

	def update_empty_weight_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET weight = ? WHERE name = ? AND (weight IS NULL OR weight = '' OR weight = 0)", [value, name], commit)

	def update_rating_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET rating = ? WHERE name = ?", [value, name], commit)

	def update_empty_rating_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET rating = ? WHERE name = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, name], commit)

	def update_ignore_auto_tag_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET ignore_auto_tag = ? WHERE name = ?", [value, name], commit)

	def update_empty_ignore_auto_tag_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET ignore_auto_tag = ? WHERE name = ? AND (ignore_auto_tag IS NULL OR ignore_auto_tag = '' OR ignore_auto_tag = 0)", [value, name], commit)

	def update_image_blob_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET image_blob = ? WHERE name = ?", [value, name], commit)

	def update_empty_image_blob_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET image_blob = ? WHERE name = ? AND (image_blob IS NULL OR image_blob = '' OR image_blob = 0)", [value, name], commit)

	def update_penis_length_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET penis_length = ? WHERE name = ?", [value, name], commit)

	def update_empty_penis_length_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET penis_length = ? WHERE name = ? AND (penis_length IS NULL OR penis_length = '' OR penis_length = 0)", [value, name], commit)

	def update_circumcised_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET circumcised = ? WHERE name = ?", [value, name], commit)

	def update_empty_circumcised_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET circumcised = ? WHERE name = ? AND (circumcised IS NULL OR circumcised = '' OR circumcised = 0)", [value, name], commit)

class GalleriesChapters(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'galleries_chapters')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [GalleriesChaptersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		return [GalleriesChaptersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_image_index(self, image_index, colvalues={}, selectcols=['*']):
		colvalues['image_index'] = image_index
		return [GalleriesChaptersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		return [GalleriesChaptersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [GalleriesChaptersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [GalleriesChaptersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesChaptersRow().from_sqliterow(row)
		else:
			return None

	def selectone_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesChaptersRow().from_sqliterow(row)
		else:
			return None

	def selectone_image_index(self, image_index, colvalues={}, selectcols=['*']):
		colvalues['image_index'] = image_index
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesChaptersRow().from_sqliterow(row)
		else:
			return None

	def selectone_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesChaptersRow().from_sqliterow(row)
		else:
			return None

	def selectone_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesChaptersRow().from_sqliterow(row)
		else:
			return None

	def selectone_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesChaptersRow().from_sqliterow(row)
		else:
			return None

	def insert(self, title, image_index, gallery_id, created_at, updated_at, commit=True):
		return self.execute("INSERT INTO galleries_chapters (title, image_index, gallery_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?)", [title, image_index, gallery_id, created_at, updated_at], commit)

	def insert_model(self, model: GalleriesChaptersRow, commit=True):
		return self.execute("INSERT INTO galleries_chapters (title, image_index, gallery_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_id(self, id, commit=True):
		return self.execute("DELETE FROM galleries_chapters WHERE id = ?", [id, ], commit)

	def delete_by_gallery_id(self, gallery_id, commit=True):
		return self.execute("DELETE FROM galleries_chapters WHERE gallery_id = ?", [gallery_id, ], commit)

	def update_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET title = ? WHERE id = ?", [value, id], commit)

	def update_empty_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET title = ? WHERE id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, id], commit)

	def update_image_index_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET image_index = ? WHERE id = ?", [value, id], commit)

	def update_empty_image_index_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET image_index = ? WHERE id = ? AND (image_index IS NULL OR image_index = '' OR image_index = 0)", [value, id], commit)

	def update_gallery_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET gallery_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_gallery_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET gallery_id = ? WHERE id = ? AND (gallery_id IS NULL OR gallery_id = '' OR gallery_id = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_title_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET title = ? WHERE gallery_id = ?", [value, gallery_id], commit)

	def update_empty_title_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET title = ? WHERE gallery_id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, gallery_id], commit)

	def update_image_index_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET image_index = ? WHERE gallery_id = ?", [value, gallery_id], commit)

	def update_empty_image_index_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET image_index = ? WHERE gallery_id = ? AND (image_index IS NULL OR image_index = '' OR image_index = 0)", [value, gallery_id], commit)

	def update_created_at_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET created_at = ? WHERE gallery_id = ?", [value, gallery_id], commit)

	def update_empty_created_at_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET created_at = ? WHERE gallery_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, gallery_id], commit)

	def update_updated_at_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET updated_at = ? WHERE gallery_id = ?", [value, gallery_id], commit)

	def update_empty_updated_at_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE galleries_chapters SET updated_at = ? WHERE gallery_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, gallery_id], commit)

class Blobs(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'blobs')

	def select_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
		return [BlobsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_blob(self, blob, colvalues={}, selectcols=['*']):
		colvalues['blob'] = blob
		return [BlobsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
		row = self.selectone(colvalues, selectcols)
		if row:
			return BlobsRow().from_sqliterow(row)
		else:
			return None

	def selectone_blob(self, blob, colvalues={}, selectcols=['*']):
		colvalues['blob'] = blob
		row = self.selectone(colvalues, selectcols)
		if row:
			return BlobsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, checksum, blob, commit=True):
		return self.execute("INSERT INTO blobs (checksum, blob) VALUES (?, ?)", [checksum, blob], commit)

	def insert_model(self, model: BlobsRow, commit=True):
		return self.execute("INSERT INTO blobs (checksum, blob) VALUES (?, ?)", model.values_list(False), commit)

	def delete_by_checksum(self, checksum, commit=True):
		return self.execute("DELETE FROM blobs WHERE checksum = ?", [checksum, ], commit)

	def update_blob_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE blobs SET blob = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_blob_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE blobs SET blob = ? WHERE checksum = ? AND (blob IS NULL OR blob = '' OR blob = 0)", [value, checksum], commit)

class SceneUrls(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'scene_urls')

	def select_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		return [SceneUrlsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_position(self, position, colvalues={}, selectcols=['*']):
		colvalues['position'] = position
		return [SceneUrlsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		return [SceneUrlsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneUrlsRow().from_sqliterow(row)
		else:
			return None

	def selectone_position(self, position, colvalues={}, selectcols=['*']):
		colvalues['position'] = position
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneUrlsRow().from_sqliterow(row)
		else:
			return None

	def selectone_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneUrlsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, scene_id, position, url, commit=True):
		return self.execute("INSERT INTO scene_urls (scene_id, position, url) VALUES (?, ?, ?)", [scene_id, position, url], commit)

	def insert_model(self, model: SceneUrlsRow, commit=True):
		return self.execute("INSERT INTO scene_urls (scene_id, position, url) VALUES (?, ?, ?)", model.values_list(False), commit)

	def delete_by_scene_id(self, scene_id, commit=True):
		return self.execute("DELETE FROM scene_urls WHERE scene_id = ?", [scene_id, ], commit)

	def update_position_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_urls SET position = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_position_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_urls SET position = ? WHERE scene_id = ? AND (position IS NULL OR position = '' OR position = 0)", [value, scene_id], commit)

	def update_url_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_urls SET url = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_url_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_urls SET url = ? WHERE scene_id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, scene_id], commit)

class Scenes(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'scenes')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_details(self, details, colvalues={}, selectcols=['*']):
		colvalues['details'] = details
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_date(self, date, colvalues={}, selectcols=['*']):
		colvalues['date'] = date
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_o_counter(self, o_counter, colvalues={}, selectcols=['*']):
		colvalues['o_counter'] = o_counter
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_organized(self, organized, colvalues={}, selectcols=['*']):
		colvalues['organized'] = organized
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_code(self, code, colvalues={}, selectcols=['*']):
		colvalues['code'] = code
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_director(self, director, colvalues={}, selectcols=['*']):
		colvalues['director'] = director
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_resume_time(self, resume_time, colvalues={}, selectcols=['*']):
		colvalues['resume_time'] = resume_time
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_last_played_at(self, last_played_at, colvalues={}, selectcols=['*']):
		colvalues['last_played_at'] = last_played_at
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_play_count(self, play_count, colvalues={}, selectcols=['*']):
		colvalues['play_count'] = play_count
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_play_duration(self, play_duration, colvalues={}, selectcols=['*']):
		colvalues['play_duration'] = play_duration
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_cover_blob(self, cover_blob, colvalues={}, selectcols=['*']):
		colvalues['cover_blob'] = cover_blob
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_details(self, details, colvalues={}, selectcols=['*']):
		colvalues['details'] = details
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_date(self, date, colvalues={}, selectcols=['*']):
		colvalues['date'] = date
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_o_counter(self, o_counter, colvalues={}, selectcols=['*']):
		colvalues['o_counter'] = o_counter
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_organized(self, organized, colvalues={}, selectcols=['*']):
		colvalues['organized'] = organized
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_code(self, code, colvalues={}, selectcols=['*']):
		colvalues['code'] = code
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_director(self, director, colvalues={}, selectcols=['*']):
		colvalues['director'] = director
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_resume_time(self, resume_time, colvalues={}, selectcols=['*']):
		colvalues['resume_time'] = resume_time
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_last_played_at(self, last_played_at, colvalues={}, selectcols=['*']):
		colvalues['last_played_at'] = last_played_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_play_count(self, play_count, colvalues={}, selectcols=['*']):
		colvalues['play_count'] = play_count
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_play_duration(self, play_duration, colvalues={}, selectcols=['*']):
		colvalues['play_duration'] = play_duration
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_cover_blob(self, cover_blob, colvalues={}, selectcols=['*']):
		colvalues['cover_blob'] = cover_blob
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, title, details, date, rating, studio_id, o_counter, organized, created_at, updated_at, code, director, resume_time, last_played_at, play_count, play_duration, cover_blob, commit=True):
		return self.execute("INSERT INTO scenes (title, details, date, rating, studio_id, o_counter, organized, created_at, updated_at, code, director, resume_time, last_played_at, play_count, play_duration, cover_blob) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [title, details, date, rating, studio_id, o_counter, organized, created_at, updated_at, code, director, resume_time, last_played_at, play_count, play_duration, cover_blob], commit)

	def insert_model(self, model: ScenesRow, commit=True):
		return self.execute("INSERT INTO scenes (title, details, date, rating, studio_id, o_counter, organized, created_at, updated_at, code, director, resume_time, last_played_at, play_count, play_duration, cover_blob) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_id(self, id, commit=True):
		return self.execute("DELETE FROM scenes WHERE id = ?", [id, ], commit)

	def delete_by_studio_id(self, studio_id, commit=True):
		return self.execute("DELETE FROM scenes WHERE studio_id = ?", [studio_id, ], commit)

	def update_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE id = ?", [value, id], commit)

	def update_empty_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, id], commit)

	def update_details_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE id = ?", [value, id], commit)

	def update_empty_details_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE id = ? AND (details IS NULL OR details = '' OR details = 0)", [value, id], commit)

	def update_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE id = ?", [value, id], commit)

	def update_empty_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, id], commit)

	def update_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE id = ?", [value, id], commit)

	def update_empty_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, id], commit)

	def update_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET studio_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET studio_id = ? WHERE id = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, id], commit)

	def update_o_counter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE id = ?", [value, id], commit)

	def update_empty_o_counter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE id = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, id], commit)

	def update_organized_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE id = ?", [value, id], commit)

	def update_empty_organized_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE id = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_code_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET code = ? WHERE id = ?", [value, id], commit)

	def update_empty_code_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET code = ? WHERE id = ? AND (code IS NULL OR code = '' OR code = 0)", [value, id], commit)

	def update_director_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET director = ? WHERE id = ?", [value, id], commit)

	def update_empty_director_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET director = ? WHERE id = ? AND (director IS NULL OR director = '' OR director = 0)", [value, id], commit)

	def update_resume_time_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET resume_time = ? WHERE id = ?", [value, id], commit)

	def update_empty_resume_time_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET resume_time = ? WHERE id = ? AND (resume_time IS NULL OR resume_time = '' OR resume_time = 0)", [value, id], commit)

	def update_last_played_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET last_played_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_last_played_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET last_played_at = ? WHERE id = ? AND (last_played_at IS NULL OR last_played_at = '' OR last_played_at = 0)", [value, id], commit)

	def update_play_count_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET play_count = ? WHERE id = ?", [value, id], commit)

	def update_empty_play_count_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET play_count = ? WHERE id = ? AND (play_count IS NULL OR play_count = '' OR play_count = 0)", [value, id], commit)

	def update_play_duration_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET play_duration = ? WHERE id = ?", [value, id], commit)

	def update_empty_play_duration_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET play_duration = ? WHERE id = ? AND (play_duration IS NULL OR play_duration = '' OR play_duration = 0)", [value, id], commit)

	def update_cover_blob_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET cover_blob = ? WHERE id = ?", [value, id], commit)

	def update_empty_cover_blob_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET cover_blob = ? WHERE id = ? AND (cover_blob IS NULL OR cover_blob = '' OR cover_blob = 0)", [value, id], commit)

	def update_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE studio_id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, studio_id], commit)

	def update_details_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_details_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE studio_id = ? AND (details IS NULL OR details = '' OR details = 0)", [value, studio_id], commit)

	def update_date_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_date_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE studio_id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, studio_id], commit)

	def update_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE studio_id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, studio_id], commit)

	def update_o_counter_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_o_counter_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE studio_id = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, studio_id], commit)

	def update_organized_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_organized_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE studio_id = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, studio_id], commit)

	def update_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE studio_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, studio_id], commit)

	def update_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE studio_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, studio_id], commit)

	def update_code_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET code = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_code_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET code = ? WHERE studio_id = ? AND (code IS NULL OR code = '' OR code = 0)", [value, studio_id], commit)

	def update_director_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET director = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_director_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET director = ? WHERE studio_id = ? AND (director IS NULL OR director = '' OR director = 0)", [value, studio_id], commit)

	def update_resume_time_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET resume_time = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_resume_time_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET resume_time = ? WHERE studio_id = ? AND (resume_time IS NULL OR resume_time = '' OR resume_time = 0)", [value, studio_id], commit)

	def update_last_played_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET last_played_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_last_played_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET last_played_at = ? WHERE studio_id = ? AND (last_played_at IS NULL OR last_played_at = '' OR last_played_at = 0)", [value, studio_id], commit)

	def update_play_count_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET play_count = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_play_count_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET play_count = ? WHERE studio_id = ? AND (play_count IS NULL OR play_count = '' OR play_count = 0)", [value, studio_id], commit)

	def update_play_duration_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET play_duration = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_play_duration_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET play_duration = ? WHERE studio_id = ? AND (play_duration IS NULL OR play_duration = '' OR play_duration = 0)", [value, studio_id], commit)

	def update_cover_blob_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET cover_blob = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_cover_blob_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET cover_blob = ? WHERE studio_id = ? AND (cover_blob IS NULL OR cover_blob = '' OR cover_blob = 0)", [value, studio_id], commit)

class SceneMarkers(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'scene_markers')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [SceneMarkersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		return [SceneMarkersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_seconds(self, seconds, colvalues={}, selectcols=['*']):
		colvalues['seconds'] = seconds
		return [SceneMarkersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_primary_tag_id(self, primary_tag_id, colvalues={}, selectcols=['*']):
		colvalues['primary_tag_id'] = primary_tag_id
		return [SceneMarkersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		return [SceneMarkersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [SceneMarkersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [SceneMarkersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneMarkersRow().from_sqliterow(row)
		else:
			return None

	def selectone_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneMarkersRow().from_sqliterow(row)
		else:
			return None

	def selectone_seconds(self, seconds, colvalues={}, selectcols=['*']):
		colvalues['seconds'] = seconds
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneMarkersRow().from_sqliterow(row)
		else:
			return None

	def selectone_primary_tag_id(self, primary_tag_id, colvalues={}, selectcols=['*']):
		colvalues['primary_tag_id'] = primary_tag_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneMarkersRow().from_sqliterow(row)
		else:
			return None

	def selectone_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneMarkersRow().from_sqliterow(row)
		else:
			return None

	def selectone_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneMarkersRow().from_sqliterow(row)
		else:
			return None

	def selectone_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneMarkersRow().from_sqliterow(row)
		else:
			return None

	def insert(self, title, seconds, primary_tag_id, scene_id, created_at, updated_at, commit=True):
		return self.execute("INSERT INTO scene_markers (title, seconds, primary_tag_id, scene_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)", [title, seconds, primary_tag_id, scene_id, created_at, updated_at], commit)

	def insert_model(self, model: SceneMarkersRow, commit=True):
		return self.execute("INSERT INTO scene_markers (title, seconds, primary_tag_id, scene_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_id(self, id, commit=True):
		return self.execute("DELETE FROM scene_markers WHERE id = ?", [id, ], commit)

	def delete_by_primary_tag_id(self, primary_tag_id, commit=True):
		return self.execute("DELETE FROM scene_markers WHERE primary_tag_id = ?", [primary_tag_id, ], commit)

	def delete_by_scene_id(self, scene_id, commit=True):
		return self.execute("DELETE FROM scene_markers WHERE scene_id = ?", [scene_id, ], commit)

	def update_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scene_markers SET title = ? WHERE id = ?", [value, id], commit)

	def update_empty_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scene_markers SET title = ? WHERE id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, id], commit)

	def update_seconds_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scene_markers SET seconds = ? WHERE id = ?", [value, id], commit)

	def update_empty_seconds_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scene_markers SET seconds = ? WHERE id = ? AND (seconds IS NULL OR seconds = '' OR seconds = 0)", [value, id], commit)

	def update_primary_tag_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scene_markers SET primary_tag_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_primary_tag_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scene_markers SET primary_tag_id = ? WHERE id = ? AND (primary_tag_id IS NULL OR primary_tag_id = '' OR primary_tag_id = 0)", [value, id], commit)

	def update_scene_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scene_markers SET scene_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_scene_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scene_markers SET scene_id = ? WHERE id = ? AND (scene_id IS NULL OR scene_id = '' OR scene_id = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scene_markers SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scene_markers SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scene_markers SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scene_markers SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_title_by_primary_tag_id(self, primary_tag_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET title = ? WHERE primary_tag_id = ?", [value, primary_tag_id], commit)

	def update_empty_title_by_primary_tag_id(self, primary_tag_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET title = ? WHERE primary_tag_id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, primary_tag_id], commit)

	def update_seconds_by_primary_tag_id(self, primary_tag_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET seconds = ? WHERE primary_tag_id = ?", [value, primary_tag_id], commit)

	def update_empty_seconds_by_primary_tag_id(self, primary_tag_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET seconds = ? WHERE primary_tag_id = ? AND (seconds IS NULL OR seconds = '' OR seconds = 0)", [value, primary_tag_id], commit)

	def update_scene_id_by_primary_tag_id(self, primary_tag_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET scene_id = ? WHERE primary_tag_id = ?", [value, primary_tag_id], commit)

	def update_empty_scene_id_by_primary_tag_id(self, primary_tag_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET scene_id = ? WHERE primary_tag_id = ? AND (scene_id IS NULL OR scene_id = '' OR scene_id = 0)", [value, primary_tag_id], commit)

	def update_created_at_by_primary_tag_id(self, primary_tag_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET created_at = ? WHERE primary_tag_id = ?", [value, primary_tag_id], commit)

	def update_empty_created_at_by_primary_tag_id(self, primary_tag_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET created_at = ? WHERE primary_tag_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, primary_tag_id], commit)

	def update_updated_at_by_primary_tag_id(self, primary_tag_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET updated_at = ? WHERE primary_tag_id = ?", [value, primary_tag_id], commit)

	def update_empty_updated_at_by_primary_tag_id(self, primary_tag_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET updated_at = ? WHERE primary_tag_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, primary_tag_id], commit)

	def update_title_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET title = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_title_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET title = ? WHERE scene_id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, scene_id], commit)

	def update_seconds_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET seconds = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_seconds_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET seconds = ? WHERE scene_id = ? AND (seconds IS NULL OR seconds = '' OR seconds = 0)", [value, scene_id], commit)

	def update_primary_tag_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET primary_tag_id = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_primary_tag_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET primary_tag_id = ? WHERE scene_id = ? AND (primary_tag_id IS NULL OR primary_tag_id = '' OR primary_tag_id = 0)", [value, scene_id], commit)

	def update_created_at_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET created_at = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_created_at_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET created_at = ? WHERE scene_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, scene_id], commit)

	def update_updated_at_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET updated_at = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_updated_at_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_markers SET updated_at = ? WHERE scene_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, scene_id], commit)

class Movies(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'movies')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_aliases(self, aliases, colvalues={}, selectcols=['*']):
		colvalues['aliases'] = aliases
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_duration(self, duration, colvalues={}, selectcols=['*']):
		colvalues['duration'] = duration
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_date(self, date, colvalues={}, selectcols=['*']):
		colvalues['date'] = date
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_director(self, director, colvalues={}, selectcols=['*']):
		colvalues['director'] = director
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_synopsis(self, synopsis, colvalues={}, selectcols=['*']):
		colvalues['synopsis'] = synopsis
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_front_image_blob(self, front_image_blob, colvalues={}, selectcols=['*']):
		colvalues['front_image_blob'] = front_image_blob
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_back_image_blob(self, back_image_blob, colvalues={}, selectcols=['*']):
		colvalues['back_image_blob'] = back_image_blob
		return [MoviesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_aliases(self, aliases, colvalues={}, selectcols=['*']):
		colvalues['aliases'] = aliases
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_duration(self, duration, colvalues={}, selectcols=['*']):
		colvalues['duration'] = duration
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_date(self, date, colvalues={}, selectcols=['*']):
		colvalues['date'] = date
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_director(self, director, colvalues={}, selectcols=['*']):
		colvalues['director'] = director
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_synopsis(self, synopsis, colvalues={}, selectcols=['*']):
		colvalues['synopsis'] = synopsis
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_front_image_blob(self, front_image_blob, colvalues={}, selectcols=['*']):
		colvalues['front_image_blob'] = front_image_blob
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def selectone_back_image_blob(self, back_image_blob, colvalues={}, selectcols=['*']):
		colvalues['back_image_blob'] = back_image_blob
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, name, aliases, duration, date, rating, studio_id, director, synopsis, url, created_at, updated_at, front_image_blob, back_image_blob, commit=True):
		return self.execute("INSERT INTO movies (name, aliases, duration, date, rating, studio_id, director, synopsis, url, created_at, updated_at, front_image_blob, back_image_blob) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [name, aliases, duration, date, rating, studio_id, director, synopsis, url, created_at, updated_at, front_image_blob, back_image_blob], commit)

	def insert_model(self, model: MoviesRow, commit=True):
		return self.execute("INSERT INTO movies (name, aliases, duration, date, rating, studio_id, director, synopsis, url, created_at, updated_at, front_image_blob, back_image_blob) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_id(self, id, commit=True):
		return self.execute("DELETE FROM movies WHERE id = ?", [id, ], commit)

	def delete_by_name(self, name, commit=True):
		return self.execute("DELETE FROM movies WHERE name = ?", [name, ], commit)

	def delete_by_studio_id(self, studio_id, commit=True):
		return self.execute("DELETE FROM movies WHERE studio_id = ?", [studio_id, ], commit)

	def update_aliases_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET aliases = ? WHERE id = ?", [value, id], commit)

	def update_empty_aliases_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET aliases = ? WHERE id = ? AND (aliases IS NULL OR aliases = '' OR aliases = 0)", [value, id], commit)

	def update_duration_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET duration = ? WHERE id = ?", [value, id], commit)

	def update_empty_duration_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET duration = ? WHERE id = ? AND (duration IS NULL OR duration = '' OR duration = 0)", [value, id], commit)

	def update_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET date = ? WHERE id = ?", [value, id], commit)

	def update_empty_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET date = ? WHERE id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, id], commit)

	def update_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET rating = ? WHERE id = ?", [value, id], commit)

	def update_empty_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET rating = ? WHERE id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, id], commit)

	def update_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET studio_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET studio_id = ? WHERE id = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, id], commit)

	def update_director_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET director = ? WHERE id = ?", [value, id], commit)

	def update_empty_director_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET director = ? WHERE id = ? AND (director IS NULL OR director = '' OR director = 0)", [value, id], commit)

	def update_synopsis_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET synopsis = ? WHERE id = ?", [value, id], commit)

	def update_empty_synopsis_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET synopsis = ? WHERE id = ? AND (synopsis IS NULL OR synopsis = '' OR synopsis = 0)", [value, id], commit)

	def update_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET url = ? WHERE id = ?", [value, id], commit)

	def update_empty_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET url = ? WHERE id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_front_image_blob_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET front_image_blob = ? WHERE id = ?", [value, id], commit)

	def update_empty_front_image_blob_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET front_image_blob = ? WHERE id = ? AND (front_image_blob IS NULL OR front_image_blob = '' OR front_image_blob = 0)", [value, id], commit)

	def update_back_image_blob_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET back_image_blob = ? WHERE id = ?", [value, id], commit)

	def update_empty_back_image_blob_by_id(self, id, value, commit=True):
		return self.execute("UPDATE movies SET back_image_blob = ? WHERE id = ? AND (back_image_blob IS NULL OR back_image_blob = '' OR back_image_blob = 0)", [value, id], commit)

	def update_aliases_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET aliases = ? WHERE name = ?", [value, name], commit)

	def update_empty_aliases_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET aliases = ? WHERE name = ? AND (aliases IS NULL OR aliases = '' OR aliases = 0)", [value, name], commit)

	def update_duration_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET duration = ? WHERE name = ?", [value, name], commit)

	def update_empty_duration_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET duration = ? WHERE name = ? AND (duration IS NULL OR duration = '' OR duration = 0)", [value, name], commit)

	def update_date_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET date = ? WHERE name = ?", [value, name], commit)

	def update_empty_date_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET date = ? WHERE name = ? AND (date IS NULL OR date = '' OR date = 0)", [value, name], commit)

	def update_rating_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET rating = ? WHERE name = ?", [value, name], commit)

	def update_empty_rating_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET rating = ? WHERE name = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, name], commit)

	def update_studio_id_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET studio_id = ? WHERE name = ?", [value, name], commit)

	def update_empty_studio_id_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET studio_id = ? WHERE name = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, name], commit)

	def update_director_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET director = ? WHERE name = ?", [value, name], commit)

	def update_empty_director_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET director = ? WHERE name = ? AND (director IS NULL OR director = '' OR director = 0)", [value, name], commit)

	def update_synopsis_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET synopsis = ? WHERE name = ?", [value, name], commit)

	def update_empty_synopsis_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET synopsis = ? WHERE name = ? AND (synopsis IS NULL OR synopsis = '' OR synopsis = 0)", [value, name], commit)

	def update_url_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET url = ? WHERE name = ?", [value, name], commit)

	def update_empty_url_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET url = ? WHERE name = ? AND (url IS NULL OR url = '' OR url = 0)", [value, name], commit)

	def update_created_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET created_at = ? WHERE name = ?", [value, name], commit)

	def update_empty_created_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET created_at = ? WHERE name = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, name], commit)

	def update_updated_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET updated_at = ? WHERE name = ?", [value, name], commit)

	def update_empty_updated_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET updated_at = ? WHERE name = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, name], commit)

	def update_front_image_blob_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET front_image_blob = ? WHERE name = ?", [value, name], commit)

	def update_empty_front_image_blob_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET front_image_blob = ? WHERE name = ? AND (front_image_blob IS NULL OR front_image_blob = '' OR front_image_blob = 0)", [value, name], commit)

	def update_back_image_blob_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET back_image_blob = ? WHERE name = ?", [value, name], commit)

	def update_empty_back_image_blob_by_name(self, name, value, commit=True):
		return self.execute("UPDATE movies SET back_image_blob = ? WHERE name = ? AND (back_image_blob IS NULL OR back_image_blob = '' OR back_image_blob = 0)", [value, name], commit)

	def update_aliases_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET aliases = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_aliases_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET aliases = ? WHERE studio_id = ? AND (aliases IS NULL OR aliases = '' OR aliases = 0)", [value, studio_id], commit)

	def update_duration_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET duration = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_duration_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET duration = ? WHERE studio_id = ? AND (duration IS NULL OR duration = '' OR duration = 0)", [value, studio_id], commit)

	def update_date_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET date = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_date_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET date = ? WHERE studio_id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, studio_id], commit)

	def update_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET rating = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET rating = ? WHERE studio_id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, studio_id], commit)

	def update_director_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET director = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_director_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET director = ? WHERE studio_id = ? AND (director IS NULL OR director = '' OR director = 0)", [value, studio_id], commit)

	def update_synopsis_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET synopsis = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_synopsis_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET synopsis = ? WHERE studio_id = ? AND (synopsis IS NULL OR synopsis = '' OR synopsis = 0)", [value, studio_id], commit)

	def update_url_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET url = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_url_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET url = ? WHERE studio_id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, studio_id], commit)

	def update_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET created_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET created_at = ? WHERE studio_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, studio_id], commit)

	def update_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET updated_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET updated_at = ? WHERE studio_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, studio_id], commit)

	def update_front_image_blob_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET front_image_blob = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_front_image_blob_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET front_image_blob = ? WHERE studio_id = ? AND (front_image_blob IS NULL OR front_image_blob = '' OR front_image_blob = 0)", [value, studio_id], commit)

	def update_back_image_blob_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET back_image_blob = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_back_image_blob_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE movies SET back_image_blob = ? WHERE studio_id = ? AND (back_image_blob IS NULL OR back_image_blob = '' OR back_image_blob = 0)", [value, studio_id], commit)

class Studios(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'studios')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [StudiosRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
		return [StudiosRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		return [StudiosRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_parent_id(self, parent_id, colvalues={}, selectcols=['*']):
		colvalues['parent_id'] = parent_id
		return [StudiosRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [StudiosRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [StudiosRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_details(self, details, colvalues={}, selectcols=['*']):
		colvalues['details'] = details
		return [StudiosRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		return [StudiosRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_ignore_auto_tag(self, ignore_auto_tag, colvalues={}, selectcols=['*']):
		colvalues['ignore_auto_tag'] = ignore_auto_tag
		return [StudiosRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_image_blob(self, image_blob, colvalues={}, selectcols=['*']):
		colvalues['image_blob'] = image_blob
		return [StudiosRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosRow().from_sqliterow(row)
		else:
			return None

	def selectone_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosRow().from_sqliterow(row)
		else:
			return None

	def selectone_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosRow().from_sqliterow(row)
		else:
			return None

	def selectone_parent_id(self, parent_id, colvalues={}, selectcols=['*']):
		colvalues['parent_id'] = parent_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosRow().from_sqliterow(row)
		else:
			return None

	def selectone_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosRow().from_sqliterow(row)
		else:
			return None

	def selectone_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosRow().from_sqliterow(row)
		else:
			return None

	def selectone_details(self, details, colvalues={}, selectcols=['*']):
		colvalues['details'] = details
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosRow().from_sqliterow(row)
		else:
			return None

	def selectone_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosRow().from_sqliterow(row)
		else:
			return None

	def selectone_ignore_auto_tag(self, ignore_auto_tag, colvalues={}, selectcols=['*']):
		colvalues['ignore_auto_tag'] = ignore_auto_tag
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosRow().from_sqliterow(row)
		else:
			return None

	def selectone_image_blob(self, image_blob, colvalues={}, selectcols=['*']):
		colvalues['image_blob'] = image_blob
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosRow().from_sqliterow(row)
		else:
			return None

	def insert(self, name, url, parent_id, created_at, updated_at, details, rating, ignore_auto_tag, image_blob, commit=True):
		return self.execute("INSERT INTO studios (name, url, parent_id, created_at, updated_at, details, rating, ignore_auto_tag, image_blob) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", [name, url, parent_id, created_at, updated_at, details, rating, ignore_auto_tag, image_blob], commit)

	def insert_model(self, model: StudiosRow, commit=True):
		return self.execute("INSERT INTO studios (name, url, parent_id, created_at, updated_at, details, rating, ignore_auto_tag, image_blob) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_id(self, id, commit=True):
		return self.execute("DELETE FROM studios WHERE id = ?", [id, ], commit)

	def delete_by_name(self, name, commit=True):
		return self.execute("DELETE FROM studios WHERE name = ?", [name, ], commit)

	def delete_by_parent_id(self, parent_id, commit=True):
		return self.execute("DELETE FROM studios WHERE parent_id = ?", [parent_id, ], commit)

	def update_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET url = ? WHERE id = ?", [value, id], commit)

	def update_empty_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET url = ? WHERE id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, id], commit)

	def update_parent_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET parent_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_parent_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET parent_id = ? WHERE id = ? AND (parent_id IS NULL OR parent_id = '' OR parent_id = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_details_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET details = ? WHERE id = ?", [value, id], commit)

	def update_empty_details_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET details = ? WHERE id = ? AND (details IS NULL OR details = '' OR details = 0)", [value, id], commit)

	def update_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET rating = ? WHERE id = ?", [value, id], commit)

	def update_empty_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET rating = ? WHERE id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, id], commit)

	def update_ignore_auto_tag_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET ignore_auto_tag = ? WHERE id = ?", [value, id], commit)

	def update_empty_ignore_auto_tag_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET ignore_auto_tag = ? WHERE id = ? AND (ignore_auto_tag IS NULL OR ignore_auto_tag = '' OR ignore_auto_tag = 0)", [value, id], commit)

	def update_image_blob_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET image_blob = ? WHERE id = ?", [value, id], commit)

	def update_empty_image_blob_by_id(self, id, value, commit=True):
		return self.execute("UPDATE studios SET image_blob = ? WHERE id = ? AND (image_blob IS NULL OR image_blob = '' OR image_blob = 0)", [value, id], commit)

	def update_url_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET url = ? WHERE name = ?", [value, name], commit)

	def update_empty_url_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET url = ? WHERE name = ? AND (url IS NULL OR url = '' OR url = 0)", [value, name], commit)

	def update_parent_id_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET parent_id = ? WHERE name = ?", [value, name], commit)

	def update_empty_parent_id_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET parent_id = ? WHERE name = ? AND (parent_id IS NULL OR parent_id = '' OR parent_id = 0)", [value, name], commit)

	def update_created_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET created_at = ? WHERE name = ?", [value, name], commit)

	def update_empty_created_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET created_at = ? WHERE name = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, name], commit)

	def update_updated_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET updated_at = ? WHERE name = ?", [value, name], commit)

	def update_empty_updated_at_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET updated_at = ? WHERE name = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, name], commit)

	def update_details_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET details = ? WHERE name = ?", [value, name], commit)

	def update_empty_details_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET details = ? WHERE name = ? AND (details IS NULL OR details = '' OR details = 0)", [value, name], commit)

	def update_rating_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET rating = ? WHERE name = ?", [value, name], commit)

	def update_empty_rating_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET rating = ? WHERE name = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, name], commit)

	def update_ignore_auto_tag_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET ignore_auto_tag = ? WHERE name = ?", [value, name], commit)

	def update_empty_ignore_auto_tag_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET ignore_auto_tag = ? WHERE name = ? AND (ignore_auto_tag IS NULL OR ignore_auto_tag = '' OR ignore_auto_tag = 0)", [value, name], commit)

	def update_image_blob_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET image_blob = ? WHERE name = ?", [value, name], commit)

	def update_empty_image_blob_by_name(self, name, value, commit=True):
		return self.execute("UPDATE studios SET image_blob = ? WHERE name = ? AND (image_blob IS NULL OR image_blob = '' OR image_blob = 0)", [value, name], commit)

	def update_url_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET url = ? WHERE parent_id = ?", [value, parent_id], commit)

	def update_empty_url_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET url = ? WHERE parent_id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, parent_id], commit)

	def update_created_at_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET created_at = ? WHERE parent_id = ?", [value, parent_id], commit)

	def update_empty_created_at_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET created_at = ? WHERE parent_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, parent_id], commit)

	def update_updated_at_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET updated_at = ? WHERE parent_id = ?", [value, parent_id], commit)

	def update_empty_updated_at_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET updated_at = ? WHERE parent_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, parent_id], commit)

	def update_details_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET details = ? WHERE parent_id = ?", [value, parent_id], commit)

	def update_empty_details_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET details = ? WHERE parent_id = ? AND (details IS NULL OR details = '' OR details = 0)", [value, parent_id], commit)

	def update_rating_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET rating = ? WHERE parent_id = ?", [value, parent_id], commit)

	def update_empty_rating_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET rating = ? WHERE parent_id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, parent_id], commit)

	def update_ignore_auto_tag_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET ignore_auto_tag = ? WHERE parent_id = ?", [value, parent_id], commit)

	def update_empty_ignore_auto_tag_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET ignore_auto_tag = ? WHERE parent_id = ? AND (ignore_auto_tag IS NULL OR ignore_auto_tag = '' OR ignore_auto_tag = 0)", [value, parent_id], commit)

	def update_image_blob_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET image_blob = ? WHERE parent_id = ?", [value, parent_id], commit)

	def update_empty_image_blob_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE studios SET image_blob = ? WHERE parent_id = ? AND (image_blob IS NULL OR image_blob = '' OR image_blob = 0)", [value, parent_id], commit)

class SavedFilters(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'saved_filters')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [SavedFiltersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
		return [SavedFiltersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_mode(self, mode, colvalues={}, selectcols=['*']):
		colvalues['mode'] = mode
		return [SavedFiltersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_find_filter(self, find_filter, colvalues={}, selectcols=['*']):
		colvalues['find_filter'] = find_filter
		return [SavedFiltersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_object_filter(self, object_filter, colvalues={}, selectcols=['*']):
		colvalues['object_filter'] = object_filter
		return [SavedFiltersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_ui_options(self, ui_options, colvalues={}, selectcols=['*']):
		colvalues['ui_options'] = ui_options
		return [SavedFiltersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return SavedFiltersRow().from_sqliterow(row)
		else:
			return None

	def selectone_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
		row = self.selectone(colvalues, selectcols)
		if row:
			return SavedFiltersRow().from_sqliterow(row)
		else:
			return None

	def selectone_mode(self, mode, colvalues={}, selectcols=['*']):
		colvalues['mode'] = mode
		row = self.selectone(colvalues, selectcols)
		if row:
			return SavedFiltersRow().from_sqliterow(row)
		else:
			return None

	def selectone_find_filter(self, find_filter, colvalues={}, selectcols=['*']):
		colvalues['find_filter'] = find_filter
		row = self.selectone(colvalues, selectcols)
		if row:
			return SavedFiltersRow().from_sqliterow(row)
		else:
			return None

	def selectone_object_filter(self, object_filter, colvalues={}, selectcols=['*']):
		colvalues['object_filter'] = object_filter
		row = self.selectone(colvalues, selectcols)
		if row:
			return SavedFiltersRow().from_sqliterow(row)
		else:
			return None

	def selectone_ui_options(self, ui_options, colvalues={}, selectcols=['*']):
		colvalues['ui_options'] = ui_options
		row = self.selectone(colvalues, selectcols)
		if row:
			return SavedFiltersRow().from_sqliterow(row)
		else:
			return None

	def insert(self, name, mode, find_filter, object_filter, ui_options, commit=True):
		return self.execute("INSERT INTO saved_filters (name, mode, find_filter, object_filter, ui_options) VALUES (?, ?, ?, ?, ?)", [name, mode, find_filter, object_filter, ui_options], commit)

	def insert_model(self, model: SavedFiltersRow, commit=True):
		return self.execute("INSERT INTO saved_filters (name, mode, find_filter, object_filter, ui_options) VALUES (?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_id(self, id, commit=True):
		return self.execute("DELETE FROM saved_filters WHERE id = ?", [id, ], commit)

	def delete_by_name(self, name, commit=True):
		return self.execute("DELETE FROM saved_filters WHERE name = ?", [name, ], commit)

	def update_mode_by_id(self, id, value, commit=True):
		return self.execute("UPDATE saved_filters SET mode = ? WHERE id = ?", [value, id], commit)

	def update_empty_mode_by_id(self, id, value, commit=True):
		return self.execute("UPDATE saved_filters SET mode = ? WHERE id = ? AND (mode IS NULL OR mode = '' OR mode = 0)", [value, id], commit)

	def update_find_filter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE saved_filters SET find_filter = ? WHERE id = ?", [value, id], commit)

	def update_empty_find_filter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE saved_filters SET find_filter = ? WHERE id = ? AND (find_filter IS NULL OR find_filter = '' OR find_filter = 0)", [value, id], commit)

	def update_object_filter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE saved_filters SET object_filter = ? WHERE id = ?", [value, id], commit)

	def update_empty_object_filter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE saved_filters SET object_filter = ? WHERE id = ? AND (object_filter IS NULL OR object_filter = '' OR object_filter = 0)", [value, id], commit)

	def update_ui_options_by_id(self, id, value, commit=True):
		return self.execute("UPDATE saved_filters SET ui_options = ? WHERE id = ?", [value, id], commit)

	def update_empty_ui_options_by_id(self, id, value, commit=True):
		return self.execute("UPDATE saved_filters SET ui_options = ? WHERE id = ? AND (ui_options IS NULL OR ui_options = '' OR ui_options = 0)", [value, id], commit)

	def update_mode_by_name(self, name, value, commit=True):
		return self.execute("UPDATE saved_filters SET mode = ? WHERE name = ?", [value, name], commit)

	def update_empty_mode_by_name(self, name, value, commit=True):
		return self.execute("UPDATE saved_filters SET mode = ? WHERE name = ? AND (mode IS NULL OR mode = '' OR mode = 0)", [value, name], commit)

	def update_find_filter_by_name(self, name, value, commit=True):
		return self.execute("UPDATE saved_filters SET find_filter = ? WHERE name = ?", [value, name], commit)

	def update_empty_find_filter_by_name(self, name, value, commit=True):
		return self.execute("UPDATE saved_filters SET find_filter = ? WHERE name = ? AND (find_filter IS NULL OR find_filter = '' OR find_filter = 0)", [value, name], commit)

	def update_object_filter_by_name(self, name, value, commit=True):
		return self.execute("UPDATE saved_filters SET object_filter = ? WHERE name = ?", [value, name], commit)

	def update_empty_object_filter_by_name(self, name, value, commit=True):
		return self.execute("UPDATE saved_filters SET object_filter = ? WHERE name = ? AND (object_filter IS NULL OR object_filter = '' OR object_filter = 0)", [value, name], commit)

	def update_ui_options_by_name(self, name, value, commit=True):
		return self.execute("UPDATE saved_filters SET ui_options = ? WHERE name = ?", [value, name], commit)

	def update_empty_ui_options_by_name(self, name, value, commit=True):
		return self.execute("UPDATE saved_filters SET ui_options = ? WHERE name = ? AND (ui_options IS NULL OR ui_options = '' OR ui_options = 0)", [value, name], commit)

class ImageUrls(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'image_urls')

	def select_image_id(self, image_id, colvalues={}, selectcols=['*']):
		colvalues['image_id'] = image_id
		return [ImageUrlsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_position(self, position, colvalues={}, selectcols=['*']):
		colvalues['position'] = position
		return [ImageUrlsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		return [ImageUrlsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_image_id(self, image_id, colvalues={}, selectcols=['*']):
		colvalues['image_id'] = image_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImageUrlsRow().from_sqliterow(row)
		else:
			return None

	def selectone_position(self, position, colvalues={}, selectcols=['*']):
		colvalues['position'] = position
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImageUrlsRow().from_sqliterow(row)
		else:
			return None

	def selectone_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImageUrlsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, image_id, position, url, commit=True):
		return self.execute("INSERT INTO image_urls (image_id, position, url) VALUES (?, ?, ?)", [image_id, position, url], commit)

	def insert_model(self, model: ImageUrlsRow, commit=True):
		return self.execute("INSERT INTO image_urls (image_id, position, url) VALUES (?, ?, ?)", model.values_list(False), commit)

	def delete_by_image_id(self, image_id, commit=True):
		return self.execute("DELETE FROM image_urls WHERE image_id = ?", [image_id, ], commit)

	def update_position_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE image_urls SET position = ? WHERE image_id = ?", [value, image_id], commit)

	def update_empty_position_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE image_urls SET position = ? WHERE image_id = ? AND (position IS NULL OR position = '' OR position = 0)", [value, image_id], commit)

	def update_url_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE image_urls SET url = ? WHERE image_id = ?", [value, image_id], commit)

	def update_empty_url_by_image_id(self, image_id, value, commit=True):
		return self.execute("UPDATE image_urls SET url = ? WHERE image_id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, image_id], commit)

class Images(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'images')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_o_counter(self, o_counter, colvalues={}, selectcols=['*']):
		colvalues['o_counter'] = o_counter
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_organized(self, organized, colvalues={}, selectcols=['*']):
		colvalues['organized'] = organized
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_date(self, date, colvalues={}, selectcols=['*']):
		colvalues['date'] = date
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_code(self, code, colvalues={}, selectcols=['*']):
		colvalues['code'] = code
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_photographer(self, photographer, colvalues={}, selectcols=['*']):
		colvalues['photographer'] = photographer
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_details(self, details, colvalues={}, selectcols=['*']):
		colvalues['details'] = details
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_o_counter(self, o_counter, colvalues={}, selectcols=['*']):
		colvalues['o_counter'] = o_counter
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_organized(self, organized, colvalues={}, selectcols=['*']):
		colvalues['organized'] = organized
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_date(self, date, colvalues={}, selectcols=['*']):
		colvalues['date'] = date
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_code(self, code, colvalues={}, selectcols=['*']):
		colvalues['code'] = code
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_photographer(self, photographer, colvalues={}, selectcols=['*']):
		colvalues['photographer'] = photographer
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_details(self, details, colvalues={}, selectcols=['*']):
		colvalues['details'] = details
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, title, rating, studio_id, o_counter, organized, created_at, updated_at, date, code, photographer, details, commit=True):
		return self.execute("INSERT INTO images (title, rating, studio_id, o_counter, organized, created_at, updated_at, date, code, photographer, details) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [title, rating, studio_id, o_counter, organized, created_at, updated_at, date, code, photographer, details], commit)

	def insert_model(self, model: ImagesRow, commit=True):
		return self.execute("INSERT INTO images (title, rating, studio_id, o_counter, organized, created_at, updated_at, date, code, photographer, details) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_id(self, id, commit=True):
		return self.execute("DELETE FROM images WHERE id = ?", [id, ], commit)

	def delete_by_studio_id(self, studio_id, commit=True):
		return self.execute("DELETE FROM images WHERE studio_id = ?", [studio_id, ], commit)

	def update_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET title = ? WHERE id = ?", [value, id], commit)

	def update_empty_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET title = ? WHERE id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, id], commit)

	def update_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET rating = ? WHERE id = ?", [value, id], commit)

	def update_empty_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET rating = ? WHERE id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, id], commit)

	def update_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET studio_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET studio_id = ? WHERE id = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, id], commit)

	def update_o_counter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET o_counter = ? WHERE id = ?", [value, id], commit)

	def update_empty_o_counter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET o_counter = ? WHERE id = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, id], commit)

	def update_organized_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET organized = ? WHERE id = ?", [value, id], commit)

	def update_empty_organized_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET organized = ? WHERE id = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET date = ? WHERE id = ?", [value, id], commit)

	def update_empty_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET date = ? WHERE id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, id], commit)

	def update_code_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET code = ? WHERE id = ?", [value, id], commit)

	def update_empty_code_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET code = ? WHERE id = ? AND (code IS NULL OR code = '' OR code = 0)", [value, id], commit)

	def update_photographer_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET photographer = ? WHERE id = ?", [value, id], commit)

	def update_empty_photographer_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET photographer = ? WHERE id = ? AND (photographer IS NULL OR photographer = '' OR photographer = 0)", [value, id], commit)

	def update_details_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET details = ? WHERE id = ?", [value, id], commit)

	def update_empty_details_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET details = ? WHERE id = ? AND (details IS NULL OR details = '' OR details = 0)", [value, id], commit)

	def update_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET title = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET title = ? WHERE studio_id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, studio_id], commit)

	def update_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET rating = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET rating = ? WHERE studio_id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, studio_id], commit)

	def update_o_counter_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET o_counter = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_o_counter_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET o_counter = ? WHERE studio_id = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, studio_id], commit)

	def update_organized_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET organized = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_organized_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET organized = ? WHERE studio_id = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, studio_id], commit)

	def update_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET created_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET created_at = ? WHERE studio_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, studio_id], commit)

	def update_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET updated_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET updated_at = ? WHERE studio_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, studio_id], commit)

	def update_date_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET date = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_date_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET date = ? WHERE studio_id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, studio_id], commit)

	def update_code_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET code = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_code_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET code = ? WHERE studio_id = ? AND (code IS NULL OR code = '' OR code = 0)", [value, studio_id], commit)

	def update_photographer_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET photographer = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_photographer_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET photographer = ? WHERE studio_id = ? AND (photographer IS NULL OR photographer = '' OR photographer = 0)", [value, studio_id], commit)

	def update_details_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET details = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_details_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET details = ? WHERE studio_id = ? AND (details IS NULL OR details = '' OR details = 0)", [value, studio_id], commit)

class GalleryUrls(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'gallery_urls')

	def select_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		return [GalleryUrlsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_position(self, position, colvalues={}, selectcols=['*']):
		colvalues['position'] = position
		return [GalleryUrlsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		return [GalleryUrlsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_gallery_id(self, gallery_id, colvalues={}, selectcols=['*']):
		colvalues['gallery_id'] = gallery_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleryUrlsRow().from_sqliterow(row)
		else:
			return None

	def selectone_position(self, position, colvalues={}, selectcols=['*']):
		colvalues['position'] = position
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleryUrlsRow().from_sqliterow(row)
		else:
			return None

	def selectone_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleryUrlsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, gallery_id, position, url, commit=True):
		return self.execute("INSERT INTO gallery_urls (gallery_id, position, url) VALUES (?, ?, ?)", [gallery_id, position, url], commit)

	def insert_model(self, model: GalleryUrlsRow, commit=True):
		return self.execute("INSERT INTO gallery_urls (gallery_id, position, url) VALUES (?, ?, ?)", model.values_list(False), commit)

	def delete_by_gallery_id(self, gallery_id, commit=True):
		return self.execute("DELETE FROM gallery_urls WHERE gallery_id = ?", [gallery_id, ], commit)

	def update_position_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE gallery_urls SET position = ? WHERE gallery_id = ?", [value, gallery_id], commit)

	def update_empty_position_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE gallery_urls SET position = ? WHERE gallery_id = ? AND (position IS NULL OR position = '' OR position = 0)", [value, gallery_id], commit)

	def update_url_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE gallery_urls SET url = ? WHERE gallery_id = ?", [value, gallery_id], commit)

	def update_empty_url_by_gallery_id(self, gallery_id, value, commit=True):
		return self.execute("UPDATE gallery_urls SET url = ? WHERE gallery_id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, gallery_id], commit)

class Galleries(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'galleries')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_folder_id(self, folder_id, colvalues={}, selectcols=['*']):
		colvalues['folder_id'] = folder_id
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_date(self, date, colvalues={}, selectcols=['*']):
		colvalues['date'] = date
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_details(self, details, colvalues={}, selectcols=['*']):
		colvalues['details'] = details
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_organized(self, organized, colvalues={}, selectcols=['*']):
		colvalues['organized'] = organized
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_code(self, code, colvalues={}, selectcols=['*']):
		colvalues['code'] = code
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_photographer(self, photographer, colvalues={}, selectcols=['*']):
		colvalues['photographer'] = photographer
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_folder_id(self, folder_id, colvalues={}, selectcols=['*']):
		colvalues['folder_id'] = folder_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_date(self, date, colvalues={}, selectcols=['*']):
		colvalues['date'] = date
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_details(self, details, colvalues={}, selectcols=['*']):
		colvalues['details'] = details
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_organized(self, organized, colvalues={}, selectcols=['*']):
		colvalues['organized'] = organized
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_code(self, code, colvalues={}, selectcols=['*']):
		colvalues['code'] = code
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_photographer(self, photographer, colvalues={}, selectcols=['*']):
		colvalues['photographer'] = photographer
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, folder_id, title, date, details, studio_id, rating, organized, created_at, updated_at, code, photographer, commit=True):
		return self.execute("INSERT INTO galleries (folder_id, title, date, details, studio_id, rating, organized, created_at, updated_at, code, photographer) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [folder_id, title, date, details, studio_id, rating, organized, created_at, updated_at, code, photographer], commit)

	def insert_model(self, model: GalleriesRow, commit=True):
		return self.execute("INSERT INTO galleries (folder_id, title, date, details, studio_id, rating, organized, created_at, updated_at, code, photographer) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def delete_by_id(self, id, commit=True):
		return self.execute("DELETE FROM galleries WHERE id = ?", [id, ], commit)

	def delete_by_folder_id(self, folder_id, commit=True):
		return self.execute("DELETE FROM galleries WHERE folder_id = ?", [folder_id, ], commit)

	def delete_by_studio_id(self, studio_id, commit=True):
		return self.execute("DELETE FROM galleries WHERE studio_id = ?", [studio_id, ], commit)

	def update_folder_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET folder_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_folder_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET folder_id = ? WHERE id = ? AND (folder_id IS NULL OR folder_id = '' OR folder_id = 0)", [value, id], commit)

	def update_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE id = ?", [value, id], commit)

	def update_empty_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, id], commit)

	def update_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET date = ? WHERE id = ?", [value, id], commit)

	def update_empty_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET date = ? WHERE id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, id], commit)

	def update_details_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET details = ? WHERE id = ?", [value, id], commit)

	def update_empty_details_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET details = ? WHERE id = ? AND (details IS NULL OR details = '' OR details = 0)", [value, id], commit)

	def update_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET studio_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET studio_id = ? WHERE id = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, id], commit)

	def update_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET rating = ? WHERE id = ?", [value, id], commit)

	def update_empty_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET rating = ? WHERE id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, id], commit)

	def update_organized_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET organized = ? WHERE id = ?", [value, id], commit)

	def update_empty_organized_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET organized = ? WHERE id = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_code_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET code = ? WHERE id = ?", [value, id], commit)

	def update_empty_code_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET code = ? WHERE id = ? AND (code IS NULL OR code = '' OR code = 0)", [value, id], commit)

	def update_photographer_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET photographer = ? WHERE id = ?", [value, id], commit)

	def update_empty_photographer_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET photographer = ? WHERE id = ? AND (photographer IS NULL OR photographer = '' OR photographer = 0)", [value, id], commit)

	def update_title_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE folder_id = ?", [value, folder_id], commit)

	def update_empty_title_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE folder_id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, folder_id], commit)

	def update_date_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET date = ? WHERE folder_id = ?", [value, folder_id], commit)

	def update_empty_date_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET date = ? WHERE folder_id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, folder_id], commit)

	def update_details_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET details = ? WHERE folder_id = ?", [value, folder_id], commit)

	def update_empty_details_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET details = ? WHERE folder_id = ? AND (details IS NULL OR details = '' OR details = 0)", [value, folder_id], commit)

	def update_studio_id_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET studio_id = ? WHERE folder_id = ?", [value, folder_id], commit)

	def update_empty_studio_id_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET studio_id = ? WHERE folder_id = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, folder_id], commit)

	def update_rating_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET rating = ? WHERE folder_id = ?", [value, folder_id], commit)

	def update_empty_rating_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET rating = ? WHERE folder_id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, folder_id], commit)

	def update_organized_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET organized = ? WHERE folder_id = ?", [value, folder_id], commit)

	def update_empty_organized_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET organized = ? WHERE folder_id = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, folder_id], commit)

	def update_created_at_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET created_at = ? WHERE folder_id = ?", [value, folder_id], commit)

	def update_empty_created_at_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET created_at = ? WHERE folder_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, folder_id], commit)

	def update_updated_at_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET updated_at = ? WHERE folder_id = ?", [value, folder_id], commit)

	def update_empty_updated_at_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET updated_at = ? WHERE folder_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, folder_id], commit)

	def update_code_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET code = ? WHERE folder_id = ?", [value, folder_id], commit)

	def update_empty_code_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET code = ? WHERE folder_id = ? AND (code IS NULL OR code = '' OR code = 0)", [value, folder_id], commit)

	def update_photographer_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET photographer = ? WHERE folder_id = ?", [value, folder_id], commit)

	def update_empty_photographer_by_folder_id(self, folder_id, value, commit=True):
		return self.execute("UPDATE galleries SET photographer = ? WHERE folder_id = ? AND (photographer IS NULL OR photographer = '' OR photographer = 0)", [value, folder_id], commit)

	def update_folder_id_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET folder_id = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_folder_id_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET folder_id = ? WHERE studio_id = ? AND (folder_id IS NULL OR folder_id = '' OR folder_id = 0)", [value, studio_id], commit)

	def update_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE studio_id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, studio_id], commit)

	def update_date_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET date = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_date_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET date = ? WHERE studio_id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, studio_id], commit)

	def update_details_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET details = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_details_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET details = ? WHERE studio_id = ? AND (details IS NULL OR details = '' OR details = 0)", [value, studio_id], commit)

	def update_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET rating = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET rating = ? WHERE studio_id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, studio_id], commit)

	def update_organized_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET organized = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_organized_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET organized = ? WHERE studio_id = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, studio_id], commit)

	def update_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET created_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET created_at = ? WHERE studio_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, studio_id], commit)

	def update_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET updated_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET updated_at = ? WHERE studio_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, studio_id], commit)

	def update_code_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET code = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_code_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET code = ? WHERE studio_id = ? AND (code IS NULL OR code = '' OR code = 0)", [value, studio_id], commit)

	def update_photographer_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET photographer = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_photographer_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET photographer = ? WHERE studio_id = ? AND (photographer IS NULL OR photographer = '' OR photographer = 0)", [value, studio_id], commit)

