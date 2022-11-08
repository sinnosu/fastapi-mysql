from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND
from uuid import UUID

from models import Task
from schemas.task import TaskCreate, TaskUpdate


def get_task(db: Session, task_id: UUID):
    try:
        item = db.query(Task).get(task_id)
    except BaseException:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    return item

def get_tasks(db: Session, limit: int = 100):
    items = db.query(Task).limit(limit).all()
    return items


def create_task(db: Session, task: TaskCreate):
    try:
        db_task = Task(title=task.title, text=task.text)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
    except BaseException:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    return db_task


def update_task(db: Session, task_id: UUID, task: TaskUpdate):
    try:
        db_task = db.query(Task).get(task_id)
        db_task.title = task.title
        db_task.text = task.text
        db.commit()
    except BaseException:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    return db_task


def delete_task(db: Session, task_id: UUID):
    try:
        db_task = db.query(Task).get(task_id)
        db.delete(db_task)
        db.commit()
    except BaseException:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
