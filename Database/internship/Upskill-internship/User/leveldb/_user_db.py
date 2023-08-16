import sqlite3
import os

def create_dbtable():
    conn = sqlite3.connect("user.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS UserDataBase(
                Website     CHAR(50),
                URL         TEXT(500),
                Username    Char(50),
                Email       TEXT(100),
                Password    TEXT(100),
                Description TEXT(5000));''')
    conn.commit()
    conn.close()
def create_datbase():
    if os.path.exists(r"User/leveldb/user.db"):
        if not os.path.exists(r"User/leveldb/user.db"):
            create_dbtable()
        else:
            os.mkdir(r"User/leveldb")
            create_dbtable()