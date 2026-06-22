from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import select, insert, update
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine

class Base(DeclarativeBase): pass

class Task(Base):
    __tablename__ = "Tasks"
    
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, nullable=True, default=False)
    
def engine():
    engine = create_engine("sqlite:///tasks.db", echo=True)
    Base.metadata.create_all(engine)
    return engine

def populate_db(engine):
    with Session(engine) as session:
        task1 = Task(
            id = 0,
            title = "Task1 Title",
            completed = False
        )
        task2 = Task(
            id = 1,
            title = "Task2 Title",
            completed = False
        )
        task3 = Task(
            id = 2,
            title = "Task3 Title",
            completed = True
        )
        session.add_all([task1,task2,task3])
        session.commit()

def setup(engine):
    populate_db(engine)
    
def get_task(engine, id: int):
    with Session(engine) as session:
        q = select(Task).where(Task.id==id)
        result = session.scalars(q).all()
    return result

def create_task(engine, task: Task):
    with Session(engine) as session:
        q = insert(Base.metadata.tables["Tasks"]).values(title = task.title, completed = False)
        result = session.execute(q)
        session.commit()
    return result

def list_tasks(engine):
    with Session(engine) as session:
        q = select(Task)
        results = session.scalars(q).all()
        titles = [task.title for task in results]
    return titles
        
def is_empty(engine):
    with Session(engine) as session:
        q = select(Task)
        result = session.scalars(q).all()
    return len(result)==0

def mark_completed(engine, id: int):
    with Session(engine) as session:
        task = session.get(Task, id)
        task.completed = True
        session.commit()