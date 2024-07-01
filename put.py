from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

Students = {
    1: {
        "Name": "Ramya",
        "age": 22,
        "classs": "Grad"
    },
    2: {
        "Name": "Gracie",
        "age": 29,
        "classs": "postGrad"
    },
    3: {
        "Name": "Taylor",
        "age": 34,
        "classs": "phD"
    }
}

class UpdateStudent(BaseModel):
    Name: Optional[str] = None
    age: Optional[int] = None
    classs: Optional[str] = None

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in Students:
        return {"Error": "Student does not exist"}
    
    if student.Name is not None:
        Students[student_id]["Name"] = student.Name

    if student.age is not None:
        Students[student_id]["age"] = student.age

    if student.classs is not None:
        Students[student_id]["classs"] = student.classs

    return Students[student_id]

      





