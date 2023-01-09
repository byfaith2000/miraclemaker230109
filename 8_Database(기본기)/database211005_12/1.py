import sqlite3
con = sqlite3.connect('topics.db')
title = input('제목 : ')
body = input('본문 : ')
author_id = input('저자id : ')
sql = "INSERT INTO topic(title, body, author_id) VALUES('"+title+"','"+body+"', '"+author_id+"')"
con.execute(sql)
con.commit()
con.close()


