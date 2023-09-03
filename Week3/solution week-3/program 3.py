import sqlite3
conn=sqlite3.connect("c:/Sqlite/ESM.db")
cur=conn.cursor()
query="update Employee\
            set basic=basic+(basic*10)/100\
            where branch like 'Surat'"
cur.execute(query)
conn.commit()
conn.close()
