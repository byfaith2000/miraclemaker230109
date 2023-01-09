import sqlite3
con = sqlite3.connect('topics.db')
result = con.execute('SELECT * FROM author')
abc = result.fetchall()
print(abc)