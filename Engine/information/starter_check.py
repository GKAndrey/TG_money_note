import json
import os
import sqlite3

PATH = os.path.abspath(__file__ + '/../..')
js_path = os.path.join(PATH, 'information', 'token.json')

try:
    with open(js_path, 'r') as file:
        TOKEN_TG = json.load(file)
except:
    TOKEN_TG = input('Print bot TOKEN \n')
    with open(js_path, 'w') as file:
        json.dump(TOKEN_TG, file)


def cret_bd():
    conn = sqlite3.connect(os.path.join(PATH, 'information', 'db.db'))
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS dolg(
                    id int NOT NULL, 
                    num int NOT NULL,
                    time str NOT NULL)''')
    conn.commit()
    conn.close()

cret_bd()

def insert_num(time:str, id:int = 1, num:int = 2):
    conn = sqlite3.connect(os.path.join(PATH, 'information', 'db.db'))
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO dolg(id, num, time) VALUES(?, ?, ?)''', (id, num, time))
    conn.commit()
    conn.close()

conn = sqlite3.connect(os.path.join(PATH, 'information', 'db.db'))
cursor = conn.cursor()
cursor.execute('''SELECT * FROM dolg''')
db_info = cursor.fetchall()
conn.close()
# print(db_info, num_info)
# cursor.execute("INSERT INTO dolg (id) VALUES (?)", (1,))
# conn.commit()