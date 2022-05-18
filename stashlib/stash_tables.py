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

	def insert(self, name, created_at, updated_at, ignore_auto_tag, commit=True):
		return self.execute("INSERT INTO tags (name, created_at, updated_at, ignore_auto_tag) VALUES (?, ?, ?, ?)", [name, created_at, updated_at, ignore_auto_tag], commit)

	def insert_model(self, model: TagsRow, commit=True):
		return self.execute("INSERT INTO tags (name, created_at, updated_at, ignore_auto_tag) VALUES (?, ?, ?, ?)", model.values_list(False), commit)

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

	def update_seq_by_name(self, name, value, commit=True):
		return self.execute("UPDATE sqlite_sequence SET seq = ? WHERE name = ?", [value, name], commit)

	def update_empty_seq_by_name(self, name, value, commit=True):
		return self.execute("UPDATE sqlite_sequence SET seq = ? WHERE name = ? AND (seq IS NULL OR seq = '' OR seq = 0)", [value, name], commit)

class Studios(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'studios')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [StudiosRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
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

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosRow().from_sqliterow(row)
		else:
			return None

	def selectone_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
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

	def insert(self, checksum, name, url, parent_id, created_at, updated_at, details, rating, ignore_auto_tag, commit=True):
		return self.execute("INSERT INTO studios (checksum, name, url, parent_id, created_at, updated_at, details, rating, ignore_auto_tag) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", [checksum, name, url, parent_id, created_at, updated_at, details, rating, ignore_auto_tag], commit)

	def insert_model(self, model: StudiosRow, commit=True):
		return self.execute("INSERT INTO studios (checksum, name, url, parent_id, created_at, updated_at, details, rating, ignore_auto_tag) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

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

	def update_url_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET url = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_url_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET url = ? WHERE checksum = ? AND (url IS NULL OR url = '' OR url = 0)", [value, checksum], commit)

	def update_parent_id_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET parent_id = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_parent_id_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET parent_id = ? WHERE checksum = ? AND (parent_id IS NULL OR parent_id = '' OR parent_id = 0)", [value, checksum], commit)

	def update_created_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET created_at = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_created_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET created_at = ? WHERE checksum = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, checksum], commit)

	def update_updated_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET updated_at = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_updated_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET updated_at = ? WHERE checksum = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, checksum], commit)

	def update_details_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET details = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_details_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET details = ? WHERE checksum = ? AND (details IS NULL OR details = '' OR details = 0)", [value, checksum], commit)

	def update_rating_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET rating = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_rating_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET rating = ? WHERE checksum = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, checksum], commit)

	def update_ignore_auto_tag_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET ignore_auto_tag = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_ignore_auto_tag_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE studios SET ignore_auto_tag = ? WHERE checksum = ? AND (ignore_auto_tag IS NULL OR ignore_auto_tag = '' OR ignore_auto_tag = 0)", [value, checksum], commit)

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

class Performers(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'performers')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
		return [PerformersRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_name(self, name, colvalues={}, selectcols=['*']):
		colvalues['name'] = name
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

	def select_aliases(self, aliases, colvalues={}, selectcols=['*']):
		colvalues['aliases'] = aliases
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

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersRow().from_sqliterow(row)
		else:
			return None

	def selectone_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
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

	def selectone_aliases(self, aliases, colvalues={}, selectcols=['*']):
		colvalues['aliases'] = aliases
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

	def insert(self, checksum, name, gender, url, twitter, instagram, birthdate, ethnicity, country, eye_color, height, measurements, fake_tits, career_length, tattoos, piercings, aliases, favorite, created_at, updated_at, details, death_date, hair_color, weight, rating, ignore_auto_tag, commit=True):
		return self.execute("INSERT INTO performers (checksum, name, gender, url, twitter, instagram, birthdate, ethnicity, country, eye_color, height, measurements, fake_tits, career_length, tattoos, piercings, aliases, favorite, created_at, updated_at, details, death_date, hair_color, weight, rating, ignore_auto_tag) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [checksum, name, gender, url, twitter, instagram, birthdate, ethnicity, country, eye_color, height, measurements, fake_tits, career_length, tattoos, piercings, aliases, favorite, created_at, updated_at, details, death_date, hair_color, weight, rating, ignore_auto_tag], commit)

	def insert_model(self, model: PerformersRow, commit=True):
		return self.execute("INSERT INTO performers (checksum, name, gender, url, twitter, instagram, birthdate, ethnicity, country, eye_color, height, measurements, fake_tits, career_length, tattoos, piercings, aliases, favorite, created_at, updated_at, details, death_date, hair_color, weight, rating, ignore_auto_tag) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

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

	def update_aliases_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET aliases = ? WHERE id = ?", [value, id], commit)

	def update_empty_aliases_by_id(self, id, value, commit=True):
		return self.execute("UPDATE performers SET aliases = ? WHERE id = ? AND (aliases IS NULL OR aliases = '' OR aliases = 0)", [value, id], commit)

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

	def update_gender_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET gender = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_gender_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET gender = ? WHERE checksum = ? AND (gender IS NULL OR gender = '' OR gender = 0)", [value, checksum], commit)

	def update_url_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET url = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_url_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET url = ? WHERE checksum = ? AND (url IS NULL OR url = '' OR url = 0)", [value, checksum], commit)

	def update_twitter_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET twitter = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_twitter_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET twitter = ? WHERE checksum = ? AND (twitter IS NULL OR twitter = '' OR twitter = 0)", [value, checksum], commit)

	def update_instagram_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET instagram = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_instagram_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET instagram = ? WHERE checksum = ? AND (instagram IS NULL OR instagram = '' OR instagram = 0)", [value, checksum], commit)

	def update_birthdate_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET birthdate = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_birthdate_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET birthdate = ? WHERE checksum = ? AND (birthdate IS NULL OR birthdate = '' OR birthdate = 0)", [value, checksum], commit)

	def update_ethnicity_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET ethnicity = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_ethnicity_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET ethnicity = ? WHERE checksum = ? AND (ethnicity IS NULL OR ethnicity = '' OR ethnicity = 0)", [value, checksum], commit)

	def update_country_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET country = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_country_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET country = ? WHERE checksum = ? AND (country IS NULL OR country = '' OR country = 0)", [value, checksum], commit)

	def update_eye_color_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET eye_color = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_eye_color_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET eye_color = ? WHERE checksum = ? AND (eye_color IS NULL OR eye_color = '' OR eye_color = 0)", [value, checksum], commit)

	def update_height_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET height = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_height_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET height = ? WHERE checksum = ? AND (height IS NULL OR height = '' OR height = 0)", [value, checksum], commit)

	def update_measurements_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET measurements = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_measurements_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET measurements = ? WHERE checksum = ? AND (measurements IS NULL OR measurements = '' OR measurements = 0)", [value, checksum], commit)

	def update_fake_tits_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET fake_tits = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_fake_tits_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET fake_tits = ? WHERE checksum = ? AND (fake_tits IS NULL OR fake_tits = '' OR fake_tits = 0)", [value, checksum], commit)

	def update_career_length_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET career_length = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_career_length_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET career_length = ? WHERE checksum = ? AND (career_length IS NULL OR career_length = '' OR career_length = 0)", [value, checksum], commit)

	def update_tattoos_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET tattoos = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_tattoos_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET tattoos = ? WHERE checksum = ? AND (tattoos IS NULL OR tattoos = '' OR tattoos = 0)", [value, checksum], commit)

	def update_piercings_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET piercings = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_piercings_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET piercings = ? WHERE checksum = ? AND (piercings IS NULL OR piercings = '' OR piercings = 0)", [value, checksum], commit)

	def update_aliases_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET aliases = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_aliases_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET aliases = ? WHERE checksum = ? AND (aliases IS NULL OR aliases = '' OR aliases = 0)", [value, checksum], commit)

	def update_favorite_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET favorite = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_favorite_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET favorite = ? WHERE checksum = ? AND (favorite IS NULL OR favorite = '' OR favorite = 0)", [value, checksum], commit)

	def update_created_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET created_at = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_created_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET created_at = ? WHERE checksum = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, checksum], commit)

	def update_updated_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET updated_at = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_updated_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET updated_at = ? WHERE checksum = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, checksum], commit)

	def update_details_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET details = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_details_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET details = ? WHERE checksum = ? AND (details IS NULL OR details = '' OR details = 0)", [value, checksum], commit)

	def update_death_date_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET death_date = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_death_date_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET death_date = ? WHERE checksum = ? AND (death_date IS NULL OR death_date = '' OR death_date = 0)", [value, checksum], commit)

	def update_hair_color_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET hair_color = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_hair_color_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET hair_color = ? WHERE checksum = ? AND (hair_color IS NULL OR hair_color = '' OR hair_color = 0)", [value, checksum], commit)

	def update_weight_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET weight = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_weight_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET weight = ? WHERE checksum = ? AND (weight IS NULL OR weight = '' OR weight = 0)", [value, checksum], commit)

	def update_rating_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET rating = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_rating_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET rating = ? WHERE checksum = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, checksum], commit)

	def update_ignore_auto_tag_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET ignore_auto_tag = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_ignore_auto_tag_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE performers SET ignore_auto_tag = ? WHERE checksum = ? AND (ignore_auto_tag IS NULL OR ignore_auto_tag = '' OR ignore_auto_tag = 0)", [value, checksum], commit)

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

	def update_aliases_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET aliases = ? WHERE name = ?", [value, name], commit)

	def update_empty_aliases_by_name(self, name, value, commit=True):
		return self.execute("UPDATE performers SET aliases = ? WHERE name = ? AND (aliases IS NULL OR aliases = '' OR aliases = 0)", [value, name], commit)

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

	def select_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
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

	def selectone_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
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

	def insert(self, name, aliases, duration, date, rating, studio_id, director, synopsis, checksum, url, created_at, updated_at, commit=True):
		return self.execute("INSERT INTO movies (name, aliases, duration, date, rating, studio_id, director, synopsis, checksum, url, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [name, aliases, duration, date, rating, studio_id, director, synopsis, checksum, url, created_at, updated_at], commit)

	def insert_model(self, model: MoviesRow, commit=True):
		return self.execute("INSERT INTO movies (name, aliases, duration, date, rating, studio_id, director, synopsis, checksum, url, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

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

	def update_aliases_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET aliases = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_aliases_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET aliases = ? WHERE checksum = ? AND (aliases IS NULL OR aliases = '' OR aliases = 0)", [value, checksum], commit)

	def update_duration_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET duration = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_duration_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET duration = ? WHERE checksum = ? AND (duration IS NULL OR duration = '' OR duration = 0)", [value, checksum], commit)

	def update_date_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET date = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_date_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET date = ? WHERE checksum = ? AND (date IS NULL OR date = '' OR date = 0)", [value, checksum], commit)

	def update_rating_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET rating = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_rating_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET rating = ? WHERE checksum = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, checksum], commit)

	def update_studio_id_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET studio_id = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_studio_id_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET studio_id = ? WHERE checksum = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, checksum], commit)

	def update_director_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET director = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_director_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET director = ? WHERE checksum = ? AND (director IS NULL OR director = '' OR director = 0)", [value, checksum], commit)

	def update_synopsis_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET synopsis = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_synopsis_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET synopsis = ? WHERE checksum = ? AND (synopsis IS NULL OR synopsis = '' OR synopsis = 0)", [value, checksum], commit)

	def update_url_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET url = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_url_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET url = ? WHERE checksum = ? AND (url IS NULL OR url = '' OR url = 0)", [value, checksum], commit)

	def update_created_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET created_at = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_created_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET created_at = ? WHERE checksum = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, checksum], commit)

	def update_updated_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET updated_at = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_updated_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE movies SET updated_at = ? WHERE checksum = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, checksum], commit)

