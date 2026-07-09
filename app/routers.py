from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .db import get_db
from . import crud, schemas

router = APIRouter(tags=["Tasks"])
@router.post(
    "/tasks",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
        task: schemas.TaskCreate,
        db: Session = Depends(get_db)
):
    return crud.create_task(db, task)

@router.get(
    "/tasks",
    response_model=list[schemas.TaskResponse]
)
def get_tasks(
        db: Session = Depends(get_db)
):
    return crud.get_tasks(db)

@router.get(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse
)
def get_task(
        task_id: int,
        db: Session = Depends(get_db)
):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return task

@router.patch(
    "/tasks/{task_id}/status",
    response_model=schemas.TaskResponse
)
def update_status(
        task_id: int,
        body: schemas.TaskUpdateStatus,
        db: Session = Depends(get_db)
):
    task = crud.update_status(db, task_id, body.status)
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return task

@router.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(
        task_id: int,
        db: Session = Depends(get_db)
):
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )