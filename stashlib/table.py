import sqlite3
from . import sqlite_wrapper as sq

class Table(object):
    
    def __init__(self, conn: sqlite3.Connection, table_name):
        self._table_name = table_name
        self._conn = conn
        self._columns = sq.db_table_columns(self._conn, table_name)

    @property
    def table_name(self):
        return self._table_name

    @property
    def conn(self):
        return self._conn

    @conn.setter
    def conn(self, conn: sqlite3.Connection):
        self._conn = conn

    def execute(self, sql, vals, commit=True):
        return sq.db_execute(self.conn, sql, vals, commit)

    def select(self, colvalues=None, selectcols=['*']):
        return sq.db_select(self.conn, self._table_name, colvalues, selectcols)

    def selectone(self, colvalues=None, selectcols=['*']):
        return sq.db_selectone(self.conn, self._table_name, colvalues, selectcols)

    def row_update(self, colvalues, keys, wherevalues=None, check_empty=False, commit=True):
        return sq.db_update(self.conn, self._table_name, colvalues, keys, wherevalues, check_empty, commit)

    def row_insert(self, colvalues, commit=True):
        return sq.db_insert(self.conn, self._table_name, colvalues, commit)
        
    def row_upsert(self, colvalues, keys=None, wherevalues=None, check_empty=False, commit=True):
        return sq.db_upsert(self.conn, self._table_name, colvalues, keys, wherevalues, check_empty, commit)

class TableRow(object):
    def __init__(self, table_name):
        self._table_name = table_name

    def from_dict(self, row_dict):
        for col, val in row_dict.items():
            setattr(self, col, val)
        return self

    def from_sqliterow(self, row):
        for col in row.keys():
            setattr(self, col, row[col])
        return self