from fastapi import FastAPI,status,HTTPException

app = FastAPI()

@app.post("/users" , status_code= status.HTTP_201_CREATED)
def create_user():
    return{
        "data" : "User created"
    }

@app.get("/users",status_code=status.HTTP_200_OK)
def get_user():
    return{
        "status" : "success",
        "message" : "data fetched",
        "data":{
            "name" : "sabin",
            "age": 21
        }
    }

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id !=1:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return{
        "id" : 1,
        "name" : "sabin"
    }