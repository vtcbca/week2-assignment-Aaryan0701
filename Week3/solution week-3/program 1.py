import sqlite3
conn=sqlite3.connect("c:/Sqlite/ESM.db")
cur=conn.cursor()
table="""create table Employee
              (
                  eid integer primary key,
                  ename text,
                  dept text,
                  basic interger,
                  branch text
              );"""
cur.execute(table)
conn.commit()
conn.cursor()
