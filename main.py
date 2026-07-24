from db import create_tables
import students
import courses
import enrollments
import grades
import attendance
import reports

def main_menu():
    create_tables()
    while True:
        print("\n=== Student Management System ===")
        print("1. Add student")
        print("2. List students")
        print("3. Add course")
        print("4. List courses")
        print("5. Enroll student in course")
        print("6. Add/update grade")
        print("7. Calculate GPA")
        print("8. Record attendance")
        print("9. Attendance risk report")
        print("10. Top students")
        print("11. View a student's enrollments")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Name: ")
            roll = input("Roll number: ")
            email = input("Email (optional): ")
            students.add_student(name, roll, email)

        elif choice == "2":
            students.list_students()

        elif choice == "3":
            code = input("Course code: ")
            name = input("Course name: ")
            credits = int(input("Credits: "))
            courses.add_course(code, name, credits)

        elif choice == "4":
            courses.list_courses()

        elif choice == "5":
            sid = int(input("Student ID: "))
            cid = int(input("Course ID: "))
            enrollments.enroll_student(sid, cid)

        elif choice == "6":
            eid = int(input("Enrollment ID: "))
            marks = float(input("Marks (0-100): "))
            grades.add_grade(eid, marks)

        elif choice == "7":
            sid = int(input("Student ID: "))
            gpa = grades.calculate_gpa(sid)
            print(f"GPA: {gpa}" if gpa is not None else "No grades recorded yet.")

        elif choice == "8":
            eid = int(input("Enrollment ID: "))
            total = int(input("Total classes held: "))
            attended = int(input("Classes attended: "))
            threshold = float(input("Minimum % required (default 75): ") or 75)
            attendance.record_attendance(eid, total, attended, threshold)

        elif choice == "9":
            attendance.attendance_risk_report()

        elif choice == "10":
            reports.top_students()

        elif choice == "11":
            sid = int(input("Student ID: "))
            rows = enrollments.list_enrollments_for_student(sid)
            for eid, code, name in rows:
                print(f"Enrollment ID {eid}: {code} - {name}")

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
