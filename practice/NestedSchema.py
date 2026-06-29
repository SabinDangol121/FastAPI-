from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Name(BaseModel):
    fname : str
    lname : str

class User(BaseModel):
    name : Name
    age :  int 
    phone_no : int 


@app.post("/user")
def create_user(user :User):
    return user



