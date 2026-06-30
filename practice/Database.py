import sqlite3
from fastapi import FastAPI

app= FastAPI()

conn = sqlite3.connect("practicedb.db" , check_same_thread=False)

cursur = conn.cursor()

cursur.execute("""
CREATE TABLE IF NOT EXISTS Todos(
               id INTEGER PRIMARY KEY,
               name TEXT,
               completed TEXT
               )
""")

conn.commit()

@app.get("/")
def home():
    return{
        "message" : "SQL created successfully"
    }
