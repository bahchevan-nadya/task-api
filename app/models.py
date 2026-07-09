from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from .db import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False,
        default='new'
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )