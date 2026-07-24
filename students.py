import sqlite3
from db import get_connection
def add_student(name, roll_number, email=""):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO students (name, roll_number, email) VALUES (?, ?, ?)",
            (name, roll_number, email)
        )
        conn.commit()
        print(f"Added student: {name} ({roll_number})")
    except sqlite3.IntegrityError:
        print("Error: roll number already exists.")
    conn.close()

def list_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, roll_number, email FROM students")
    rows = cur.fetchall()
    conn.close()
    if not rows:
        print("No students yet.")
        return
    for r in rows:
        print(f"{r[0]:>3} | {r[1]:<20} | {r[2]:<12} | {r[3]}")

def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted.")
