from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import crud
from app.db.database import get_async_session
from app.models import schemas, models


app = FastAPI()


@app.post('/todos/', response_model=schemas.ReadTask)
async def create_task_API(task: schemas.DatabaseCreateTask, db: Session = Depends(get_db)):
    new_task = await crud.create_task(db=db, new_task=task)
    return new_task


@app.get('/todos/{todo_id}', response_model=schemas.ReadTask)
async def read_task_API(todo_id: int, db: Session = Depends(get_async_session)):
    read_task = await crud.get_task_by_id(db=db, id=todo_id)
    if read_task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return read_task


@app.put('/todos/{todo_id}', response_model=schemas.UpdateTask)
async def update_todo(todo_id: int, new_task: schemas.UpdateTask, db: Session = Depends(get_async_session)):
    upd_task = await crud.update_task(db=db, task_id=todo_id, new_task=new_task)
    return upd_task

@app.delete('/todos/{todo_id}', response_model=str)
async def delete_task(todo_id: int, db: Session = Depends(get_async_session)):
    del_task = await crud.get_task_by_id(db=db, id=todo_id)
    if del_task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    await db.delete(del_task)
    await db.commit()
    return "Задача успешно удалена"

