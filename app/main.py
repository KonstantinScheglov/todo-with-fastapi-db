from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db import crud
from app.db.database import get_db, session, engine
from app.models import schemas, models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post('/todos/', response_model=schemas.ReadTask)
def create_task_API(task: schemas.DatabaseCreateTask, db: Session = Depends(get_db)):
    new_task = crud.create_task(db=db, new_task=task) 
    return new_task


@app.get('/todos/{todo_id}', response_model=schemas.ReadTask)
def read_task_API(todo_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_id(db=db, id=todo_id)
    return db_task


@app.put('/todos/{todo_id}', response_model=schemas.UpdateTask)
def update_todo(todo_id: int, new_task: schemas.UpdateTask, db: Session = Depends(get_db)):
    upd_task = crud.update_task(db=db, task_id=todo_id, new_task=new_task)
    return upd_task

