import sqlite3

from sqlite3 import Error
from sqlite3.dbapi2 import SQLITE_CREATE_TABLE

dbPath = "ping.db"

def createSqlLiteDb():
# Creates a SQLite3 database in memory

    conn = None;
    fileDbSchema = ''' CREATE TABLE IF NOT EXISTS latency (
                    id integer PRIMARY KEY,
                    source text NOT NULL,
                    destination text NOT NULL,
                    latency int NOT NULL
                 ); '''
    
    try:

        conn = sqlite3.connect(dbPath)
        
        cursor = conn.cursor()
        cursor.execute(fileDbSchema)
        conn.commit()
        print("Database and tables\n")
    
    except Error as e:

        print(e)
    
    finally:
        
        if conn:
            conn.close()

def insertTestData():
# Inserts test data into SQLite database
    
    insertTestData = ''' INSERT INTO latency(
                        source, destination, latency)
                        VALUES('192.168.0.1', '192.168.1.1', 2),
                        ('192.168.0.1', '192.168.1.2', 4);
                     '''

    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute (insertTestData)
    conn.commit()
    print("Inserted values into database")

    conn.close()

def readTableData():

    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM latency''')
    result = cursor.fetchall();
    print(result)