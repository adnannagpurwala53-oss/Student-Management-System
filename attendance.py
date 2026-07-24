from db import get_connection

def record_attendance(enrollment_id, total_classes, attended_classes, min_percent=75):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO attendance (enrollment_id, total_classes, attended_classes, min_percent_required)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(enrollment_id) DO UPDATE SET
            total_classes = excluded.total_classes,
            attended_classes = excluded.attended_classes,
            min_percent_required = excluded.min_percent_required
    """, (enrollment_id, total_classes, attended_classes, min_percent))
    conn.commit()
    conn.close()
    print("Attendance recorded.")

def attendance_risk_report():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT s.name, c.name, a.attended_classes, a.total_classes, a.min_percent_required
        FROM attendance a
        JOIN enrollments e ON a.enrollment_id = e.id
        JOIN students s ON e.student_id = s.id
        JOIN courses c ON e.course_id = c.id
    """)
    rows = cur.fetchall()
    conn.close()

    for student_name, course_name, attended, total, threshold in rows:
        if total == 0:
            continue
        pct = round(100 * attended / total, 2)
        if pct >= threshold:
            safe_skips = int((attended * 100 - threshold * total) / threshold)
            print(f"{student_name} | {course_name} | {pct}% | can skip {safe_skips} more")
        else:
            needed = int((threshold * total - attended * 100) / (100 - threshold)) + 1
            print(f"{student_name} | {course_name} | {pct}% | must attend next {needed} in a row")
