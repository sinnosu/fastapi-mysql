from database import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class Task(Base, TimestampMixin):
    __tablename__ = 'tasks'

    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    title = Column(String(128), nullable=False)
    text = Column(String(1024), index=True)

    # リレーション設定
    user_id = Column(
        UUIDType(binary=False),
        ForeignKey('users.uuid'),
        nullable=True
    )
    user = relationship(
        'User',
        back_populates='tasks'
    )

