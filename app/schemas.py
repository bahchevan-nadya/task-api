from enum import Enum
from datetime import datetime

from pydantic import BaseModel, ConfigDict

class TaskStatus(str, Enum):
    new = 'new'
    in_progress = 'in_progress'
    done = 'done'

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdateStatus(BaseModel):
    status: TaskStatus

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)