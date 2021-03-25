import sqlite3
import pandas

con = sqlite3.connect('db.sqlite')
cur = con.cursor()
for row in cur.execute('SELECT * FROM user;'):
    print(row)

con.close()