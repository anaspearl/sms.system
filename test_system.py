import os
from db import init_db, get_db, Base, engine
from managers import StudentManager, CourseManager, EnrollmentManager
from models import Student, Course, Enrollment

# Clean up existing database
if os.path.exists("student_management.db"):
    os.remove("student_management.db")

# Initialize DB
Base.metadata.create_all(bind=engine)
db = next(get_db())

print("Testing Student Management System...")

# 1. Add Student
sm = StudentManager(db)
student = sm.add_student("John Doe", "john@example.com", 20)
assert student.id is not None
assert student.name == "John Doe"
print("PASS: Add Student")

# 2. Add Course
cm = CourseManager(db)
course = cm.add_course("Computer Science 101", "CS101")
assert course.id is not None
assert course.code == "CS101"
print("PASS: Add Course")

# 3. Enroll Student
em = EnrollmentManager(db)
enrollment = em.enroll_student(student.id, course.id, "A")
assert enrollment.id is not None
assert enrollment.student_id == student.id
assert enrollment.course_id == course.id
print("PASS: Enroll Student")

# 4. Verify Relationships
# Re-query to ensure relationships are loaded
student_from_db = sm.get_student(student.id)
assert len(student_from_db.enrollments) == 1
assert student_from_db.enrollments[0].course.code == "CS101"
print("PASS: Verify Relationships")

# 5. Business Logic Checks
# Try to enroll same student in same course (should return existing)
enrollment2 = em.enroll_student(student.id, course.id)
assert enrollment2.id == enrollment.id
print("PASS: Duplicate Enrollment Check")

# 6. Delete Student
# Provide valid arguments for delete_student
# Assuming delete_student takes student_id as argument based on managers.py implementation
# Let's double check managers.py content first if needed, but based on my implementation it was delete_student(student_id)
is_deleted = sm.delete_student(student.id)
assert is_deleted is True
assert sm.get_student(student.id) is None
# Verify cascading delete (enrollments should be gone)
# Note: In SQLite, foreign key constraints are disabled by default. 
# SQLAlchemy handles cascade delete if configured in relationship options.
# Our models have cascade="all, delete-orphan", so SQLAlchemy should handle it on the object side 
# if the session is managed correctly, or if we ensure FK support is on.
# But simply checking if the enrollment exists via query is good enough.
existing_enrollment = db.query(Enrollment).filter_by(id=enrollment.id).first()
assert existing_enrollment is None
print("PASS: Delete Student & Cascade")

print("\nAll automated tests passed successfully!")