class ScrapedItems(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'scraped_items')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_description(self, description, colvalues={}, selectcols=['*']):
		colvalues['description'] = description
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_date(self, date, colvalues={}, selectcols=['*']):
		colvalues['date'] = date
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_tags(self, tags, colvalues={}, selectcols=['*']):
		colvalues['tags'] = tags
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_models(self, models, colvalues={}, selectcols=['*']):
		colvalues['models'] = models
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_episode(self, episode, colvalues={}, selectcols=['*']):
		colvalues['episode'] = episode
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_gallery_filename(self, gallery_filename, colvalues={}, selectcols=['*']):
		colvalues['gallery_filename'] = gallery_filename
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_gallery_url(self, gallery_url, colvalues={}, selectcols=['*']):
		colvalues['gallery_url'] = gallery_url
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_video_filename(self, video_filename, colvalues={}, selectcols=['*']):
		colvalues['video_filename'] = video_filename
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_video_url(self, video_url, colvalues={}, selectcols=['*']):
		colvalues['video_url'] = video_url
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [ScrapedItemsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_description(self, description, colvalues={}, selectcols=['*']):
		colvalues['description'] = description
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_date(self, date, colvalues={}, selectcols=['*']):
		colvalues['date'] = date
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_tags(self, tags, colvalues={}, selectcols=['*']):
		colvalues['tags'] = tags
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_models(self, models, colvalues={}, selectcols=['*']):
		colvalues['models'] = models
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_episode(self, episode, colvalues={}, selectcols=['*']):
		colvalues['episode'] = episode
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_gallery_filename(self, gallery_filename, colvalues={}, selectcols=['*']):
		colvalues['gallery_filename'] = gallery_filename
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_gallery_url(self, gallery_url, colvalues={}, selectcols=['*']):
		colvalues['gallery_url'] = gallery_url
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_video_filename(self, video_filename, colvalues={}, selectcols=['*']):
		colvalues['video_filename'] = video_filename
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_video_url(self, video_url, colvalues={}, selectcols=['*']):
		colvalues['video_url'] = video_url
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def selectone_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScrapedItemsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, title, description, url, date, rating, tags, models, episode, gallery_filename, gallery_url, video_filename, video_url, studio_id, created_at, updated_at, commit=True):
		return self.execute("INSERT INTO scraped_items (title, description, url, date, rating, tags, models, episode, gallery_filename, gallery_url, video_filename, video_url, studio_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [title, description, url, date, rating, tags, models, episode, gallery_filename, gallery_url, video_filename, video_url, studio_id, created_at, updated_at], commit)

	def insert_model(self, model: ScrapedItemsRow, commit=True):
		return self.execute("INSERT INTO scraped_items (title, description, url, date, rating, tags, models, episode, gallery_filename, gallery_url, video_filename, video_url, studio_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def update_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET title = ? WHERE id = ?", [value, id], commit)

	def update_empty_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET title = ? WHERE id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, id], commit)

	def update_description_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET description = ? WHERE id = ?", [value, id], commit)

	def update_empty_description_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET description = ? WHERE id = ? AND (description IS NULL OR description = '' OR description = 0)", [value, id], commit)

	def update_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET url = ? WHERE id = ?", [value, id], commit)

	def update_empty_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET url = ? WHERE id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, id], commit)

	def update_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET date = ? WHERE id = ?", [value, id], commit)

	def update_empty_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET date = ? WHERE id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, id], commit)

	def update_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET rating = ? WHERE id = ?", [value, id], commit)

	def update_empty_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET rating = ? WHERE id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, id], commit)

	def update_tags_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET tags = ? WHERE id = ?", [value, id], commit)

	def update_empty_tags_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET tags = ? WHERE id = ? AND (tags IS NULL OR tags = '' OR tags = 0)", [value, id], commit)

	def update_models_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET models = ? WHERE id = ?", [value, id], commit)

	def update_empty_models_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET models = ? WHERE id = ? AND (models IS NULL OR models = '' OR models = 0)", [value, id], commit)

	def update_episode_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET episode = ? WHERE id = ?", [value, id], commit)

	def update_empty_episode_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET episode = ? WHERE id = ? AND (episode IS NULL OR episode = '' OR episode = 0)", [value, id], commit)

	def update_gallery_filename_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET gallery_filename = ? WHERE id = ?", [value, id], commit)

	def update_empty_gallery_filename_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET gallery_filename = ? WHERE id = ? AND (gallery_filename IS NULL OR gallery_filename = '' OR gallery_filename = 0)", [value, id], commit)

	def update_gallery_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET gallery_url = ? WHERE id = ?", [value, id], commit)

	def update_empty_gallery_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET gallery_url = ? WHERE id = ? AND (gallery_url IS NULL OR gallery_url = '' OR gallery_url = 0)", [value, id], commit)

	def update_video_filename_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET video_filename = ? WHERE id = ?", [value, id], commit)

	def update_empty_video_filename_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET video_filename = ? WHERE id = ? AND (video_filename IS NULL OR video_filename = '' OR video_filename = 0)", [value, id], commit)

	def update_video_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET video_url = ? WHERE id = ?", [value, id], commit)

	def update_empty_video_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET video_url = ? WHERE id = ? AND (video_url IS NULL OR video_url = '' OR video_url = 0)", [value, id], commit)

	def update_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET studio_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET studio_id = ? WHERE id = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scraped_items SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET title = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET title = ? WHERE studio_id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, studio_id], commit)

	def update_description_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET description = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_description_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET description = ? WHERE studio_id = ? AND (description IS NULL OR description = '' OR description = 0)", [value, studio_id], commit)

	def update_url_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET url = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_url_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET url = ? WHERE studio_id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, studio_id], commit)

	def update_date_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET date = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_date_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET date = ? WHERE studio_id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, studio_id], commit)

	def update_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET rating = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET rating = ? WHERE studio_id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, studio_id], commit)

	def update_tags_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET tags = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_tags_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET tags = ? WHERE studio_id = ? AND (tags IS NULL OR tags = '' OR tags = 0)", [value, studio_id], commit)

	def update_models_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET models = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_models_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET models = ? WHERE studio_id = ? AND (models IS NULL OR models = '' OR models = 0)", [value, studio_id], commit)

	def update_episode_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET episode = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_episode_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET episode = ? WHERE studio_id = ? AND (episode IS NULL OR episode = '' OR episode = 0)", [value, studio_id], commit)

	def update_gallery_filename_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET gallery_filename = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_gallery_filename_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET gallery_filename = ? WHERE studio_id = ? AND (gallery_filename IS NULL OR gallery_filename = '' OR gallery_filename = 0)", [value, studio_id], commit)

	def update_gallery_url_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET gallery_url = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_gallery_url_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET gallery_url = ? WHERE studio_id = ? AND (gallery_url IS NULL OR gallery_url = '' OR gallery_url = 0)", [value, studio_id], commit)

	def update_video_filename_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET video_filename = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_video_filename_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET video_filename = ? WHERE studio_id = ? AND (video_filename IS NULL OR video_filename = '' OR video_filename = 0)", [value, studio_id], commit)

	def update_video_url_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET video_url = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_video_url_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET video_url = ? WHERE studio_id = ? AND (video_url IS NULL OR video_url = '' OR video_url = 0)", [value, studio_id], commit)

	def update_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET created_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET created_at = ? WHERE studio_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, studio_id], commit)

	def update_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET updated_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scraped_items SET updated_at = ? WHERE studio_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, studio_id], commit)

