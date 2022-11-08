from database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from schemas.task import Task as TaskSchema, \
    TaskCreate as TaskCreateSchema, TaskCreate as TaskCreateSchema, TaskUpdate as TaskUpdateSchema
import cruds.task as crud

router = APIRouter()

@router.get('/{task_id}', response_model=TaskSchema)
async def get_task(task_id: UUID, db: Session = Depends(get_db)):
    return crud.get_task(task_id=task_id, db=db)

@router.get('/', response_model=List[TaskSchema])
async def get_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db=db)

@router.post('/', response_model=TaskSchema)
async def create_task(task: TaskCreateSchema, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@router.put('/{task_id}', response_model=TaskSchema)
async def update_tasks(task_id: UUID, task: TaskUpdateSchema, db: Session = Depends(get_db)):
    return crud.update_task(db=db, task_id=task_id, task=task)

@router.delete('/{task_id}')
async def delete_tasks(task_id: UUID, db: Session = Depends(get_db)):
    crud.delete_task(db=db, task_id=task_id)

