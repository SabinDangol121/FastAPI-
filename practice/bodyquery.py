from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name : str
    age : int

@app.post("/users")
def create_users(user : User):
    users.append(user) # yesma user's value from the parameter is assigned to users like a container
    return{
        "users" : "User created",
        "data" : user
    }

@app.put("/users/{user_id}")
def update_users(user_id : int , user : User ,notify : bool = False ):
    if user_id < len(users):
        users[user_id] = user
        return{
            "users" : "user updated",
            "notify" : notify,
            "data" : user
        }
    return{"error" : "user not found"} 

@app.get('/users')
def get_users():
    return users