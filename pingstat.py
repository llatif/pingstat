import sqlite3

from sqlite3 import Error
from sqlite3.dbapi2 import SQLITE_CREATE_TABLE

def createSqlLiteDb():
# Creates a SQLite3 database in memory

    conn = None;
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
        print("SQLite database created")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def createTable():
# DB schema for files

  fileDbSchema = """ CREATE TABLE IF NOT EXISTS files (
                    id integer PRIMARY KEY,
                    path text NOT NULL,
                    filetype text NOT NULL
                 ); """

  create_table()