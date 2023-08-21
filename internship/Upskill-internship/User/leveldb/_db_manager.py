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

def update_password(website,new_password):
    conn = connect_database()  
    myCur = conn.cursor()

    sqlQuery = f'''update UserDataBase set Password = "{new_password}" where Website = "{website}"'''

    myCur.execute(sqlQuery)
    conn.commit()
    conn.close()

def show_deatails():
    conn=connect_database()
    myCur = conn.cursor()

    sqlQuery= "SELECT * FROM UserDataBase"
    myCur.execute(sqlQuery)
    data = myCur.fetchall()
    return data

if not os.path.exists('user.db'):
    create_dbtable()

myTable1 = PrettyTable(["Website","URL","Username","Email","Password","Description"])
myTable2 = PrettyTable(["Website","URL","Username","Email","Password","Description"])
  
# Add rows to Database

store_password( "instagram", "insta.com", "hamsa","ham","pass","private acc")
store_password( "facebook", "insta.com", "hamsa","ham","pass","private acc")
store_password( "twitter", "insta.com", "hamsa","ham","pass","private acc")
store_password( "thread", "insta.com", "hamsa","ham","pass","private acc")
store_password( "snap", "insta.com", "hamsa","ham","pass","private acc")
store_password( "insram", "insta.com", "hamsa","ham","pass","private acc")
store_password( "tagram", "insta.com", "hamsa","ham","pass","private acc")
  
data = show_deatails()
for row in data:
    myTable1.add_row(list(row))

print(myTable1)
print('\n\n')

update_password('instagram','kolitandu')

data = show_deatails()
for row in data:
    myTable2.add_row(list(row))
print(myTable2)