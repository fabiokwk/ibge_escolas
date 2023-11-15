import csv
import sqlite3

con = sqlite3.connect('dsbd.db')
cur = con.cursor()

cur.execute("SELECT * FROM censo")
result = cur.fetchall()
print(result[0:6])
print(len(result))
con.commit()  