# Student Management & Result System
A command-line student management system built with Python and SQLite.

## Features
- Student records (add, list)
- Course management
- Enrollment linking students to courses (many-to-many)
- Grade entry with automatic credit-weighted GPA calculation
- Attendance tracking with risk analysis (safe skips / required attendance to hit the minimum %)
- Top students report

## Structure
- `db.py` — database connection and schema
- `students.py`, `courses.py`, `enrollments.py` — core record management
- `grades.py` — GPA calculation
- `attendance.py` — attendance risk math
- `reports.py` — cross-student reports
- `main.py` — the menu-driven entry point

## Run it
```bash
python main.py
