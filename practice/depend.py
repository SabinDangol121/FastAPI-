from fastapi import FastAPI, Depends, Header ,HTTPException

app = FastAPI()

# def commom_logic():
#     return {
#         "message": "commom logic is executed!"
#     }

# @app.get("/")
# def home(data = Depends(commom_logic)):
#     return data


def verify_token(token : str = Header(None)):
    if token != "secrettoken":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return{
        "msessage":"Authorized"
    }

@app.get("/")
def secure(user = Depends(verify_token)):
    return{
        "message" : "secured data accessed succesfully",
        "user" : user
    }
