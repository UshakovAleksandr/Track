import pytest
import sqlite3


@pytest.fixture()
def db_connection():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    QUERY_CREATE = "CREATE TABLE IF NOT EXISTS current_tasks (date TEXT, event TEXT, status TEXT)"
    cur.execute(QUERY_CREATE)
    conn.commit()

    cur.close()

    yield conn

    conn.close()
