from db import get_connection

def marks_to_grade_point(marks):
    if marks >= 90: return 10
    if marks >= 80: return 9
    if marks >= 70: return 8
    if marks >= 60: return 7
    if marks >= 50: return 6
    if marks >= 40: return 5
    return 0

def add_grade(enrollment_id, marks):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO grades (enrollment_id, marks) VALUES (?, ?)
        ON CONFLICT(enrollment_id) DO UPDATE SET marks = excluded.marks
    """, (enrollment_id, marks))
    conn.commit()
    conn.close()
    print(f"Recorded marks: {marks} -> grade point {marks_to_grade_point(marks)}")

def calculate_gpa(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT g.marks, c.credits
        FROM grades g
        JOIN enrollments e ON g.enrollment_id = e.id
        JOIN courses c ON e.course_id = c.id
        WHERE e.student_id = ?
    """, (student_id,))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        return None

    total_points = 0
    total_credits = 0
    for marks, credits in rows:
        gp = marks_to_grade_point(marks)
        total_points += gp * credits
        total_credits += credits

    return round(total_points / total_credits, 2) if total_credits else None
