from sqlalchemy.ext.asyncio import AsyncSession
from app.models import models, schemas


async def get_task_by_id(db: AsyncSession, id: int):
    item = await db.get_one(models.Tasks, ident=id)
    
    return item


async def create_task(db: AsyncSession, new_task: schemas.DatabaseCreateTask):
    db_task = models.Tasks(title=new_task.title, 
                           description=new_task.description, 
                           completed=new_task.completed)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)

    return db_task

async def update_task(db: AsyncSession, task_id: int, upd_task: schemas.UpdateTask):
    db_update = await get_task_by_id(db=db, id=task_id)
    for k, v in upd_task.model_dump().items():
        if k is not None:
            setattr(db_update, k, v)
    await db.commit()
    await db.refresh(db_update)

    return db_update