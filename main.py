from db import get_db, Base, engine, init_db
from managers import StudentManager, CourseManager, EnrollmentManager
from sqlalchemy.orm import Session
import sys

# init_db is now imported from db

def main_menu():
    print("\n--- Smart Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Add Course")
    print("6. View All Courses")
    print("7. Delete Course")
    print("8. Enroll Student in Course")
    print("9. View Student Enrollments")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_student_ui(sm: StudentManager):
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    age = int(input("Enter Age: "))
    try:
        student = sm.add_student(name, email, age)
        print(f"Student '{student.name}' added successfully (ID: {student.id}).")
    except Exception as e:
        print(f"Error adding student: {e}")

def view_students_ui(sm: StudentManager):
    students = sm.get_all_students()
    if not students:
        print("No students found.")
    for s in students:
        print(f"ID: {s.id}, Name: {s.name}, Email: {s.email}, Age: {s.age}")

def update_student_ui(sm: StudentManager):
    sid = int(input("Enter Student ID to update: "))
    name = input("Enter New Name (leave blank to keep current): ") or None
    email = input("Enter New Email (leave blank to keep current): ") or None
    age_str = input("Enter New Age (leave blank to keep current): ")
    age = int(age_str) if age_str else None
    
    updated = sm.update_student(sid, name, email, age)
    if updated:
        print("Student updated successfully.")
    else:
        print("Student not found.")

def delete_student_ui(sm: StudentManager):
    sid = int(input("Enter Student ID to delete: "))
    if sm.delete_student(sid):
        print("Student deleted.")
    else:
        print("Student not found.")

def add_course_ui(cm: CourseManager):
    name = input("Enter Course Name: ")
    code = input("Enter Course Code: ")
    try:
        course = cm.add_course(name, code)
        print(f"Course '{course.name}' added successfully (ID: {course.id}).")
    except Exception as e:
        print(f"Error adding course: {e}")

def view_courses_ui(cm: CourseManager):
    courses = cm.get_all_courses()
    if not courses:
        print("No courses found.")
    for c in courses:
        print(f"ID: {c.id}, Name: {c.name}, Code: {c.code}")

def delete_course_ui(cm: CourseManager):
    cid = int(input("Enter Course ID to delete: "))
    if cm.delete_course(cid):
        print("Course deleted.")
    else:
        print("Course not found.")

def enroll_student_ui(em: EnrollmentManager):
    sid = int(input("Enter Student ID: "))
    cid = int(input("Enter Course ID: "))
    grade = input("Enter Grade (optional, press Enter to skip): ") or None
    try:
        enrollment = em.enroll_student(sid, cid, grade)
        print(f"Student {sid} enrolled in Course {cid} successfully.")
    except Exception as e:
        print(f"Error enrolling student: {e}")

def view_enrollments_ui(em: EnrollmentManager):
    sid = int(input("Enter Student ID: "))
    enrollments = em.get_enrollments_for_student(sid)
    if not enrollments:
        print("No enrollments found for this student.")
    else:
        for e in enrollments:
            print(f"Course ID: {e.course_id}, Code: {e.course.code}, Name: {e.course.name}, Grade: {e.grade}, Date: {e.enrollment_date}")

def main():
    init_db()
    db = next(get_db())
    sm = StudentManager(db)
    cm = CourseManager(db)
    em = EnrollmentManager(db)

    while True:
        choice = main_menu()
        if choice == '1':
            add_student_ui(sm)
        elif choice == '2':
            view_students_ui(sm)
        elif choice == '3':
            update_student_ui(sm)
        elif choice == '4':
            delete_student_ui(sm)
        elif choice == '5':
            add_course_ui(cm)
        elif choice == '6':
            view_courses_ui(cm)
        elif choice == '7':
            delete_course_ui(cm)
        elif choice == '8':
            enroll_student_ui(em)
        elif choice == '9':
            view_enrollments_ui(em)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
