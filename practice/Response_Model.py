from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name : str
    age : int
    password : str

class Response_user(BaseModel):
    name : str
    age : int

@app.get("/user", response_model = Response_user)
def get_user():
    return{
        "name" : "sabin",
        "age"  :20,
        "password" : "123456"
    }