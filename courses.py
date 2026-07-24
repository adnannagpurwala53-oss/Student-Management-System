from db import get_connection

def add_course(code, name, credits=3):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO courses (code, name, credits) VALUES (?, ?, ?)",
            (code, name, credits)
        )
        conn.commit()
        print(f"Added course: {name} ({code})")
    except Exception as e:
        print("Error adding course:", e)
    conn.close()

def list_courses():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, code, name, credits FROM courses")
    rows = cur.fetchall()
    conn.close()
    for r in rows:
        print(f"{r[0]:>3} | {r[1]:<8} | {r[2]:<20} | {r[3]} credits")
