from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from db import get_db, init_db
from managers import StudentManager, CourseManager, EnrollmentManager
from models import Student as StudentModel, Course as CourseModel, Enrollment as EnrollmentModel

app = FastAPI(title="Smart Student Management System API")

# Initialize database
init_db()

# Pydantic models for request/response bodies
class StudentCreate(BaseModel):
    name: str
    email: str
    age: int

class Student(StudentCreate):
    id: int
    class Config:
        from_attributes = True

class StudentUpdate(BaseModel):
    name: str = None
    email: str = None
    age: int = None

class CourseCreate(BaseModel):
    name: str
    code: str

class Course(CourseCreate):
    id: int
    class Config:
        from_attributes = True

class CourseUpdate(BaseModel):
    name: str = None
    code: str = None

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
    grade: str = None

# Endpoints
@app.get("/students", response_model=List[Student])
def get_students(db: Session = Depends(get_db)):
    sm = StudentManager(db)
    return sm.get_all_students()

@app.post("/students", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    sm = StudentManager(db)
    try:
        return sm.add_student(student.name, student.email, student.age)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    sm = StudentManager(db)
    res = sm.update_student(student_id, student.name, student.email, student.age)
    if not res:
        raise HTTPException(status_code=404, detail="Student not found")
    return res

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    sm = StudentManager(db)
    if sm.delete_student(student_id):
        return {"message": "Deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")

@app.get("/courses", response_model=List[Course])
def get_courses(db: Session = Depends(get_db)):
    cm = CourseManager(db)
    return cm.get_all_courses()

@app.post("/courses", response_model=Course)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    cm = CourseManager(db)
    try:
        return cm.add_course(course.name, course.code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/courses/{course_id}", response_model=Course)
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    cm = CourseManager(db)
    res = cm.update_course(course_id, course.name, course.code)
    if not res:
        raise HTTPException(status_code=404, detail="Course not found")
    return res

@app.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    cm = CourseManager(db)
    if cm.delete_course(course_id):
        return {"message": "Deleted successfully"}
    raise HTTPException(status_code=404, detail="Course not found")

@app.post("/enroll")
def enroll_student(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    em = EnrollmentManager(db)
    try:
        res = em.enroll_student(enrollment.student_id, enrollment.course_id, enrollment.grade)
        return {"message": "Success", "enrollment_id": res.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/students/{student_id}/enrollments")
def get_student_enrollments(student_id: int, db: Session = Depends(get_db)):
    em = EnrollmentManager(db)
    enrollments = em.get_enrollments_for_student(student_id)
    return [{"course_name": e.course.name, "course_code": e.course.code, "grade": e.grade, "date": e.enrollment_date} for e in enrollments]

# Serve static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
