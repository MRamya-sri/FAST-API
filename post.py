from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

Students={
    1: {
        "Name": "Ramya",
        "age" : 22,
        "classs": "Grad"
    },
    2: {
        "Name": "Gracie",
        "age": 29,
        "classs":"postGrad"        
    } ,
    3 :{
        "Name": "Taylor",
        "age": 34,
        "classs":"phD" 
    }
}

class Student( BaseModel):
    Name: str
    age: int
    classs: str


@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in Students:
        return { "error": "student_exists"}
    Students[student_id] = student
    return Students[student_id]

