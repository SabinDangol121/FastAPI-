from fastapi import FastAPI, Depends, HTTPException, Header
from jose import jwt
from datetime import datetime, timedelta , timezone

app = FastAPI()

SECRET_KEY = "mysecretkey"

ALGORTHM = "HS256"

def create_token(data : dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORTHM)

    return token

#login token API
@app.post("/login")
def login_page(username:str , password:str):
    if username != "admin" or password != "12345":
        raise HTTPException(
            status_code=301,
            detail="invalid username or password"
        )
    
    token = create_token({
        "sub" : username
    })
    return{
        "access_token" : token
    }

#token verify
def verify(token : str = Header(None)):

    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORTHM)
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
    
#protected route
@app.get("/secure")
def secure_data(user = Depends(verify)):
    return{
        "message":"securedata accessed",
        "user":user
    }
