from fastapi import FastAPI
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

@app.get("/get-by-Name")
def get_student(Name: str):
    for student_id in students:
        if students[student_id]["Name"] == Name:
            return students[student_id]
    return { " Data ": "Not Found"}