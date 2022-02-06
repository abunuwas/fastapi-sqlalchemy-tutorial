import uuid

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, default=generate_uuid)
    created = Column(DateTime, nullable=False)
    email = Column(String, nullable=False)

    tasks = relationship("Task")

    def dict(self):
        return {
            "id": self.id,
            "created": self.created,
            "email": self.email,
            "tasks": self.tasks
        }


class Task(Base):
    __tablename__ = "task"

    id = Column(String, primary_key=True, default=generate_uuid)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime, nullable=False)
    priority = Column(String, nullable=False)
    status = Column(String, nullable=False)
    task = Column(String, nullable=False)
    user_id = Column(String, ForeignKey("user.id"))

    def dict(self):
        return {
            "id": self.id,
            "created": self.created,
            "priority": self.priority,
            "status": self.status,
            "task": self.task,
        }
