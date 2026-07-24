from db import get_connection
from grades import calculate_gpa

def top_students(n=5):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM students")
    students = cur.fetchall()
    conn.close()

    scored = []
    for sid, name in students:
        gpa = calculate_gpa(sid)
        if gpa is not None:
            scored.append((name, gpa))

    scored.sort(key=lambda x: x[1], reverse=True)
    for name, gpa in scored[:n]:
        print(f"{name}: GPA {gpa}")
