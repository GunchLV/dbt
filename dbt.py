import pandas as pd
from sqlalchemy import create_engine, inspect
import inspect as pyinspect
import difflib

engine = create_engine("sqlite:///example.db")

class DB:
    def __new__(cls, table, col_where='', where='', limit=None):
        
        if not isinstance(table, str): # if table is not string, use variable as name
            frame = pyinspect.currentframe().f_back
            name = next((k for k, v in frame.f_globals.items() if v is table), None)
            table = name or str(table)
        
        if isinstance(col_where, int): # this will allow to use limit at any place
            limit = col_where
            col_where = ''
        if isinstance(where, int):
            limit = where
            where = ''
        
        def build_query(tbl): # make query from all parts
            if col_where == '' and where == '':
                query = f'SELECT * FROM {tbl}'
            elif col_where and not where:
                if any(op in col_where.lower() for op in ['=', '<', '>', ' in ', '(']):
                    query = f'SELECT * FROM {tbl} WHERE {col_where}'
                else:
                    query = f'SELECT {col_where} FROM {tbl}'
            else:
                query = f'SELECT {col_where} FROM {tbl} WHERE {where}'
            if limit:
                query += f' LIMIT {limit}'
            return query

        try: # try to use it
            return pd.read_sql(build_query(table), engine)
        except Exception as e: # if it failed then try to look for similar table names and use those
            inspector = inspect(engine)
            all_tables = inspector.get_table_names()
            closest = difflib.get_close_matches(table, all_tables, n=1)
            if closest:
                print(f"Warning: Table '{table}' not found. Using closest match: '{closest[0]}'")
                return pd.read_sql(build_query(closest[0]), engine)
            else:
                raise ValueError(f"Table '{table}' not found. Available tables: {all_tables}") from e