class PerformersImage(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'performers_image')

	def select_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		return [PerformersImageRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_image(self, image, colvalues={}, selectcols=['*']):
		colvalues['image'] = image
		return [PerformersImageRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_performer_id(self, performer_id, colvalues={}, selectcols=['*']):
		colvalues['performer_id'] = performer_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersImageRow().from_sqliterow(row)
		else:
			return None

	def selectone_image(self, image, colvalues={}, selectcols=['*']):
		colvalues['image'] = image
		row = self.selectone(colvalues, selectcols)
		if row:
			return PerformersImageRow().from_sqliterow(row)
		else:
			return None

	def insert(self, performer_id, image, commit=True):
		return self.execute("INSERT INTO performers_image (performer_id, image) VALUES (?, ?)", [performer_id, image], commit)

	def insert_model(self, model: PerformersImageRow, commit=True):
		return self.execute("INSERT INTO performers_image (performer_id, image) VALUES (?, ?)", model.values_list(False), commit)

	def update_image_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performers_image SET image = ? WHERE performer_id = ?", [value, performer_id], commit)

	def update_empty_image_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performers_image SET image = ? WHERE performer_id = ? AND (image IS NULL OR image = '' OR image = 0)", [value, performer_id], commit)

class StudiosImage(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'studios_image')

	def select_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		return [StudiosImageRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_image(self, image, colvalues={}, selectcols=['*']):
		colvalues['image'] = image
		return [StudiosImageRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosImageRow().from_sqliterow(row)
		else:
			return None

	def selectone_image(self, image, colvalues={}, selectcols=['*']):
		colvalues['image'] = image
		row = self.selectone(colvalues, selectcols)
		if row:
			return StudiosImageRow().from_sqliterow(row)
		else:
			return None

	def insert(self, studio_id, image, commit=True):
		return self.execute("INSERT INTO studios_image (studio_id, image) VALUES (?, ?)", [studio_id, image], commit)

	def insert_model(self, model: StudiosImageRow, commit=True):
		return self.execute("INSERT INTO studios_image (studio_id, image) VALUES (?, ?)", model.values_list(False), commit)

	def update_image_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE studios_image SET image = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_image_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE studios_image SET image = ? WHERE studio_id = ? AND (image IS NULL OR image = '' OR image = 0)", [value, studio_id], commit)

class MoviesImages(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'movies_images')

	def select_movie_id(self, movie_id, colvalues={}, selectcols=['*']):
		colvalues['movie_id'] = movie_id
		return [MoviesImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_front_image(self, front_image, colvalues={}, selectcols=['*']):
		colvalues['front_image'] = front_image
		return [MoviesImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_back_image(self, back_image, colvalues={}, selectcols=['*']):
		colvalues['back_image'] = back_image
		return [MoviesImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_movie_id(self, movie_id, colvalues={}, selectcols=['*']):
		colvalues['movie_id'] = movie_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_front_image(self, front_image, colvalues={}, selectcols=['*']):
		colvalues['front_image'] = front_image
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_back_image(self, back_image, colvalues={}, selectcols=['*']):
		colvalues['back_image'] = back_image
		row = self.selectone(colvalues, selectcols)
		if row:
			return MoviesImagesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, movie_id, front_image, back_image, commit=True):
		return self.execute("INSERT INTO movies_images (movie_id, front_image, back_image) VALUES (?, ?, ?)", [movie_id, front_image, back_image], commit)

	def insert_model(self, model: MoviesImagesRow, commit=True):
		return self.execute("INSERT INTO movies_images (movie_id, front_image, back_image) VALUES (?, ?, ?)", model.values_list(False), commit)

	def update_front_image_by_movie_id(self, movie_id, value, commit=True):
		return self.execute("UPDATE movies_images SET front_image = ? WHERE movie_id = ?", [value, movie_id], commit)

	def update_empty_front_image_by_movie_id(self, movie_id, value, commit=True):
		return self.execute("UPDATE movies_images SET front_image = ? WHERE movie_id = ? AND (front_image IS NULL OR front_image = '' OR front_image = 0)", [value, movie_id], commit)

	def update_back_image_by_movie_id(self, movie_id, value, commit=True):
		return self.execute("UPDATE movies_images SET back_image = ? WHERE movie_id = ?", [value, movie_id], commit)

	def update_empty_back_image_by_movie_id(self, movie_id, value, commit=True):
		return self.execute("UPDATE movies_images SET back_image = ? WHERE movie_id = ? AND (back_image IS NULL OR back_image = '' OR back_image = 0)", [value, movie_id], commit)

class TagsImage(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'tags_image')

	def select_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		return [TagsImageRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_image(self, image, colvalues={}, selectcols=['*']):
		colvalues['image'] = image
		return [TagsImageRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_tag_id(self, tag_id, colvalues={}, selectcols=['*']):
		colvalues['tag_id'] = tag_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagsImageRow().from_sqliterow(row)
		else:
			return None

	def selectone_image(self, image, colvalues={}, selectcols=['*']):
		colvalues['image'] = image
		row = self.selectone(colvalues, selectcols)
		if row:
			return TagsImageRow().from_sqliterow(row)
		else:
			return None

	def insert(self, tag_id, image, commit=True):
		return self.execute("INSERT INTO tags_image (tag_id, image) VALUES (?, ?)", [tag_id, image], commit)

	def insert_model(self, model: TagsImageRow, commit=True):
		return self.execute("INSERT INTO tags_image (tag_id, image) VALUES (?, ?)", model.values_list(False), commit)

	def update_image_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE tags_image SET image = ? WHERE tag_id = ?", [value, tag_id], commit)

	def update_empty_image_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE tags_image SET image = ? WHERE tag_id = ? AND (image IS NULL OR image = '' OR image = 0)", [value, tag_id], commit)

class Scenes(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'scenes')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_path(self, path, colvalues={}, selectcols=['*']):
		colvalues['path'] = path
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_oshash(self, oshash, colvalues={}, selectcols=['*']):
		colvalues['oshash'] = oshash
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_details(self, details, colvalues={}, selectcols=['*']):
		colvalues['details'] = details
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_date(self, date, colvalues={}, selectcols=['*']):
		colvalues['date'] = date
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_size(self, size, colvalues={}, selectcols=['*']):
		colvalues['size'] = size
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_duration(self, duration, colvalues={}, selectcols=['*']):
		colvalues['duration'] = duration
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_video_codec(self, video_codec, colvalues={}, selectcols=['*']):
		colvalues['video_codec'] = video_codec
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_audio_codec(self, audio_codec, colvalues={}, selectcols=['*']):
		colvalues['audio_codec'] = audio_codec
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_width(self, width, colvalues={}, selectcols=['*']):
		colvalues['width'] = width
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_height(self, height, colvalues={}, selectcols=['*']):
		colvalues['height'] = height
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_framerate(self, framerate, colvalues={}, selectcols=['*']):
		colvalues['framerate'] = framerate
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_bitrate(self, bitrate, colvalues={}, selectcols=['*']):
		colvalues['bitrate'] = bitrate
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_o_counter(self, o_counter, colvalues={}, selectcols=['*']):
		colvalues['o_counter'] = o_counter
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_format(self, format, colvalues={}, selectcols=['*']):
		colvalues['format'] = format
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_file_mod_time(self, file_mod_time, colvalues={}, selectcols=['*']):
		colvalues['file_mod_time'] = file_mod_time
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_organized(self, organized, colvalues={}, selectcols=['*']):
		colvalues['organized'] = organized
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_phash(self, phash, colvalues={}, selectcols=['*']):
		colvalues['phash'] = phash
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_interactive(self, interactive, colvalues={}, selectcols=['*']):
		colvalues['interactive'] = interactive
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_interactive_speed(self, interactive_speed, colvalues={}, selectcols=['*']):
		colvalues['interactive_speed'] = interactive_speed
		return [ScenesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_path(self, path, colvalues={}, selectcols=['*']):
		colvalues['path'] = path
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_oshash(self, oshash, colvalues={}, selectcols=['*']):
		colvalues['oshash'] = oshash
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

	def selectone_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
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

	def selectone_size(self, size, colvalues={}, selectcols=['*']):
		colvalues['size'] = size
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_duration(self, duration, colvalues={}, selectcols=['*']):
		colvalues['duration'] = duration
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_video_codec(self, video_codec, colvalues={}, selectcols=['*']):
		colvalues['video_codec'] = video_codec
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_audio_codec(self, audio_codec, colvalues={}, selectcols=['*']):
		colvalues['audio_codec'] = audio_codec
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_width(self, width, colvalues={}, selectcols=['*']):
		colvalues['width'] = width
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_height(self, height, colvalues={}, selectcols=['*']):
		colvalues['height'] = height
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_framerate(self, framerate, colvalues={}, selectcols=['*']):
		colvalues['framerate'] = framerate
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_bitrate(self, bitrate, colvalues={}, selectcols=['*']):
		colvalues['bitrate'] = bitrate
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

	def selectone_format(self, format, colvalues={}, selectcols=['*']):
		colvalues['format'] = format
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

	def selectone_file_mod_time(self, file_mod_time, colvalues={}, selectcols=['*']):
		colvalues['file_mod_time'] = file_mod_time
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

	def selectone_phash(self, phash, colvalues={}, selectcols=['*']):
		colvalues['phash'] = phash
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_interactive(self, interactive, colvalues={}, selectcols=['*']):
		colvalues['interactive'] = interactive
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def selectone_interactive_speed(self, interactive_speed, colvalues={}, selectcols=['*']):
		colvalues['interactive_speed'] = interactive_speed
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesRow().from_sqliterow(row)
		else:
			return None

	def insert(self, path, checksum, oshash, title, details, url, date, rating, size, duration, video_codec, audio_codec, width, height, framerate, bitrate, studio_id, o_counter, format, created_at, updated_at, file_mod_time, organized, phash, interactive, interactive_speed, commit=True):
		return self.execute("INSERT INTO scenes (path, checksum, oshash, title, details, url, date, rating, size, duration, video_codec, audio_codec, width, height, framerate, bitrate, studio_id, o_counter, format, created_at, updated_at, file_mod_time, organized, phash, interactive, interactive_speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [path, checksum, oshash, title, details, url, date, rating, size, duration, video_codec, audio_codec, width, height, framerate, bitrate, studio_id, o_counter, format, created_at, updated_at, file_mod_time, organized, phash, interactive, interactive_speed], commit)

	def insert_model(self, model: ScenesRow, commit=True):
		return self.execute("INSERT INTO scenes (path, checksum, oshash, title, details, url, date, rating, size, duration, video_codec, audio_codec, width, height, framerate, bitrate, studio_id, o_counter, format, created_at, updated_at, file_mod_time, organized, phash, interactive, interactive_speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def update_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE id = ?", [value, id], commit)

	def update_empty_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, id], commit)

	def update_details_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE id = ?", [value, id], commit)

	def update_empty_details_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE id = ? AND (details IS NULL OR details = '' OR details = 0)", [value, id], commit)

	def update_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET url = ? WHERE id = ?", [value, id], commit)

	def update_empty_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET url = ? WHERE id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, id], commit)

	def update_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE id = ?", [value, id], commit)

	def update_empty_date_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, id], commit)

	def update_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE id = ?", [value, id], commit)

	def update_empty_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, id], commit)

	def update_size_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET size = ? WHERE id = ?", [value, id], commit)

	def update_empty_size_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET size = ? WHERE id = ? AND (size IS NULL OR size = '' OR size = 0)", [value, id], commit)

	def update_duration_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET duration = ? WHERE id = ?", [value, id], commit)

	def update_empty_duration_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET duration = ? WHERE id = ? AND (duration IS NULL OR duration = '' OR duration = 0)", [value, id], commit)

	def update_video_codec_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET video_codec = ? WHERE id = ?", [value, id], commit)

	def update_empty_video_codec_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET video_codec = ? WHERE id = ? AND (video_codec IS NULL OR video_codec = '' OR video_codec = 0)", [value, id], commit)

	def update_audio_codec_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET audio_codec = ? WHERE id = ?", [value, id], commit)

	def update_empty_audio_codec_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET audio_codec = ? WHERE id = ? AND (audio_codec IS NULL OR audio_codec = '' OR audio_codec = 0)", [value, id], commit)

	def update_width_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET width = ? WHERE id = ?", [value, id], commit)

	def update_empty_width_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET width = ? WHERE id = ? AND (width IS NULL OR width = '' OR width = 0)", [value, id], commit)

	def update_height_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET height = ? WHERE id = ?", [value, id], commit)

	def update_empty_height_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET height = ? WHERE id = ? AND (height IS NULL OR height = '' OR height = 0)", [value, id], commit)

	def update_framerate_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET framerate = ? WHERE id = ?", [value, id], commit)

	def update_empty_framerate_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET framerate = ? WHERE id = ? AND (framerate IS NULL OR framerate = '' OR framerate = 0)", [value, id], commit)

	def update_bitrate_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET bitrate = ? WHERE id = ?", [value, id], commit)

	def update_empty_bitrate_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET bitrate = ? WHERE id = ? AND (bitrate IS NULL OR bitrate = '' OR bitrate = 0)", [value, id], commit)

	def update_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET studio_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET studio_id = ? WHERE id = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, id], commit)

	def update_o_counter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE id = ?", [value, id], commit)

	def update_empty_o_counter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE id = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, id], commit)

	def update_format_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET format = ? WHERE id = ?", [value, id], commit)

	def update_empty_format_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET format = ? WHERE id = ? AND (format IS NULL OR format = '' OR format = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_file_mod_time_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET file_mod_time = ? WHERE id = ?", [value, id], commit)

	def update_empty_file_mod_time_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET file_mod_time = ? WHERE id = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, id], commit)

	def update_organized_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE id = ?", [value, id], commit)

	def update_empty_organized_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE id = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, id], commit)

	def update_phash_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET phash = ? WHERE id = ?", [value, id], commit)

	def update_empty_phash_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET phash = ? WHERE id = ? AND (phash IS NULL OR phash = '' OR phash = 0)", [value, id], commit)

	def update_interactive_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET interactive = ? WHERE id = ?", [value, id], commit)

	def update_empty_interactive_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET interactive = ? WHERE id = ? AND (interactive IS NULL OR interactive = '' OR interactive = 0)", [value, id], commit)

	def update_interactive_speed_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET interactive_speed = ? WHERE id = ?", [value, id], commit)

	def update_empty_interactive_speed_by_id(self, id, value, commit=True):
		return self.execute("UPDATE scenes SET interactive_speed = ? WHERE id = ? AND (interactive_speed IS NULL OR interactive_speed = '' OR interactive_speed = 0)", [value, id], commit)

	def update_title_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE path = ?", [value, path], commit)

	def update_empty_title_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE path = ? AND (title IS NULL OR title = '' OR title = 0)", [value, path], commit)

	def update_details_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE path = ?", [value, path], commit)

	def update_empty_details_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE path = ? AND (details IS NULL OR details = '' OR details = 0)", [value, path], commit)

	def update_url_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET url = ? WHERE path = ?", [value, path], commit)

	def update_empty_url_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET url = ? WHERE path = ? AND (url IS NULL OR url = '' OR url = 0)", [value, path], commit)

	def update_date_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE path = ?", [value, path], commit)

	def update_empty_date_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE path = ? AND (date IS NULL OR date = '' OR date = 0)", [value, path], commit)

	def update_rating_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE path = ?", [value, path], commit)

	def update_empty_rating_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE path = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, path], commit)

	def update_size_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET size = ? WHERE path = ?", [value, path], commit)

	def update_empty_size_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET size = ? WHERE path = ? AND (size IS NULL OR size = '' OR size = 0)", [value, path], commit)

	def update_duration_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET duration = ? WHERE path = ?", [value, path], commit)

	def update_empty_duration_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET duration = ? WHERE path = ? AND (duration IS NULL OR duration = '' OR duration = 0)", [value, path], commit)

	def update_video_codec_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET video_codec = ? WHERE path = ?", [value, path], commit)

	def update_empty_video_codec_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET video_codec = ? WHERE path = ? AND (video_codec IS NULL OR video_codec = '' OR video_codec = 0)", [value, path], commit)

	def update_audio_codec_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET audio_codec = ? WHERE path = ?", [value, path], commit)

	def update_empty_audio_codec_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET audio_codec = ? WHERE path = ? AND (audio_codec IS NULL OR audio_codec = '' OR audio_codec = 0)", [value, path], commit)

	def update_width_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET width = ? WHERE path = ?", [value, path], commit)

	def update_empty_width_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET width = ? WHERE path = ? AND (width IS NULL OR width = '' OR width = 0)", [value, path], commit)

	def update_height_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET height = ? WHERE path = ?", [value, path], commit)

	def update_empty_height_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET height = ? WHERE path = ? AND (height IS NULL OR height = '' OR height = 0)", [value, path], commit)

	def update_framerate_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET framerate = ? WHERE path = ?", [value, path], commit)

	def update_empty_framerate_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET framerate = ? WHERE path = ? AND (framerate IS NULL OR framerate = '' OR framerate = 0)", [value, path], commit)

	def update_bitrate_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET bitrate = ? WHERE path = ?", [value, path], commit)

	def update_empty_bitrate_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET bitrate = ? WHERE path = ? AND (bitrate IS NULL OR bitrate = '' OR bitrate = 0)", [value, path], commit)

	def update_studio_id_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET studio_id = ? WHERE path = ?", [value, path], commit)

	def update_empty_studio_id_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET studio_id = ? WHERE path = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, path], commit)

	def update_o_counter_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE path = ?", [value, path], commit)

	def update_empty_o_counter_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE path = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, path], commit)

	def update_format_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET format = ? WHERE path = ?", [value, path], commit)

	def update_empty_format_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET format = ? WHERE path = ? AND (format IS NULL OR format = '' OR format = 0)", [value, path], commit)

	def update_created_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE path = ?", [value, path], commit)

	def update_empty_created_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE path = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, path], commit)

	def update_updated_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE path = ?", [value, path], commit)

	def update_empty_updated_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE path = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, path], commit)

	def update_file_mod_time_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET file_mod_time = ? WHERE path = ?", [value, path], commit)

	def update_empty_file_mod_time_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET file_mod_time = ? WHERE path = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, path], commit)

	def update_organized_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE path = ?", [value, path], commit)

	def update_empty_organized_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE path = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, path], commit)

	def update_phash_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET phash = ? WHERE path = ?", [value, path], commit)

	def update_empty_phash_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET phash = ? WHERE path = ? AND (phash IS NULL OR phash = '' OR phash = 0)", [value, path], commit)

	def update_interactive_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET interactive = ? WHERE path = ?", [value, path], commit)

	def update_empty_interactive_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET interactive = ? WHERE path = ? AND (interactive IS NULL OR interactive = '' OR interactive = 0)", [value, path], commit)

	def update_interactive_speed_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET interactive_speed = ? WHERE path = ?", [value, path], commit)

	def update_empty_interactive_speed_by_path(self, path, value, commit=True):
		return self.execute("UPDATE scenes SET interactive_speed = ? WHERE path = ? AND (interactive_speed IS NULL OR interactive_speed = '' OR interactive_speed = 0)", [value, path], commit)

	def update_title_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_title_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE checksum = ? AND (title IS NULL OR title = '' OR title = 0)", [value, checksum], commit)

	def update_details_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_details_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE checksum = ? AND (details IS NULL OR details = '' OR details = 0)", [value, checksum], commit)

	def update_url_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET url = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_url_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET url = ? WHERE checksum = ? AND (url IS NULL OR url = '' OR url = 0)", [value, checksum], commit)

	def update_date_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_date_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE checksum = ? AND (date IS NULL OR date = '' OR date = 0)", [value, checksum], commit)

	def update_rating_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_rating_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE checksum = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, checksum], commit)

	def update_size_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET size = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_size_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET size = ? WHERE checksum = ? AND (size IS NULL OR size = '' OR size = 0)", [value, checksum], commit)

	def update_duration_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET duration = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_duration_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET duration = ? WHERE checksum = ? AND (duration IS NULL OR duration = '' OR duration = 0)", [value, checksum], commit)

	def update_video_codec_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET video_codec = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_video_codec_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET video_codec = ? WHERE checksum = ? AND (video_codec IS NULL OR video_codec = '' OR video_codec = 0)", [value, checksum], commit)

	def update_audio_codec_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET audio_codec = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_audio_codec_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET audio_codec = ? WHERE checksum = ? AND (audio_codec IS NULL OR audio_codec = '' OR audio_codec = 0)", [value, checksum], commit)

	def update_width_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET width = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_width_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET width = ? WHERE checksum = ? AND (width IS NULL OR width = '' OR width = 0)", [value, checksum], commit)

	def update_height_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET height = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_height_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET height = ? WHERE checksum = ? AND (height IS NULL OR height = '' OR height = 0)", [value, checksum], commit)

	def update_framerate_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET framerate = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_framerate_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET framerate = ? WHERE checksum = ? AND (framerate IS NULL OR framerate = '' OR framerate = 0)", [value, checksum], commit)

	def update_bitrate_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET bitrate = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_bitrate_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET bitrate = ? WHERE checksum = ? AND (bitrate IS NULL OR bitrate = '' OR bitrate = 0)", [value, checksum], commit)

	def update_studio_id_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET studio_id = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_studio_id_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET studio_id = ? WHERE checksum = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, checksum], commit)

	def update_o_counter_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_o_counter_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE checksum = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, checksum], commit)

	def update_format_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET format = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_format_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET format = ? WHERE checksum = ? AND (format IS NULL OR format = '' OR format = 0)", [value, checksum], commit)

	def update_created_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_created_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE checksum = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, checksum], commit)

	def update_updated_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_updated_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE checksum = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, checksum], commit)

	def update_file_mod_time_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET file_mod_time = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_file_mod_time_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET file_mod_time = ? WHERE checksum = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, checksum], commit)

	def update_organized_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_organized_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE checksum = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, checksum], commit)

	def update_phash_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET phash = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_phash_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET phash = ? WHERE checksum = ? AND (phash IS NULL OR phash = '' OR phash = 0)", [value, checksum], commit)

	def update_interactive_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET interactive = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_interactive_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET interactive = ? WHERE checksum = ? AND (interactive IS NULL OR interactive = '' OR interactive = 0)", [value, checksum], commit)

	def update_interactive_speed_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET interactive_speed = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_interactive_speed_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE scenes SET interactive_speed = ? WHERE checksum = ? AND (interactive_speed IS NULL OR interactive_speed = '' OR interactive_speed = 0)", [value, checksum], commit)

	def update_title_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_title_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE oshash = ? AND (title IS NULL OR title = '' OR title = 0)", [value, oshash], commit)

	def update_details_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_details_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE oshash = ? AND (details IS NULL OR details = '' OR details = 0)", [value, oshash], commit)

	def update_url_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET url = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_url_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET url = ? WHERE oshash = ? AND (url IS NULL OR url = '' OR url = 0)", [value, oshash], commit)

	def update_date_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_date_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE oshash = ? AND (date IS NULL OR date = '' OR date = 0)", [value, oshash], commit)

	def update_rating_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_rating_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE oshash = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, oshash], commit)

	def update_size_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET size = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_size_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET size = ? WHERE oshash = ? AND (size IS NULL OR size = '' OR size = 0)", [value, oshash], commit)

	def update_duration_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET duration = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_duration_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET duration = ? WHERE oshash = ? AND (duration IS NULL OR duration = '' OR duration = 0)", [value, oshash], commit)

	def update_video_codec_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET video_codec = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_video_codec_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET video_codec = ? WHERE oshash = ? AND (video_codec IS NULL OR video_codec = '' OR video_codec = 0)", [value, oshash], commit)

	def update_audio_codec_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET audio_codec = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_audio_codec_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET audio_codec = ? WHERE oshash = ? AND (audio_codec IS NULL OR audio_codec = '' OR audio_codec = 0)", [value, oshash], commit)

	def update_width_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET width = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_width_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET width = ? WHERE oshash = ? AND (width IS NULL OR width = '' OR width = 0)", [value, oshash], commit)

	def update_height_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET height = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_height_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET height = ? WHERE oshash = ? AND (height IS NULL OR height = '' OR height = 0)", [value, oshash], commit)

	def update_framerate_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET framerate = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_framerate_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET framerate = ? WHERE oshash = ? AND (framerate IS NULL OR framerate = '' OR framerate = 0)", [value, oshash], commit)

	def update_bitrate_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET bitrate = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_bitrate_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET bitrate = ? WHERE oshash = ? AND (bitrate IS NULL OR bitrate = '' OR bitrate = 0)", [value, oshash], commit)

	def update_studio_id_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET studio_id = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_studio_id_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET studio_id = ? WHERE oshash = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, oshash], commit)

	def update_o_counter_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_o_counter_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE oshash = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, oshash], commit)

	def update_format_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET format = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_format_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET format = ? WHERE oshash = ? AND (format IS NULL OR format = '' OR format = 0)", [value, oshash], commit)

	def update_created_at_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_created_at_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE oshash = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, oshash], commit)

	def update_updated_at_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_updated_at_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE oshash = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, oshash], commit)

	def update_file_mod_time_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET file_mod_time = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_file_mod_time_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET file_mod_time = ? WHERE oshash = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, oshash], commit)

	def update_organized_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_organized_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE oshash = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, oshash], commit)

	def update_phash_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET phash = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_phash_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET phash = ? WHERE oshash = ? AND (phash IS NULL OR phash = '' OR phash = 0)", [value, oshash], commit)

	def update_interactive_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET interactive = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_interactive_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET interactive = ? WHERE oshash = ? AND (interactive IS NULL OR interactive = '' OR interactive = 0)", [value, oshash], commit)

	def update_interactive_speed_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET interactive_speed = ? WHERE oshash = ?", [value, oshash], commit)

	def update_empty_interactive_speed_by_oshash(self, oshash, value, commit=True):
		return self.execute("UPDATE scenes SET interactive_speed = ? WHERE oshash = ? AND (interactive_speed IS NULL OR interactive_speed = '' OR interactive_speed = 0)", [value, oshash], commit)

	def update_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET title = ? WHERE studio_id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, studio_id], commit)

	def update_details_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_details_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET details = ? WHERE studio_id = ? AND (details IS NULL OR details = '' OR details = 0)", [value, studio_id], commit)

	def update_url_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET url = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_url_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET url = ? WHERE studio_id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, studio_id], commit)

	def update_date_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_date_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET date = ? WHERE studio_id = ? AND (date IS NULL OR date = '' OR date = 0)", [value, studio_id], commit)

	def update_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET rating = ? WHERE studio_id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, studio_id], commit)

	def update_size_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET size = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_size_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET size = ? WHERE studio_id = ? AND (size IS NULL OR size = '' OR size = 0)", [value, studio_id], commit)

	def update_duration_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET duration = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_duration_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET duration = ? WHERE studio_id = ? AND (duration IS NULL OR duration = '' OR duration = 0)", [value, studio_id], commit)

	def update_video_codec_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET video_codec = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_video_codec_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET video_codec = ? WHERE studio_id = ? AND (video_codec IS NULL OR video_codec = '' OR video_codec = 0)", [value, studio_id], commit)

	def update_audio_codec_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET audio_codec = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_audio_codec_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET audio_codec = ? WHERE studio_id = ? AND (audio_codec IS NULL OR audio_codec = '' OR audio_codec = 0)", [value, studio_id], commit)

	def update_width_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET width = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_width_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET width = ? WHERE studio_id = ? AND (width IS NULL OR width = '' OR width = 0)", [value, studio_id], commit)

	def update_height_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET height = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_height_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET height = ? WHERE studio_id = ? AND (height IS NULL OR height = '' OR height = 0)", [value, studio_id], commit)

	def update_framerate_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET framerate = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_framerate_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET framerate = ? WHERE studio_id = ? AND (framerate IS NULL OR framerate = '' OR framerate = 0)", [value, studio_id], commit)

	def update_bitrate_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET bitrate = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_bitrate_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET bitrate = ? WHERE studio_id = ? AND (bitrate IS NULL OR bitrate = '' OR bitrate = 0)", [value, studio_id], commit)

	def update_o_counter_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_o_counter_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET o_counter = ? WHERE studio_id = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, studio_id], commit)

	def update_format_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET format = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_format_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET format = ? WHERE studio_id = ? AND (format IS NULL OR format = '' OR format = 0)", [value, studio_id], commit)

	def update_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET created_at = ? WHERE studio_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, studio_id], commit)

	def update_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET updated_at = ? WHERE studio_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, studio_id], commit)

	def update_file_mod_time_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET file_mod_time = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_file_mod_time_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET file_mod_time = ? WHERE studio_id = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, studio_id], commit)

	def update_organized_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_organized_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET organized = ? WHERE studio_id = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, studio_id], commit)

	def update_phash_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET phash = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_phash_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET phash = ? WHERE studio_id = ? AND (phash IS NULL OR phash = '' OR phash = 0)", [value, studio_id], commit)

	def update_interactive_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET interactive = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_interactive_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET interactive = ? WHERE studio_id = ? AND (interactive IS NULL OR interactive = '' OR interactive = 0)", [value, studio_id], commit)

	def update_interactive_speed_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET interactive_speed = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_interactive_speed_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE scenes SET interactive_speed = ? WHERE studio_id = ? AND (interactive_speed IS NULL OR interactive_speed = '' OR interactive_speed = 0)", [value, studio_id], commit)

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

	def update_scene_id_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performers_scenes SET scene_id = ? WHERE performer_id = ?", [value, performer_id], commit)

	def update_empty_scene_id_by_performer_id(self, performer_id, value, commit=True):
		return self.execute("UPDATE performers_scenes SET scene_id = ? WHERE performer_id = ? AND (scene_id IS NULL OR scene_id = '' OR scene_id = 0)", [value, performer_id], commit)

	def update_performer_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE performers_scenes SET performer_id = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_performer_id_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE performers_scenes SET performer_id = ? WHERE scene_id = ? AND (performer_id IS NULL OR performer_id = '' OR performer_id = 0)", [value, scene_id], commit)

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

