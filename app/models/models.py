from app.db.database import Base
from sqlalchemy.orm import mapped_column, Mapped

class Tasks(Base):
    __tablename__ =  'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)


