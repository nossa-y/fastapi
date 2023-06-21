from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from pydantic import EmailStr
from typing import Annotated

app = FastAPI()

#recupere tous les numeros de telephone d'un répertoire pour 
#repertorier combien y'a de 06, 01 etc

inter = {
    1: {
        "name": "john",
        "phone_number": 112345678,
        "city": "toulouse"
    },
    2: {
        "name": "manon",
        "phone_number": 198765432,
        "city": "paris"
    },
    3: {
        "name": "pierre",
        "phone_number": 698765432,
        "city": "marseille"
    }
}

departement = {
    1:{0},
    2:{0},
    3:{0},
    4:{0},
    5:{0},
    6:{0},
    7:{0},
    8:{0},
    9:{0}
}

class directory():
    name : str
    phone_number : int
    city : str

@app.get("/numero")
def show_number():
    repertoire=[]
    for i in range (0,10):
        departement[i]=0
    for personne in inter:
        repertoire.append(inter[personne]["phone_number"])
        for i in departement:
            if int(inter[personne]["phone_number"]/100000000)==i:
                departement[i]+=1
    return {{"il y a": f"{departement[1]}, 01" },{"il y a": f"{departement[2]}, 02" },{"il y a": f"{departement[3]}, 03" },{"il y a": f"{departement[4]}, 04" },{"il y a": f"{departement[5]}, 05" },{"il y a": f"{departement[6]}, 06" },{"il y a": f"{departement[7]}, 07" },{"il y a": f"{departement[8]}, 08" },{"il y a": f"{departement[9]}, 09" },

