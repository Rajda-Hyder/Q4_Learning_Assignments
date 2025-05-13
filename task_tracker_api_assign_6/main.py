from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, constr, validator
from typing import List, Dict
from datetime import date

# FastAPI app initialization
app = FastAPI()

# Global dictionaries to store users and tasks
USERS: Dict[int, "UserRead"] = {}
TASKS: Dict[int, "Task"] = {}

# Pydantic Models

# User creation model
class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr

# User read model with ID field
class UserRead(UserCreate):
    id: int

# Task model
class Task(BaseModel):
    title: str
    description: str
    due_date: date
    status: constr(pattern="^(pending|in-progress|done)$")

    # Validator for due_date field
    @validator("due_date")
    def validate_due_date(cls, value):
        if value < date.today():
            raise ValueError("Due date cannot be in the past.")
        return value

# Endpoints

# Create a user
@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    user_id = len(USERS) + 1  # Generate a new ID
    new_user = UserRead(id=user_id, **user.dict())
    USERS[user_id] = new_user
    return new_user

# Get user details by ID
@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

# Create a task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task, user_id: int):
    task_id = len(TASKS) + 1  # Generate a new ID
    new_task = Task(**task.dict())
    TASKS[task_id] = new_task
    return new_task

# Get task details by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

# Update task status by ID
@app.put("/tasks/{task_id}")
def update_task_status(task_id: int, status: str):
    if status not in ["pending", "in-progress", "done"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid status")
    
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    task.status = status
    TASKS[task_id] = task
    return {"message": "Task status updated", "task": task}

# List all tasks for a specific user
@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_user_tasks(user_id: int):
    user_tasks = [task for task_id, task in TASKS.items() if task_id == user_id]
    if not user_tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No tasks found for this user")
    return user_tasks

