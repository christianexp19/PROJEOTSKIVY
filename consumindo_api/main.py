
import sqlite3

con = sqlite3.connect("meubanco.db")

cur = con.cursor()
cur.execute("""
 CREATE TABLE IF NOT EXISTS usuarios(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT,
 email TEXT
 )
""")
con.commit()