class ScenesCover(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'scenes_cover')

	def select_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		return [ScenesCoverRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_cover(self, cover, colvalues={}, selectcols=['*']):
		colvalues['cover'] = cover
		return [ScenesCoverRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesCoverRow().from_sqliterow(row)
		else:
			return None

	def selectone_cover(self, cover, colvalues={}, selectcols=['*']):
		colvalues['cover'] = cover
		row = self.selectone(colvalues, selectcols)
		if row:
			return ScenesCoverRow().from_sqliterow(row)
		else:
			return None

	def insert(self, scene_id, cover, commit=True):
		return self.execute("INSERT INTO scenes_cover (scene_id, cover) VALUES (?, ?)", [scene_id, cover], commit)

	def insert_model(self, model: ScenesCoverRow, commit=True):
		return self.execute("INSERT INTO scenes_cover (scene_id, cover) VALUES (?, ?)", model.values_list(False), commit)

	def update_cover_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scenes_cover SET cover = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_cover_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scenes_cover SET cover = ? WHERE scene_id = ? AND (cover IS NULL OR cover = '' OR cover = 0)", [value, scene_id], commit)

class Images(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'images')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_path(self, path, colvalues={}, selectcols=['*']):
		colvalues['path'] = path
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_rating(self, rating, colvalues={}, selectcols=['*']):
		colvalues['rating'] = rating
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_size(self, size, colvalues={}, selectcols=['*']):
		colvalues['size'] = size
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_width(self, width, colvalues={}, selectcols=['*']):
		colvalues['width'] = width
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_height(self, height, colvalues={}, selectcols=['*']):
		colvalues['height'] = height
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_studio_id(self, studio_id, colvalues={}, selectcols=['*']):
		colvalues['studio_id'] = studio_id
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_o_counter(self, o_counter, colvalues={}, selectcols=['*']):
		colvalues['o_counter'] = o_counter
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_created_at(self, created_at, colvalues={}, selectcols=['*']):
		colvalues['created_at'] = created_at
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_updated_at(self, updated_at, colvalues={}, selectcols=['*']):
		colvalues['updated_at'] = updated_at
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_file_mod_time(self, file_mod_time, colvalues={}, selectcols=['*']):
		colvalues['file_mod_time'] = file_mod_time
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_organized(self, organized, colvalues={}, selectcols=['*']):
		colvalues['organized'] = organized
		return [ImagesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_path(self, path, colvalues={}, selectcols=['*']):
		colvalues['path'] = path
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
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

	def selectone_size(self, size, colvalues={}, selectcols=['*']):
		colvalues['size'] = size
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_width(self, width, colvalues={}, selectcols=['*']):
		colvalues['width'] = width
		row = self.selectone(colvalues, selectcols)
		if row:
			return ImagesRow().from_sqliterow(row)
		else:
			return None

	def selectone_height(self, height, colvalues={}, selectcols=['*']):
		colvalues['height'] = height
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

	def selectone_file_mod_time(self, file_mod_time, colvalues={}, selectcols=['*']):
		colvalues['file_mod_time'] = file_mod_time
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

	def insert(self, path, checksum, title, rating, size, width, height, studio_id, o_counter, created_at, updated_at, file_mod_time, organized, commit=True):
		return self.execute("INSERT INTO images (path, checksum, title, rating, size, width, height, studio_id, o_counter, created_at, updated_at, file_mod_time, organized) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [path, checksum, title, rating, size, width, height, studio_id, o_counter, created_at, updated_at, file_mod_time, organized], commit)

	def insert_model(self, model: ImagesRow, commit=True):
		return self.execute("INSERT INTO images (path, checksum, title, rating, size, width, height, studio_id, o_counter, created_at, updated_at, file_mod_time, organized) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def update_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET title = ? WHERE id = ?", [value, id], commit)

	def update_empty_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET title = ? WHERE id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, id], commit)

	def update_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET rating = ? WHERE id = ?", [value, id], commit)

	def update_empty_rating_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET rating = ? WHERE id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, id], commit)

	def update_size_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET size = ? WHERE id = ?", [value, id], commit)

	def update_empty_size_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET size = ? WHERE id = ? AND (size IS NULL OR size = '' OR size = 0)", [value, id], commit)

	def update_width_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET width = ? WHERE id = ?", [value, id], commit)

	def update_empty_width_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET width = ? WHERE id = ? AND (width IS NULL OR width = '' OR width = 0)", [value, id], commit)

	def update_height_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET height = ? WHERE id = ?", [value, id], commit)

	def update_empty_height_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET height = ? WHERE id = ? AND (height IS NULL OR height = '' OR height = 0)", [value, id], commit)

	def update_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET studio_id = ? WHERE id = ?", [value, id], commit)

	def update_empty_studio_id_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET studio_id = ? WHERE id = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, id], commit)

	def update_o_counter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET o_counter = ? WHERE id = ?", [value, id], commit)

	def update_empty_o_counter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET o_counter = ? WHERE id = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, id], commit)

	def update_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET created_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_created_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET created_at = ? WHERE id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, id], commit)

	def update_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET updated_at = ? WHERE id = ?", [value, id], commit)

	def update_empty_updated_at_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET updated_at = ? WHERE id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, id], commit)

	def update_file_mod_time_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET file_mod_time = ? WHERE id = ?", [value, id], commit)

	def update_empty_file_mod_time_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET file_mod_time = ? WHERE id = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, id], commit)

	def update_organized_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET organized = ? WHERE id = ?", [value, id], commit)

	def update_empty_organized_by_id(self, id, value, commit=True):
		return self.execute("UPDATE images SET organized = ? WHERE id = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, id], commit)

	def update_title_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET title = ? WHERE path = ?", [value, path], commit)

	def update_empty_title_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET title = ? WHERE path = ? AND (title IS NULL OR title = '' OR title = 0)", [value, path], commit)

	def update_rating_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET rating = ? WHERE path = ?", [value, path], commit)

	def update_empty_rating_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET rating = ? WHERE path = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, path], commit)

	def update_size_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET size = ? WHERE path = ?", [value, path], commit)

	def update_empty_size_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET size = ? WHERE path = ? AND (size IS NULL OR size = '' OR size = 0)", [value, path], commit)

	def update_width_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET width = ? WHERE path = ?", [value, path], commit)

	def update_empty_width_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET width = ? WHERE path = ? AND (width IS NULL OR width = '' OR width = 0)", [value, path], commit)

	def update_height_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET height = ? WHERE path = ?", [value, path], commit)

	def update_empty_height_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET height = ? WHERE path = ? AND (height IS NULL OR height = '' OR height = 0)", [value, path], commit)

	def update_studio_id_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET studio_id = ? WHERE path = ?", [value, path], commit)

	def update_empty_studio_id_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET studio_id = ? WHERE path = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, path], commit)

	def update_o_counter_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET o_counter = ? WHERE path = ?", [value, path], commit)

	def update_empty_o_counter_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET o_counter = ? WHERE path = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, path], commit)

	def update_created_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET created_at = ? WHERE path = ?", [value, path], commit)

	def update_empty_created_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET created_at = ? WHERE path = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, path], commit)

	def update_updated_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET updated_at = ? WHERE path = ?", [value, path], commit)

	def update_empty_updated_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET updated_at = ? WHERE path = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, path], commit)

	def update_file_mod_time_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET file_mod_time = ? WHERE path = ?", [value, path], commit)

	def update_empty_file_mod_time_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET file_mod_time = ? WHERE path = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, path], commit)

	def update_organized_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET organized = ? WHERE path = ?", [value, path], commit)

	def update_empty_organized_by_path(self, path, value, commit=True):
		return self.execute("UPDATE images SET organized = ? WHERE path = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, path], commit)

	def update_title_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET title = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_title_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET title = ? WHERE checksum = ? AND (title IS NULL OR title = '' OR title = 0)", [value, checksum], commit)

	def update_rating_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET rating = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_rating_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET rating = ? WHERE checksum = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, checksum], commit)

	def update_size_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET size = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_size_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET size = ? WHERE checksum = ? AND (size IS NULL OR size = '' OR size = 0)", [value, checksum], commit)

	def update_width_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET width = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_width_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET width = ? WHERE checksum = ? AND (width IS NULL OR width = '' OR width = 0)", [value, checksum], commit)

	def update_height_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET height = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_height_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET height = ? WHERE checksum = ? AND (height IS NULL OR height = '' OR height = 0)", [value, checksum], commit)

	def update_studio_id_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET studio_id = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_studio_id_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET studio_id = ? WHERE checksum = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, checksum], commit)

	def update_o_counter_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET o_counter = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_o_counter_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET o_counter = ? WHERE checksum = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, checksum], commit)

	def update_created_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET created_at = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_created_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET created_at = ? WHERE checksum = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, checksum], commit)

	def update_updated_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET updated_at = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_updated_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET updated_at = ? WHERE checksum = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, checksum], commit)

	def update_file_mod_time_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET file_mod_time = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_file_mod_time_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET file_mod_time = ? WHERE checksum = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, checksum], commit)

	def update_organized_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET organized = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_organized_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE images SET organized = ? WHERE checksum = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, checksum], commit)

	def update_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET title = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET title = ? WHERE studio_id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, studio_id], commit)

	def update_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET rating = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_rating_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET rating = ? WHERE studio_id = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, studio_id], commit)

	def update_size_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET size = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_size_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET size = ? WHERE studio_id = ? AND (size IS NULL OR size = '' OR size = 0)", [value, studio_id], commit)

	def update_width_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET width = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_width_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET width = ? WHERE studio_id = ? AND (width IS NULL OR width = '' OR width = 0)", [value, studio_id], commit)

	def update_height_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET height = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_height_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET height = ? WHERE studio_id = ? AND (height IS NULL OR height = '' OR height = 0)", [value, studio_id], commit)

	def update_o_counter_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET o_counter = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_o_counter_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET o_counter = ? WHERE studio_id = ? AND (o_counter IS NULL OR o_counter = '' OR o_counter = 0)", [value, studio_id], commit)

	def update_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET created_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_created_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET created_at = ? WHERE studio_id = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, studio_id], commit)

	def update_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET updated_at = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_updated_at_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET updated_at = ? WHERE studio_id = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, studio_id], commit)

	def update_file_mod_time_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET file_mod_time = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_file_mod_time_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET file_mod_time = ? WHERE studio_id = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, studio_id], commit)

	def update_organized_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET organized = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_organized_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE images SET organized = ? WHERE studio_id = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, studio_id], commit)

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

