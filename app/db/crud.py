from sqlalchemy.orm import Session
from app.models import models, schemas


def get_task_by_id(db: Session, id: int):
    return db.query(models.Tasks).filter(models.Tasks.id == id).first()


def create_task(db: Session, new_task: schemas.DatabaseCreateTask):
    db_task = models.Tasks(title=new_task.title, 
                           description=new_task.description, 
                           completed=new_task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, new_task: schemas.UpdateTask):
    db_update = get_task_by_id(db=db, id=task_id)
    for k, v in new_task.model_dump().items():
        if k is not None:
            setattr(db_update, k, v)
    db.commit()
    db.refresh(db_update)
    return db_update