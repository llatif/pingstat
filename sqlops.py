import sqlite3

from sqlite3 import Error
from sqlite3.dbapi2 import SQLITE_CREATE_TABLE

def createSqlLiteDb():
# Creates a SQLite3 database in memory

    conn = None;
    fileDbSchema = ''' CREATE TABLE IF NOT EXISTS latency (
                    id integer PRIMARY KEY,
                    source text NOT NULL,
                    destination text NOT NULL,
                    latency int NOT NULL
                 ); '''
    
    insertTestData = '''INSERT INTO latency(
                        source, destination, latency)
                        VALUES('192.168.0.1', '192.168.1.1', 2),
                        ('192.168.0.1', '192.168.1.2', 4);
                      '''
    try:

        conn = sqlite3.connect(':memory:')
        print("SQLite database created")
        
        cursor = conn.cursor()
        cursor.execute(fileDbSchema)

        cursor.execute (insertTestData)
        conn.commit()
        print("Database created\nInserted values into database")
    
        cursor.execute('''SELECT * FROM latency''')
        result = cursor.fetchall();
        print(result)
    
    except Error as e:

        print(e)
    
    finally:
        
        if conn:
            conn.close()