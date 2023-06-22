from fastapi import FastAPI, Query, Path
from typing import Annotated
from pydantic import BaseModel




app = FastAPI()

students= {
    1:{
        "name": "john",
        "age": 17,
        "year": "year 12"
    }
}

class Student(BaseModel):
    name : str 
    age : int 
    year : str 

class UpdateStudent(BaseModel):
    name : str | None
    age : int | None
    year : str | None
              

@app.get("/get-student/{student_id}")
def get_student(student_id: Annotated[int, Path(description="the id student you want to wiew", ge=0)]):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(student_id : int , name: str=None):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return { "Data": "Not found"}

@app.post('/create-student/{student_id}')
def create_student(student_id : int, student : Student):
    if student_id in student:
        return {"Error" : f"student {student_id} already registered"}
    students.update({student_id:student})
    return students

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "student doesn't exist"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error" : "student not exist"}
    del students[student_id]
    return {"Message": "student deleted"}