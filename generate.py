from stashlib.common import camel_case, array_param
from stashlib.database import Database

def generate_database(db_path, outfile, schema_version):
    with Database(db_path) as db:
        f = open(outfile, 'w')
        f.write(f"""from . import sqlite_wrapper as sq
from .database import Database
from .stash_tables import *

class StashDatabaseBase(Database):

\tSCHEMA_VERSION = {schema_version}

\tdef __init__(self, db_path):
\t\tsuper().__init__(db_path)
""")
        for table in db.tables:
            print(table)
            cols = db.table_columns(table)
            print(cols)
            f.write(f"""\t\tself.{table} = {camel_case(table)}(self.conn)\n""")

def generate_tables(db_path, outfile):
    with Database(db_path) as db:
        f = open(outfile, 'w')
        f.write(f"""import sqlite3
from .table import Table
from .stash_models import *\n\n""")
        for table in db.tables:
            print(table)
            cols = db.table_columns(table)
            print(cols)
            f.write(f"""class {camel_case(table)}(Table):
\tdef __init__(self, conn: sqlite3.Connection):
\t\tsuper().__init__(conn, '{table}')

""")

            for col in cols:
                f.write(f"""\tdef select_{col}(self, {col}, colvalues={{}}, selectcols=['*']):
\t\tcolvalues['{col}'] = {col}
\t\treturn [{camel_case(table)}Row().from_sqliterow(x) for x in self.select(colvalues, selectcols)]

""")

            for col in cols:
                f.write(f"""\tdef selectone_{col}(self, {col}, colvalues={{}}, selectcols=['*']):
\t\tcolvalues['{col}'] = {col}
\t\trow = self.selectone(colvalues, selectcols)
\t\tif row:
\t\t\treturn {camel_case(table)}Row().from_sqliterow(row)
\t\telse:
\t\t\treturn None

""")

            non_id_cols = [col for col in cols if col != 'id']
            col_params = ', '.join(non_id_cols)
            f.write(f"""\tdef insert(self, {col_params}, commit=True):
\t\treturn self.execute("INSERT INTO {table} ({col_params}) VALUES ({array_param(non_id_cols)})", [{col_params}], commit)

""")
            f.write(f"""\tdef insert_model(self, model: {camel_case(table)}Row, commit=True):
\t\treturn self.execute("INSERT INTO {table} ({col_params}) VALUES ({array_param(non_id_cols)})", model.values_list(False), commit)

""")

            key_cols = ['id', 'name', 'checksum', 'path', 'oshash']
            for col in cols:
                if col in key_cols or col.endswith('_id'):
                    for target_col in cols:
                        if target_col in key_cols or target_col == col:
                            continue
                        f.write(f"""\tdef update_{target_col}_by_{col}(self, {col}, value, commit=True):
\t\treturn self.execute("UPDATE {table} SET {target_col} = ? WHERE {col} = ?", [value, {col}], commit)

\tdef update_empty_{target_col}_by_{col}(self, {col}, value, commit=True):
\t\treturn self.execute("UPDATE {table} SET {target_col} = ? WHERE {col} = ? AND ({target_col} IS NULL OR {target_col} = '' OR {target_col} = 0)", [value, {col}], commit)

""")

        f.close()

def generate_models(db_path, outfile):
    with Database(db_path) as db:
        f = open(outfile, 'w')
        f.write(f"""from .table import TableRow\n\n""")
        for table in db.tables:
            print(table)
            cols = db.table_columns(table)
            print(cols)
            f.write(f"""class {camel_case(table)}Row(TableRow):
\tdef __init__(self):
\t\tsuper().__init__('{table}')
""")
            for col in cols:
                f.write(f"""\t\tself._{col} = None\n""")
            f.write("\n")

            f.write(f"""\t@property
\tdef table_name(self):
\t\treturn self._table_name

""")
            for col in cols:
                f.write(f"""\t@property
\tdef {col}(self):
\t\treturn self._{col}

\t@{col}.setter
\tdef {col}(self, {col}):
\t\tself._{col} = {col}

""")

            f.write(f"""\tdef __str__(self):
\t\treturn str(self.__class__) + ": " + str(self.__dict__)

""")

            f.write(f"""\tdef values_list(self, include_id=False):
\t\tif include_id:
\t\t\treturn [{', '.join(['self.' + col for col in cols])}]
\t\telse:
\t\t\treturn [{', '.join(['self.' + col for col in cols if col != 'id'])}]

""")

        f.close()

generate_database(r'stash-go.sqlite', 'stashlib/stash_database_base.py', 30)
generate_tables(r'stash-go.sqlite', 'stashlib/stash_tables.py')
generate_models(r'stash-go.sqlite', 'stashlib/stash_models.py')

