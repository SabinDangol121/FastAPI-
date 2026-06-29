from fastapi import FastAPI
from pydantic  import BaseModel
# pydantic is the structured form of validating a data.  

app = FastAPI()

@app.get("/")
def home():
    return {"This is home page!"}

# @app.post("/createuser")
# def create_user(user_id:User):
#     return{
#         "message" :  "User Created",
#         "data" :
#             user_id
#     }


class Address(BaseModel):
    place : str
    portal : int

class User(BaseModel):
    name :  str
    age : int
    address : Address

@app.post("/createUser")
def create_user(user : User):
    return user
