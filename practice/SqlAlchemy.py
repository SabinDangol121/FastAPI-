from sqlalchemy import create_engine, Column , Integer , String
from sqlalchemy.orm import sessionmaker , declarative_base , Session
from fastapi import FastAPI,Depends

app = FastAPI()
DATABASE_URL = "sqlite:///./practicedb.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__="todos"

    id = Column(Integer , primary_key=True , index = True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(db:Session = Depends(get_db)):
    return{
        "message" : "Database connected fine"
    }