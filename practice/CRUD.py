from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []


class TODO(BaseModel):
    id : int
    name  : str
    status : bool


@app.post("/todos" )
def Create_todo(todo : TODO):
    todos.append(todo)
    return todo

@app.get("/todos")
def Get_Todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id : int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error" : "Todo not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id : int,updated_todo : TODO):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
            "messasge" : "todo updated",
            "data"  : updated_todo
            }
    return {"error" : "todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id : int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted_todo = todos.pop(index)
            return {
                "message" : "todo deleted",
                "data" : deleted_todo
            }
    return {"error" : "todo not found"}



