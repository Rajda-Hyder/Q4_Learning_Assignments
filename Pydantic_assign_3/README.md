# 📘 Pydantic + FastAPI DACA Tutorial — README

This README provides a full explanation of the Pydantic + FastAPI setup in the context of a DACA-style chatbot system. It includes theory, examples, and usage instructions, aimed at learners.

---

## 📌 What is Pydantic?

**Pydantic** is a Python library used to define data structures and validate data. It makes sure that the data is:

* **Type-safe** (correct types: int, str, etc.)
* **Complete** (required fields are present)
* **Well-structured** (can use nested models)

### ✅ Why use Pydantic?

* Helps catch bugs early with validation.
* Reduces manual error checking.
* Makes your code cleaner and safer.
* Automatically converts types if possible.

Pydantic works by creating classes that inherit from `BaseModel`.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
```

This ensures that `id` must be an integer, `name` and `email` must be strings.

---

## 🧠 What is DACA?

**DACA** stands for **Distributed Agentic Computing Architecture**. It is a design pattern where multiple intelligent agents work together in a system.

### 🤖 Example DACA Scenario:

* A chatbot sends a message.
* An AI assistant analyzes the message.
* A second agent responds with context.

Pydantic is useful in DACA systems because:

* It ensures **data consistency** across agents.
* Makes **validation and error-handling** easier.
* Handles **nested and complex data** smoothly.

---

## 🔌 Required Libraries

Install the following packages using `uv` (or `pip`):

```bash
uv add "fastapi[standard]"
```

### 🔃 Or with pip:

```bash
pip install fastapi uvicorn
```

---

## 📁 Project Files & Explanation

### 1. `pydantic_example_1.py`

**Basic Pydantic Example**

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  # Optional field

user = User(id=1, name="Alice", email="alice@example.com", age=25)
print(user.model_dump())
```

### ✅ Explanation:

* `BaseModel`: Makes the class a Pydantic model.
* `ValidationError`: Used to catch data validation issues.
* `age: int | None`: Means this field is optional.

---

### 2. `pydantic_example_2.py`

**Nested Model Example**

```python
from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: str
    addresses: List[Address]
```

### ✅ Explanation:

* `List[Address]`: Means the field expects a list of Address objects.
* Useful when a user has multiple addresses.
* The Address model is nested inside the UserWithAddress model.
* EmailStr automatically validates the email format.

---

### 3. `pydantic_example_3.py`

**Adding Validation with ****`@field_validator`**** (Pydantic v2)**

```python
from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]

# we use Pydantic V1 style `@validator` validators are deprecated.so migrate to Pydantic V2 style `@field_validator`

    @field_validator("name")
    @classmethod
    def name_must_be_at_least_two_chars(cls, v):
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v

# Test with invalid data
try:
    invalid_user = UserWithAddress(
        id=3,
        name="A",  # Too short
        email="charlie@example.com",
        addresses=[{"street": "789 Pine Rd", "city": "Chicago", "zip_code": "60601"}],
    )
except ValidationError as e:
    
    print("\n" + "="*50 + "\n")
    print("Validation failed:")
    print(e)
    print("\n" + "="*50 + "\n")

# ✅ Test with valid data
try:
    valid_user = UserWithAddress(
        id=1,
        name="Alice",
        email="alice@example.com",
        addresses=[
            {"street": "123 Main St", "city": "New York", "zip_code": "10001"},
            {"street": "456 Oak Ave", "city": "Los Angeles", "zip_code": "90001"},
        ],
    )
    print("Valid user created successfully:")
    print(valid_user)
    print("As dictionary:", valid_user.model_dump())  # Optional
except ValidationError as e:
    print("Validation failed:")
    print(e)
```

### ✅ Explanation:

* `EmailStr`: Validates that the email is in proper format.
* `@field_validator`: Custom validator for a specific field.
* `ValidationError`: Error raised when data is invalid.

---

### 4. `main.py`

**FastAPI App with Nested Pydantic Models**

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import uuid4

app = FastAPI(title="DACA Chatbot API")

class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    session_id: str = Field(default_factory=lambda: str(uuid4()))

class Message(BaseModel):
    user_id: str
    text: str
    metadata: Metadata
    tags: list[str] | None = None

class Response(BaseModel):
    user_id: str
    reply: str
    metadata: Metadata

@app.get("/")
async def root():
    return {"message": "Welcome to the DACA Chatbot API! Access /docs for the API documentation."}

@app.get("/users/{user_id}")
async def get_user(user_id: str, role: str | None = None):
    return {"user_id": user_id, "role": role or "guest"}

@app.post("/chat/", response_model=Response)
async def chat(message: Message):
    if not message.text.strip():
        raise HTTPException(status_code=400, detail="Message text cannot be empty")
    reply_text = f"Hello, {message.user_id}! You said: '{message.text}'. How can I assist you today?"
    return Response(user_id=message.user_id, reply=reply_text, metadata=Metadata())
```

### ✅ Explanation:

* `Field(default_factory=...)`: Automatically sets default values like timestamps or UUIDs.
* `/chat/`: Accepts a POST request with a nested message object.
* `/users/{user_id}`: Simple GET route with optional query parameter.

---

## 🚀 How to Run the Project

### 1. Create project and virtual environment:

```bash
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate
```

### 2. Install required packages:

```bash
uv add "fastapi[standard]"
```

### 3. Run FastAPI app:

```bash
fastapi dev main.py
```

Or:

```bash
uvicorn main:app --reload
```

### 4. Open Browser:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Root Page: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🌍 Where to Use Pydantic

* ✅ APIs with FastAPI
* ✅ Data validation in AI pipelines
* ✅ Configuration handling
* ✅ Form input validation
* ✅ JSON file validation

---

## 🧠 Summary

* Pydantic helps keep your data safe, clean, and structured.
* Perfect match with FastAPI and DACA-style agent systems.
* It reduces bugs and makes your code easier to maintain.

---

## 📎 References

* Pydantic Docs: [https://docs.pydantic.dev](https://docs.pydantic.dev)
* FastAPI Docs: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)
* DACA Blog: [https://www.latent.space/p/daca](https://www.latent.space/p/daca)