class Galleries(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'galleries')

	def select_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_path(self, path, colvalues={}, selectcols=['*']):
		colvalues['path'] = path
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_zip(self, zip, colvalues={}, selectcols=['*']):
		colvalues['zip'] = zip
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_title(self, title, colvalues={}, selectcols=['*']):
		colvalues['title'] = title
		return [GalleriesRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
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

	def select_file_mod_time(self, file_mod_time, colvalues={}, selectcols=['*']):
		colvalues['file_mod_time'] = file_mod_time
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

	def selectone_id(self, id, colvalues={}, selectcols=['*']):
		colvalues['id'] = id
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_path(self, path, colvalues={}, selectcols=['*']):
		colvalues['path'] = path
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_checksum(self, checksum, colvalues={}, selectcols=['*']):
		colvalues['checksum'] = checksum
		row = self.selectone(colvalues, selectcols)
		if row:
			return GalleriesRow().from_sqliterow(row)
		else:
			return None

	def selectone_zip(self, zip, colvalues={}, selectcols=['*']):
		colvalues['zip'] = zip
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

	def selectone_url(self, url, colvalues={}, selectcols=['*']):
		colvalues['url'] = url
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

	def selectone_file_mod_time(self, file_mod_time, colvalues={}, selectcols=['*']):
		colvalues['file_mod_time'] = file_mod_time
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

	def insert(self, path, checksum, zip, title, url, date, details, studio_id, rating, file_mod_time, organized, created_at, updated_at, commit=True):
		return self.execute("INSERT INTO galleries (path, checksum, zip, title, url, date, details, studio_id, rating, file_mod_time, organized, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [path, checksum, zip, title, url, date, details, studio_id, rating, file_mod_time, organized, created_at, updated_at], commit)

	def insert_model(self, model: GalleriesRow, commit=True):
		return self.execute("INSERT INTO galleries (path, checksum, zip, title, url, date, details, studio_id, rating, file_mod_time, organized, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", model.values_list(False), commit)

	def update_zip_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET zip = ? WHERE id = ?", [value, id], commit)

	def update_empty_zip_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET zip = ? WHERE id = ? AND (zip IS NULL OR zip = '' OR zip = 0)", [value, id], commit)

	def update_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE id = ?", [value, id], commit)

	def update_empty_title_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, id], commit)

	def update_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET url = ? WHERE id = ?", [value, id], commit)

	def update_empty_url_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET url = ? WHERE id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, id], commit)

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

	def update_file_mod_time_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET file_mod_time = ? WHERE id = ?", [value, id], commit)

	def update_empty_file_mod_time_by_id(self, id, value, commit=True):
		return self.execute("UPDATE galleries SET file_mod_time = ? WHERE id = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, id], commit)

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

	def update_zip_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET zip = ? WHERE path = ?", [value, path], commit)

	def update_empty_zip_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET zip = ? WHERE path = ? AND (zip IS NULL OR zip = '' OR zip = 0)", [value, path], commit)

	def update_title_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE path = ?", [value, path], commit)

	def update_empty_title_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE path = ? AND (title IS NULL OR title = '' OR title = 0)", [value, path], commit)

	def update_url_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET url = ? WHERE path = ?", [value, path], commit)

	def update_empty_url_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET url = ? WHERE path = ? AND (url IS NULL OR url = '' OR url = 0)", [value, path], commit)

	def update_date_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET date = ? WHERE path = ?", [value, path], commit)

	def update_empty_date_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET date = ? WHERE path = ? AND (date IS NULL OR date = '' OR date = 0)", [value, path], commit)

	def update_details_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET details = ? WHERE path = ?", [value, path], commit)

	def update_empty_details_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET details = ? WHERE path = ? AND (details IS NULL OR details = '' OR details = 0)", [value, path], commit)

	def update_studio_id_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET studio_id = ? WHERE path = ?", [value, path], commit)

	def update_empty_studio_id_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET studio_id = ? WHERE path = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, path], commit)

	def update_rating_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET rating = ? WHERE path = ?", [value, path], commit)

	def update_empty_rating_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET rating = ? WHERE path = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, path], commit)

	def update_file_mod_time_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET file_mod_time = ? WHERE path = ?", [value, path], commit)

	def update_empty_file_mod_time_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET file_mod_time = ? WHERE path = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, path], commit)

	def update_organized_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET organized = ? WHERE path = ?", [value, path], commit)

	def update_empty_organized_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET organized = ? WHERE path = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, path], commit)

	def update_created_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET created_at = ? WHERE path = ?", [value, path], commit)

	def update_empty_created_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET created_at = ? WHERE path = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, path], commit)

	def update_updated_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET updated_at = ? WHERE path = ?", [value, path], commit)

	def update_empty_updated_at_by_path(self, path, value, commit=True):
		return self.execute("UPDATE galleries SET updated_at = ? WHERE path = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, path], commit)

	def update_zip_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET zip = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_zip_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET zip = ? WHERE checksum = ? AND (zip IS NULL OR zip = '' OR zip = 0)", [value, checksum], commit)

	def update_title_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_title_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE checksum = ? AND (title IS NULL OR title = '' OR title = 0)", [value, checksum], commit)

	def update_url_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET url = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_url_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET url = ? WHERE checksum = ? AND (url IS NULL OR url = '' OR url = 0)", [value, checksum], commit)

	def update_date_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET date = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_date_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET date = ? WHERE checksum = ? AND (date IS NULL OR date = '' OR date = 0)", [value, checksum], commit)

	def update_details_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET details = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_details_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET details = ? WHERE checksum = ? AND (details IS NULL OR details = '' OR details = 0)", [value, checksum], commit)

	def update_studio_id_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET studio_id = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_studio_id_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET studio_id = ? WHERE checksum = ? AND (studio_id IS NULL OR studio_id = '' OR studio_id = 0)", [value, checksum], commit)

	def update_rating_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET rating = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_rating_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET rating = ? WHERE checksum = ? AND (rating IS NULL OR rating = '' OR rating = 0)", [value, checksum], commit)

	def update_file_mod_time_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET file_mod_time = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_file_mod_time_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET file_mod_time = ? WHERE checksum = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, checksum], commit)

	def update_organized_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET organized = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_organized_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET organized = ? WHERE checksum = ? AND (organized IS NULL OR organized = '' OR organized = 0)", [value, checksum], commit)

	def update_created_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET created_at = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_created_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET created_at = ? WHERE checksum = ? AND (created_at IS NULL OR created_at = '' OR created_at = 0)", [value, checksum], commit)

	def update_updated_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET updated_at = ? WHERE checksum = ?", [value, checksum], commit)

	def update_empty_updated_at_by_checksum(self, checksum, value, commit=True):
		return self.execute("UPDATE galleries SET updated_at = ? WHERE checksum = ? AND (updated_at IS NULL OR updated_at = '' OR updated_at = 0)", [value, checksum], commit)

	def update_zip_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET zip = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_zip_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET zip = ? WHERE studio_id = ? AND (zip IS NULL OR zip = '' OR zip = 0)", [value, studio_id], commit)

	def update_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_title_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET title = ? WHERE studio_id = ? AND (title IS NULL OR title = '' OR title = 0)", [value, studio_id], commit)

	def update_url_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET url = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_url_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET url = ? WHERE studio_id = ? AND (url IS NULL OR url = '' OR url = 0)", [value, studio_id], commit)

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

	def update_file_mod_time_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET file_mod_time = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_file_mod_time_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE galleries SET file_mod_time = ? WHERE studio_id = ? AND (file_mod_time IS NULL OR file_mod_time = '' OR file_mod_time = 0)", [value, studio_id], commit)

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

	def update_alias_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE tag_aliases SET alias = ? WHERE tag_id = ?", [value, tag_id], commit)

	def update_empty_alias_by_tag_id(self, tag_id, value, commit=True):
		return self.execute("UPDATE tag_aliases SET alias = ? WHERE tag_id = ? AND (alias IS NULL OR alias = '' OR alias = 0)", [value, tag_id], commit)

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

	def select_filter(self, filter, colvalues={}, selectcols=['*']):
		colvalues['filter'] = filter
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

	def selectone_filter(self, filter, colvalues={}, selectcols=['*']):
		colvalues['filter'] = filter
		row = self.selectone(colvalues, selectcols)
		if row:
			return SavedFiltersRow().from_sqliterow(row)
		else:
			return None

	def insert(self, name, mode, filter, commit=True):
		return self.execute("INSERT INTO saved_filters (name, mode, filter) VALUES (?, ?, ?)", [name, mode, filter], commit)

	def insert_model(self, model: SavedFiltersRow, commit=True):
		return self.execute("INSERT INTO saved_filters (name, mode, filter) VALUES (?, ?, ?)", model.values_list(False), commit)

	def update_mode_by_id(self, id, value, commit=True):
		return self.execute("UPDATE saved_filters SET mode = ? WHERE id = ?", [value, id], commit)

	def update_empty_mode_by_id(self, id, value, commit=True):
		return self.execute("UPDATE saved_filters SET mode = ? WHERE id = ? AND (mode IS NULL OR mode = '' OR mode = 0)", [value, id], commit)

	def update_filter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE saved_filters SET filter = ? WHERE id = ?", [value, id], commit)

	def update_empty_filter_by_id(self, id, value, commit=True):
		return self.execute("UPDATE saved_filters SET filter = ? WHERE id = ? AND (filter IS NULL OR filter = '' OR filter = 0)", [value, id], commit)

	def update_mode_by_name(self, name, value, commit=True):
		return self.execute("UPDATE saved_filters SET mode = ? WHERE name = ?", [value, name], commit)

	def update_empty_mode_by_name(self, name, value, commit=True):
		return self.execute("UPDATE saved_filters SET mode = ? WHERE name = ? AND (mode IS NULL OR mode = '' OR mode = 0)", [value, name], commit)

	def update_filter_by_name(self, name, value, commit=True):
		return self.execute("UPDATE saved_filters SET filter = ? WHERE name = ?", [value, name], commit)

	def update_empty_filter_by_name(self, name, value, commit=True):
		return self.execute("UPDATE saved_filters SET filter = ? WHERE name = ? AND (filter IS NULL OR filter = '' OR filter = 0)", [value, name], commit)

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

	def update_child_id_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE tags_relations SET child_id = ? WHERE parent_id = ?", [value, parent_id], commit)

	def update_empty_child_id_by_parent_id(self, parent_id, value, commit=True):
		return self.execute("UPDATE tags_relations SET child_id = ? WHERE parent_id = ? AND (child_id IS NULL OR child_id = '' OR child_id = 0)", [value, parent_id], commit)

	def update_parent_id_by_child_id(self, child_id, value, commit=True):
		return self.execute("UPDATE tags_relations SET parent_id = ? WHERE child_id = ?", [value, child_id], commit)

	def update_empty_parent_id_by_child_id(self, child_id, value, commit=True):
		return self.execute("UPDATE tags_relations SET parent_id = ? WHERE child_id = ? AND (parent_id IS NULL OR parent_id = '' OR parent_id = 0)", [value, child_id], commit)

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

	def update_alias_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE studio_aliases SET alias = ? WHERE studio_id = ?", [value, studio_id], commit)

	def update_empty_alias_by_studio_id(self, studio_id, value, commit=True):
		return self.execute("UPDATE studio_aliases SET alias = ? WHERE studio_id = ? AND (alias IS NULL OR alias = '' OR alias = 0)", [value, studio_id], commit)

