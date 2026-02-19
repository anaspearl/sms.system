from sqlalchemy.orm import Session
from models import Student, Course, Enrollment  # Corrected import
from datetime import date as dt

class StudentManager:
    def __init__(self, db: Session):
        self.db = db

    def add_student(self, name: str, email: str, age: int) -> Student:
        student = Student(name=name, email=email, age=age)
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)
        return student

    def get_student(self, student_id: int) -> Student:
        return self.db.query(Student).filter(Student.id == student_id).first()

    def get_all_students(self):
        return self.db.query(Student).all()

    def update_student(self, student_id: int, name: str = None, email: str = None, age: int = None) -> Student:
        student = self.get_student(student_id)
        if student:
            if name: student.name = name
            if email: student.email = email
            if age: student.age = age
            self.db.commit()
            self.db.refresh(student)
        return student

    def delete_student(self, student_id: int) -> bool:
        student = self.get_student(student_id)
        if student:
            self.db.delete(student)
            self.db.commit()
            return True
        return False

class CourseManager:
    def __init__(self, db: Session):
        self.db = db

    def add_course(self, name: str, code: str) -> Course:
        course = Course(name=name, code=code)
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)
        return course

    def get_course(self, course_id: int) -> Course:
        return self.db.query(Course).filter(Course.id == course_id).first()

    def get_all_courses(self):
        return self.db.query(Course).all()
        
    def delete_course(self, course_id: int) -> bool:
        course = self.get_course(course_id)
        if course:
            self.db.delete(course)
            self.db.commit()
            return True
        return False

    def update_course(self, course_id: int, name: str = None, code: str = None) -> Course:
        course = self.get_course(course_id)
        if course:
            if name: course.name = name
            if code: course.code = code
            self.db.commit()
            self.db.refresh(course)
        return course

class EnrollmentManager:
    def __init__(self, db: Session):
        self.db = db

    def enroll_student(self, student_id: int, course_id: int, grade: str = None) -> Enrollment:
        # Check if already enrolled
        existing = self.db.query(Enrollment).filter_by(student_id=student_id, course_id=course_id).first()
        if existing:
            return existing
            
        enrollment = Enrollment(student_id=student_id, course_id=course_id, enrollment_date=dt.today(), grade=grade)
        self.db.add(enrollment)
        self.db.commit()
        self.db.refresh(enrollment)
        return enrollment

    def get_enrollments_for_student(self, student_id: int):
        return self.db.query(Enrollment).filter(Enrollment.student_id == student_id).all()

    def get_enrollments_for_course(self, course_id: int):
        return self.db.query(Enrollment).filter(Enrollment.course_id == course_id).all()
