from fastapi import FastAPI , HTTPException , Request 
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name):
        self.name = name


@app.get("/users/{name}")
def get_user(name : str):
    if name!="sabin":
        raise UserNotFoundException(name)
    
    return{
        "name" :name
    }

@app.exception_handler(UserNotFoundException)
def user_Not_Found_exception_handler(request:Request, exc :UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "message": f"User {exc.name} not found"
            }
    )

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return{
        "id":1,
        "name" : "sabin"
    }
