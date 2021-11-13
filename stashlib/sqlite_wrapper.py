import sqlite3
from .common import dict_subset, array_param
    
def db_select(conn: sqlite3.Connection, table, colvalues=None, selectcols=['*']):
    vals = []
    where = ''
    if colvalues:
        cols, vals = zip(*colvalues.items())
        where = ' WHERE ' + ' AND '.join([col + ' = ?' for col in cols])
    select = ','.join([col for col in selectcols])
    sql = f"""SELECT {select} FROM {table}{where}"""
    # print(sql, vals)
    c = conn.execute(sql, vals)
    results = c.fetchall()
    if len(selectcols) == 1 and selectcols[0] != '*':
        return [x[0] for x in results]
    else:
        return results

def db_selectone(conn: sqlite3.Connection, table, colvalues=None, selectcols=['*']):
    results = db_select(conn, table, colvalues, selectcols)
    if results:
        return results[0]
    else:
        return None

def db_tables(conn: sqlite3.Connection):
    return db_select(conn, 'sqlite_master', {'type': 'table'}, ['name'])

def db_table_columns(conn: sqlite3.Connection, table):
    c = conn.execute(f"""PRAGMA table_info({table});""")
    return [x[1] for x in c.fetchall()]


def db_execute(conn: sqlite3.Connection, sql, vals, commit=True):
    # print('execute', sql, vals)
    c = conn.execute(sql, vals)
    if commit:
        conn.commit()
    return c

def db_update(conn: sqlite3.Connection, table, colvalues, keys, wherevalues=None, check_empty=False, commit=True):
    cols, vals = zip(*colvalues.items())
    where = ' AND '.join([col + ' = ?' for col in keys])
    if check_empty:
        where  += ' AND ' + ' AND '.join([f"({col} IS NULL OR {col} = '' OR {col} = 0)" for col in cols])
    setvals = ', '.join([col + ' = ?' for col in cols])
    sql = f"""UPDATE {table} SET {setvals} WHERE {where}"""
    if not wherevalues:
        wherevalues = colvalues
    vals += tuple([wherevalues[key] for key in keys])
    return db_execute(conn, sql, vals, commit)

def db_insert(conn: sqlite3.Connection, table, colvalues, commit=True):
    cols, vals = zip(*colvalues.items())
    sql = f"""INSERT INTO {table} ({', '.join(cols)}) VALUES ({array_param(vals)})"""
    return db_execute(conn, sql, vals, commit)
    
def db_upsert(conn: sqlite3.Connection, table, colvalues, keys=None, wherevalues=None, check_empty=False, commit=True):
    if keys:
        keyvals = dict_subset(colvalues, keys)
        rows = db_select(conn, table, keyvals)
        if rows:
            return db_update(conn, table, colvalues, keys, wherevalues, check_empty, commit)
    return db_insert(conn, table, colvalues, commit)
