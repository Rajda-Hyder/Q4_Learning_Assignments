# ✅ Task Tracker API (FastAPI)

This is a simple Task Tracker API built using **FastAPI** and **Pydantic**.  
It helps manage **Users** and their **Tasks**.

---

## 📦 Features

- Create and get users.
- Create and get tasks.
- Link tasks to users.
- Validate email, username, and due dates.
- Update task status (only valid values allowed).

---

## 🚀 How to Run

### 1. Setup Project

Open terminal and run these commands:

```bash
uv init task_tracker_api
cd task_tracker_api
uv venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
uv add "fastapi[standard]"  # Add FastAPI
uv add "uvicorn"            # Add Uvicorn server
```

### 2. Start the API
Make sure your main file is named main.py or adjust the command below:

```bash
uvicorn main:app --reload
```

Now open your browser:

📍 Swagger UI: http://127.0.0.1:8000/docs

📍 ReDoc: http://127.0.0.1:8000/redoc

## 🧑 User Model
```python
class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
```

## ✅ Task Model

```python
class Task(BaseModel):
    title: str
    description: str
    due_date: date
    status: constr(pattern="^(pending|in-progress|done)$")

    @validator("due_date")
    def validate_due_date(cls, value):
        if value < date.today():
            raise ValueError("Due date cannot be in the past.")
        return value
```

## 🛠️ API Endpoints

### 👤 Users

| Method | Endpoint      | Description       |
|--------|---------------|-------------------|
| POST   | `/users/`     | Create new user   |
| GET    | `/users/{id}` | Get user by ID    |

#### Example Body to Create User:

```json

{
  "username": "ahmed",
  "email": "ahmed@gmail.com"
}
```
### ✅ Tasks

| Method | Endpoint               | Description              |
|--------|------------------------|--------------------------|
| POST   | `/tasks/`              | Create new task          |
| GET    | `/tasks/{id}`          | Get task by ID           |
| PUT    | `/tasks/{id}`          | Update task status only  |
| GET    | `/users/{id}/tasks`    | Get all tasks of a user  |

#### Example Body to Create Task:

```json
{
  "title": "Complete FastAPI Project",
  "description": "Finish task tracker assignment",
  "due_date": "2025-05-15",
  "status": "pending"
}
```
#### To Update Status:

```json
{
  "status": "done"
}
```

##### ✅ Allowed status values:

- pending

- in-progress

- done

## 📂 Internal Storage
For now, all data is stored in simple dictionaries:

```python
USERS: dict[int, User] = {}
TASKS: dict[int, Task] = {}
```

So when you restart the app, all data is lost. For permanent storage, you can later add a database like SQLite or PostgreSQL.

## ✅ Validation Rules
- ✅ Username must be 3–20 characters.

- ✅ Email must be valid.

- ✅ Due date must be today or in the future.

- ✅ Status must be one of these: pending, in-progress, done.

## 📧 Author

Syeda Rajda Bano
rajdahyder@gmail.com
