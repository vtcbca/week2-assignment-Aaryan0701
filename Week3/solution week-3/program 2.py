import sqlite3
conn=sqlite3.connect("c:/Sqlite/ESM.db")
cur=conn.cursor()
"""
Records insert directly:
1|Aryan|IT|8000|Vyara
2|Param|HR|8000|Surat
3|Meet|Account|7000|Surat
4|Parth|Inventory|6000|Mota
5|Mann|HR|7000|Bardoli
"""
#Record insert using tuple
data=[(6,'Sujal','Account',5500,'Isorli'),
          (7,'Harsh','Inventory',5500,'Bardoli'),
          (8,'Dhruv','IT',7000,'Songadh'),
          (9,'Kavi','Account',6000,'Bardoli'),
          (10,'Akshar','HR',7000,'Palsana')]
cur.executemany("insert into Employee values(?,?,?,?,?)",data)
#Record insert from user
lis=[]
for i in range(5):
    eid=int(input('Enter eid:'))
    ename=input('Enter name:')
    dept=input('Enter dept:')
    basic=int(input('Enter basic:'))
    branch=input('Enter branch:')
    d=(eid,ename,dept,basic,branch)
    lis.append(d)
cur.executemany("insert into values(?,?,?,?,?)",lis)
conn.commit()
conn.close()
