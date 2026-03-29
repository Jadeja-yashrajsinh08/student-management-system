from connection import get_connection
def create_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        course TEXT,
        marks1 INTEGER,
        marks2 INTEGER,
        marks3 INTEGER,
        total INTEGER,
        percentage REAL
    )
    """)

    #user table

    cursor.execute("""
    CREATE  TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
        )
    """)

    conn.commit()
    conn.close()