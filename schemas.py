from datetime import datetime
from enum import Enum
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel


class Error(BaseModel):
    detail: Optional[str] = None


class Priority(Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Status(Enum):
    progress = "progress"
    pending = "pending"
    completed = "completed"


class CreateTaskSchema(BaseModel):
    priority: Optional[Priority] = "low"
    status: Optional[Status] = "pending"
    task: str


class GetTaskSchema(BaseModel):
    id: UUID
    created: datetime
    priority: Priority
    status: Status
    task: str


class ListTasksSchema(BaseModel):
    tasks: List[GetTaskSchema]
