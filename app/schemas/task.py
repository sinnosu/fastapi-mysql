from pydantic import BaseModel
from uuid import UUID


class TaskBase(BaseModel):
    title: str
    text: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    uuid: UUID

    class Config:
        orm_mode = True