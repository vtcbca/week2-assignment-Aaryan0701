import sqlite3
conn=sqlite3.connect("c:/Sqlite/ESM.db")
cur=conn.cursor()
query="select * from Employee\
            group by dept\
            having dept like 'Account' or dept like 'Inventory'"
cur.execute(query)
r=cur.fetchall()
for i in r:
    print(i)
conn.commit()
conn.close()
