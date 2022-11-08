from database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from schemas.user import \
    User as UserSchema, UserDetail as UserDetailSchema
import cruds.user as crud

router = APIRouter()

@router.get('/', response_model=List[UserSchema])
async def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)

@router.get('/{user_id}', response_model=UserDetailSchema)
async def get_user(user_id: UUID, db: Session = Depends(get_db)):
    return crud.get_user(user_id=user_id, db=db)
