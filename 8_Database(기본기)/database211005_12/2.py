import sqlite3
con = sqlite3.connect('topics.db')
result = con.execute('SELECT*FROM topic')
abc = result.fetchall()
print(abc)