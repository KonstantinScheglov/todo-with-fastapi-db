from pydantic import BaseModel


class DatabaseCreateTask(BaseModel):
    title: str
    description: str
    completed: bool = False


class ReadTask(DatabaseCreateTask):
    id: int    


class UpdateTask(DatabaseCreateTask):
    pass 
