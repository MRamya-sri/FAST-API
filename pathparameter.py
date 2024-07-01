from fastapi import FastAPI, Path
app = FastAPI()

students={
    1: {
        "Name": "Ramya",
        "age" : 22,
        "class": "Grad"
    },
    2: {
        "Name": "Gracie",
        "age": 29,
        "class":"postGrad"        
    } ,
    3 :{
        "Name": "Taylor",
        "age": 34,
        "class":"phD" 
    }
}

@app.get("/get-Student/{student_id}")
def get_student(student_id: int = Path(description="ID of the student you want to view..", gt=0, lt=4)):
    return students[student_id]