from fastapi import FastAPI, Query, Path
from typing import Annotated




app = FastAPI()

students= {
    1:{
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}

@app.get("/get-student/{student_id}")
def get_student(student_id: Annotated[int, Path(description="the id student you want to wiew", ge=0)]):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name=None):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return { "Data": "Not found"}