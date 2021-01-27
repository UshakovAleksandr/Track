import sqlite3

"""
Инициализирующий файл.
Так же, здесь исполняется инструкции по созданию БД и таблицы.
"""

conn = sqlite3.connect("tracker.db")
cur = conn.cursor()

QUERY_CREATE = "CREATE TABLE IF NOT EXISTS current_tasks (date TEXT, event TEXT, status TEXT)"
cur.execute(QUERY_CREATE)
conn.commit()

cur.close()
conn.close()
