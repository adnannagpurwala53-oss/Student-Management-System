from db import get_connection

def enroll_student(student_id, course_id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
            (student_id, course_id)
        )
        conn.commit()
        print("Enrolled.")
    except Exception as e:
        print("Error enrolling (maybe already enrolled?):", e)
    conn.close()

def list_enrollments_for_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT e.id, c.code, c.name
        FROM enrollments e
        JOIN courses c ON e.course_id = c.id
        WHERE e.student_id = ?
    """, (student_id,))
    rows = cur.fetchall()
    conn.close()
    return rows
