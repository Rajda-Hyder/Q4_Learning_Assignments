# FastAPI Dependency Injection (Simple Guide with Live Examples)

This guide explains **Dependency Injection (DI)** in FastAPI using **real examples**.

---

## ✅ What is Dependency Injection?

Dependency Injection lets you share common logic (like user login, data fetch, etc.) across multiple API routes in a clean and reusable way.

---

## 🌟 Why Use Dependency Injection?

| Benefit             | Meaning                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Reusability         | Write common logic once, use everywhere (like login, DB connection).   |
| Separation of Logic | Keeps route code clean. Common logic goes into dependency function.     |
| Testability         | Easy to replace dependencies during testing.                            |
| Organization        | Keeps project structure clean and modular.                              |

---

## 🧪 How it Works

1. **Define a Dependency Function or Class**: It does a task like checking login or getting data.
2. **Use it in your API Function** using `Depends()` or `Annotated`.

> FastAPI runs the dependency first, and passes the result to your API function.

---

## 🚀 Examples of Dependencies

### 1. Basic Function Dependency

```python
from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

def get_simple_goal():
    return {"goal": "We are building AI Agents Workforce"}

@app.get("/get-simple-goal")
def simple_goal(response: Annotated[dict, Depends(get_simple_goal)]):
    return response
```

### 🔎 What Happens:
- The get_simple_goal() function runs first.

- The result is passed as response.

### 2. Dependency With Parameters
```python
def get_goal(username: str):
    return {"goal": "We are building AI Agents Workforce", "username": username}

@app.get("/get-goal")
def get_my_goal(response: Annotated[dict, Depends(get_goal)]):
    return response
```

### ✅ Example:
```pgsql
GET /get-goal?username=ali
→ {"goal": "We are building AI Agents Workforce", "username": "ali"}
```

### 3. Dependency with Query Parameters (Login Check)
```python
from fastapi import Query

def dep_login(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message": "Login Successful"}
    else:
        return {"message": "Login Failed"}

@app.get("/signin")
def login_api(user: Annotated[dict, Depends(dep_login)]):
    return user
```

### ✅ Example:
```pgsql
GET /signin?username=admin&password=admin
→ {"message": "Login Successful"}
```

### 4. Multiple Dependencies
```python
def depfunc1(num: int): 
    return num + 1

def depfunc2(num: int): 
    return num + 2

@app.get("/main/{num}")
def get_main(
    num: int, 
    num1: Annotated[int, Depends(depfunc1)], 
    num2: Annotated[int, Depends(depfunc2)]
):
    total = num + num1 + num2
    return f"Pakistan {total}"
```

### ✅ Example:
```bash
GET /main/5
→ 5 + (5+1) + (5+2) = 18
→ "Pakistan 18"
```

### 5. Class as Dependency (like Django’s get_object_or_404)
```python
from fastapi import HTTPException, status

blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

users = {
    "8": "Ahmed",
    "9": "Mohammed"
}

class GetObjectOr404:
    def __init__(self, model):
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj

blog_dependency = GetObjectOr404(blogs)
user_dependency = GetObjectOr404(users)

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return blog_name

@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    return user_name
```
### ✅ Examples:
```sql
GET /blog/1 → "Generative AI Blog"
GET /user/8 → "Ahmed"
GET /blog/99 → 404 Error
```
## 🔚 Final Notes
- Use functions for simple logic.

- Use classes when you want reusable, customizable, and testable logic.

- Depends() helps FastAPI manage these for each request.


