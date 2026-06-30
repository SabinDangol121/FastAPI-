from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from fastapi import FastAPI,Depends,HTTPException

app = FastAPI()

#Database url fetched
DATABASE_URL = "sqlite:///./practicedb.db"

# Db connection
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

# Session (for db operation)
sessionlocal = sessionmaker(bind=engine)

#base (fro model)
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    completed = Column(String)

# provides db session
Base.metadata.create_all(bind=engine)


#dependancy
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

# create api
@app.post("/todo")
def create_data(title:str, completed:str , db: Session = Depends(get_db)):
    todo = Todo(title = title , completed = completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message" : "Todo Created",
        "data"  : todo 
    }


# Read API
@app.get("/todo")
def get_data(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()

    return { 
        "message": "Data Fetched Sucessfully",
        "Total"  : len(todos),
        "data" : todos
    }

@app.get("/todos/{todo_id}")
def get_data_by_id(todo_id=int , db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo:
        raise HTTPException(status_code=404 , detail="todo not found")


    return todo

#update API
@app.put("/todo/{todo_id}")
def update_todo(todo_id:int , title:str, completed:str , db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
     
    if not todo:
        try:
            raise HTTPException(
                status_code=404,
                detail="todo not found"
            )
        finally:
            db.close()

    todo.title = title
    todo.completed = completed
    db.commit()
    
    return{
        "message" : f" id no. {todo_id} updated successfully",
        "data" : todo
    }


# delete API
@app.delete("/todo/{todo_id}")
def delete_todo(todo_id:int , db : Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,
                            detail="todo not found")
    
    db.delete(todo)
    db.commit()

    return{
        "Message" : "deleted todos",
        "data" : todo
    }