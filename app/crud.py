from sqlalchemy.orm import Session
from .models import Task
from .schemas import TaskCreate, TaskStatus

def create_task(db: Session, task: TaskCreate):
    db_task = Task(
        title=task.title,
        description=task.description,
        status=TaskStatus.new.value
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session):
    return db.query(Task).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_status(db: Session, task_id: int, status: TaskStatus):
    task = get_task(db, task_id)
    if not task:
        return None
    task.status = status.value
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True