import sqlite3
conn=sqlite3.connect("c:/Sqlite/ESM.db")
cur=conn.cursor()
query="select * from Employee\
            where basic>6000"
cur.execute(query)
r=cur.fetchall()
for i in r:
    print(i)
conn.commit()
conn.close()
