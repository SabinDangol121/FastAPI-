from fastapi import FastAPI, Depends, HTTPException
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta , timezone
from passlib.context import CryptContext

app = FastAPI()

#jwt config
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30