from _user_db import connect_database,create_dbtable
import sqlite3
import os
from prettytable import PrettyTable
def store_password(website,url,username,email,password,description):
    conn = connect_database() 
    myCur = conn.cursor()

    myCur.execute(f'''insert into UserDataBase values ("{website}","{url}","{username}","{email}","{password}","{description}");''')
    conn.commit()
    conn.close()
