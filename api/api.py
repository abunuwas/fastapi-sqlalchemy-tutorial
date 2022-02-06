import datetime
import uuid

from fastapi import HTTPException
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from api.schemas import ListTasksSchema, GetTaskSchema, CreateTaskSchema
from api.server import server, session_maker
from data_access.models import Task, User

TODO = []


@server.get("/todo", response_model=ListTasksSchema)
def get_tasks(request: Request):
    user_id = request.state.user_id
    with session_maker() as session:
        tasks = [
            task.dict() for task in session.query(User).filter(User.id == user_id).first().tasks
        ]
    return {"tasks": tasks}


@server.post("/todo", response_model=GetTaskSchema, status_code=status.HTTP_201_CREATED)
def create_task(request: Request, payload: CreateTaskSchema):
    with session_maker() as session:
        task = Task(
            created=datetime.datetime.utcnow(),
            updated=datetime.datetime.utcnow(),
            priority=payload.priority.value,
            status=payload.status.value,
            task=payload.task,
            user_id=request.state.user_id
        )
        session.add(task)
        session.commit()
        task = task.dict()
    return task


@server.get("/todo/{task_id}", response_model=GetTaskSchema)
def get_task(request: Request, task_id: uuid.UUID):
    with session_maker() as session:
        task = session.query(Task).filter(
            Task.id == str(task_id), Task.user_id == request.state.user_id
        ).first()
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
    return task.dict()


@server.put("/todo/{task_id}", response_model=GetTaskSchema)
def update_task(request: Request, task_id: uuid.UUID, payload: CreateTaskSchema):
    with session_maker() as session:
        task = session.query(Task).filter(
            Task.id == str(task_id), Task.user_id == request.state.user_id
        ).first()
        if task is None:
            raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
        task.status = payload.status.value
        task.priority = payload.priority.value
        task.task = payload.task
        task.updated = datetime.datetime.utcnow()
        session.add(task)
        session.commit()
        task = task.dict()
    return task


@server.delete(
    "/todo/{task_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response
)
def delete_task(request: Request, task_id: uuid.UUID):
    with session_maker() as session:
        task = session.query(Task).filter(
            Task.id == str(task_id), Task.user_id == request.state.user_id
        ).first()
        if task is None:
            raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
        session.delete(task)
        session.commit()
