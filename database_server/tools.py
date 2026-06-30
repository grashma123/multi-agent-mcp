import sqlite3

DB_NAME = "sample.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """)

    conn.commit()
    conn.close()

    return {"message": "Table created successfully"}


def insert_student(name, age):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        (name, age)
    )

    conn.commit()
    conn.close()

    return {"message": "Student added successfully"}


def list_students():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return {"students": students}