import os
import re
import sqlite3
from . import sqlite_wrapper as sq
from .common import alphanum_chars
from .logger import logger as log

def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

def studio_matcher(expr, item):
    return alphanum_chars(expr).lower() == alphanum_chars(item).lower()

class Database(object):

    def __init__(self, db_path):
        try:
            if not os.path.isfile(db_path):
                raise Exception(f'database file missing {db_path}')
            self._conn = sqlite3.connect(db_path)
            self._conn.row_factory = sqlite3.Row
            self._conn.execute("PRAGMA foreign_keys = 1")
            self._conn.create_function("REGEXP", 2, regexp)
            self._conn.create_function("STUDIOMATCHER", 2, studio_matcher)
        except sqlite3.Error as e:
            raise Exception("error connecting to database!")
        self._tables = sq.db_tables(self._conn)

    @property
    def conn(self):
        return self._conn

    @property
    def tables(self):
        return self._tables

    def close(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def commit(self):
        self.conn.commit()

    def execute(self, sql, vals=[], commit=True):
        return sq.db_execute(self.conn, sql, vals, commit)

    def fetchall(self, sql, vals=[]):
        c = sq.db_execute(self.conn, sql, vals, commit=False)
        return c.fetchall()

    def fetchone(self, sql, vals=[]):
        results = self.fetchall(sql, vals)
        if results:
            return results[0]
        else:
            return None

    def table_columns(self, table_name):
        return sq.db_table_columns(self.conn, table_name)