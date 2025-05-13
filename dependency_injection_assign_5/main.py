from fastapi import FastAPI, Depends, HTTPException, Query, status
from typing import Annotated

app = FastAPI()

# ────────────────────────────────────────────────
# 1. FUNCTION-BASED DEPENDENCY (REUSABLE GOAL)
# ────────────────────────────────────────────────
def get_goal():
    return {"goal": "We are building AI Agents Workforce"}

@app.get("/goal")
def show_goal(data: Annotated[dict, Depends(get_goal)]):
    return data


# ────────────────────────────────────────────────
# 2. DEPENDENCY WITH QUERY PARAMETERS (LOGIN CHECK)
# ────────────────────────────────────────────────
def check_login(
    username: str = Query(None),
    password: str = Query(None)
):
    if username == "admin" and password == "admin":
        return {"message": "Login Successful"}
    raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/login")
def login_status(user: Annotated[dict, Depends(check_login)]):
    return user


# ────────────────────────────────────────────────
# 3. MULTIPLE DEPENDENCIES (MATH TRANSFORM)
# ────────────────────────────────────────────────
def add_one(num: int):
    return num + 1

def add_two(num: int):
    return num + 2

@app.get("/calc/{num}")
def calculate_total(
    num: int,
    a: Annotated[int, Depends(add_one)],
    b: Annotated[int, Depends(add_two)]
):
    total = num + a + b
    return {"message": f"Total is {total}"}


# ────────────────────────────────────────────────
# 4. CLASS-BASED DEPENDENCY (OBJECT LOOKUP)
# ────────────────────────────────────────────────
blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog"
}

users = {
    "10": "Fatima",
    "20": "Zain"
}

class GetObjectOr404:
    def __init__(self, data_source: dict):
        self.data_source = data_source

    def __call__(self, id: str):
        obj = self.data_source.get(id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Item with ID '{id}' not found."
            )
        return obj

get_blog = GetObjectOr404(blogs)
get_user = GetObjectOr404(users)

@app.get("/blogs/{id}")
def read_blog(blog: Annotated[str, Depends(get_blog)]):
    return {"blog": blog}

@app.get("/users/{id}")
def read_user(user: Annotated[str, Depends(get_user)]):
    return {"user": user}


# ────────────────────────────────────────────────
# 5. SUB-DEPENDENCY (LOGIN CHECK + GOAL COMBINED)
# ────────────────────────────────────────────────
def combine_login_and_goal(
    login: Annotated[dict, Depends(check_login)],
    goal: Annotated[dict, Depends(get_goal)]
):
    return {**login, **goal}

@app.get("/dashboard")
def dashboard(data: Annotated[dict, Depends(combine_login_and_goal)]):
    return data