class SceneCaptions(Table):
	def __init__(self, conn: sqlite3.Connection):
		super().__init__(conn, 'scene_captions')

	def select_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		return [SceneCaptionsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_language_code(self, language_code, colvalues={}, selectcols=['*']):
		colvalues['language_code'] = language_code
		return [SceneCaptionsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_filename(self, filename, colvalues={}, selectcols=['*']):
		colvalues['filename'] = filename
		return [SceneCaptionsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def select_caption_type(self, caption_type, colvalues={}, selectcols=['*']):
		colvalues['caption_type'] = caption_type
		return [SceneCaptionsRow().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

	def selectone_scene_id(self, scene_id, colvalues={}, selectcols=['*']):
		colvalues['scene_id'] = scene_id
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneCaptionsRow().from_sqliterow(row)
		else:
			return None

	def selectone_language_code(self, language_code, colvalues={}, selectcols=['*']):
		colvalues['language_code'] = language_code
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneCaptionsRow().from_sqliterow(row)
		else:
			return None

	def selectone_filename(self, filename, colvalues={}, selectcols=['*']):
		colvalues['filename'] = filename
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneCaptionsRow().from_sqliterow(row)
		else:
			return None

	def selectone_caption_type(self, caption_type, colvalues={}, selectcols=['*']):
		colvalues['caption_type'] = caption_type
		row = self.selectone(colvalues, selectcols)
		if row:
			return SceneCaptionsRow().from_sqliterow(row)
		else:
			return None

	def insert(self, scene_id, language_code, filename, caption_type, commit=True):
		return self.execute("INSERT INTO scene_captions (scene_id, language_code, filename, caption_type) VALUES (?, ?, ?, ?)", [scene_id, language_code, filename, caption_type], commit)

	def insert_model(self, model: SceneCaptionsRow, commit=True):
		return self.execute("INSERT INTO scene_captions (scene_id, language_code, filename, caption_type) VALUES (?, ?, ?, ?)", model.values_list(False), commit)

	def update_language_code_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_captions SET language_code = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_language_code_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_captions SET language_code = ? WHERE scene_id = ? AND (language_code IS NULL OR language_code = '' OR language_code = 0)", [value, scene_id], commit)

	def update_filename_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_captions SET filename = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_filename_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_captions SET filename = ? WHERE scene_id = ? AND (filename IS NULL OR filename = '' OR filename = 0)", [value, scene_id], commit)

	def update_caption_type_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_captions SET caption_type = ? WHERE scene_id = ?", [value, scene_id], commit)

	def update_empty_caption_type_by_scene_id(self, scene_id, value, commit=True):
		return self.execute("UPDATE scene_captions SET caption_type = ? WHERE scene_id = ? AND (caption_type IS NULL OR caption_type = '' OR caption_type = 0)", [value, scene_id], commit)

