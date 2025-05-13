# FastAPI Parameters Guide with Examples(main.py)

## Complete Example: `main.py`

```python
from fastapi import FastAPI, Path, Query, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(
        ...,  # required
        title="The ID of the item",
        description="A unique identifier for the item",
        ge=1
    )
):
    return {"item_id": item_id}

@app.get("/items/")
async def read_items(
    q: str | None = Query(
        None,
        title="Query string",
        description="Query string for searching items",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    return {"q": q, "skip": skip, "limit": limit}

@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="Optional item data (JSON body)")
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item.model_dump()})
    return result
```

## Explanation Line-by-Line

### Imports

* `FastAPI`, `Path`, `Query`, `Body`: To define and validate various parameter types.
* `BaseModel`: Used to define the structure and validation for request bodies.

### Create App

```python
app = FastAPI()
```

* This creates a new FastAPI application instance.

### Define a Pydantic Model

```python
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
```

* Used to validate JSON body input.

### Path Parameter Endpoint

```python
@app.get("/items/{item_id}")
```

* Example URL: `/items/5`
* `item_id` is required and must be `int >= 1`

### Query Parameters Endpoint

```python
@app.get("/items/")
```

* Example URL: `/items/?q=book&skip=0&limit=10`
* `q`: Optional search string (3 to 50 chars)
* `skip`: Default 0, for pagination
* `limit`: Default 10, max 100 items

### Combining Path + Query + Body

```python
@app.put("/items/validated/{item_id}")
```

* Combines three parameter types:

  * Path: `item_id`
  * Query: `q`
  * Body: `item` object (name, description, price)

### Conditional Updates

```python
if q:
    result.update({"q": q})
if item:
    result.update({"item": item.model_dump()})
```

* If optional values are provided, they are added to the response.

## Running the Application

### Step 1: Install FastAPI and dependencies

```bash
uv add "fastapi[standard]"
```

### Step 2: Run the development server

```bash
fastapi dev main.py
```

### Step 3: Open Docs

Go to:

```
http://localhost:8000/docs
```

To explore and test all the APIs with auto-generated Swagger UI.

---

## ✅ Key Validation Functions in FastAPI

| Function             | Meaning (Simple English)                                                       |
| -------------------- | ------------------------------------------------------------------------------ |
| `Path()`             | Used to define and **validate path parameters** (like `/items/{id}`).          |
| `Query()`            | Used to define and **validate query parameters** (like `/items?skip=0`).       |
| `ge`                 | "Greater than or equal to" – value must be **≥ this number**.                  |
| `gt`                 | "Greater than" – value must be **> this number**.                              |
| `le`                 | "Less than or equal to" – value must be **≤ this number**.                     |
| `lt`                 | "Less than" – value must be **< this number**.                                 |
| `min_length`         | Minimum length for strings – good for **validating text input**.               |
| `max_length`         | Maximum length for strings – limits **how long text can be**.                  |
| `regex` or `pattern` | Checks if the input **matches a specific pattern** (like email, phone number). |
| `enum`               | Limits values to a **predefined set** (like "red", "green", "blue" only).      |

## 📌 Bonus Tip:

When any validation fails, FastAPI automatically returns:

- Status Code: 422 Unprocessable Entity

- Details: Clear JSON error message explaining what went wrong.

# FastAPI with Path Parameters Example

This project demonstrates the use of **path parameters** in a FastAPI application. Path parameters are a crucial part of creating RESTful APIs, allowing you to accept dynamic values in the URL.

## Introduction

In this project, we demonstrate how to create a FastAPI app that handles path parameters to fetch specific data from an external API. We use **`httpx`** to make asynchronous HTTP requests to `https://dummyjson.com/quotes` to fetch quotes based on the provided quote ID.

## What are API Parameters?

API parameters are values passed by the client to an API endpoint. There are several types of parameters in a RESTful API:
1. **Query Parameters** – Passed as part of the URL after `?`, e.g., `/items?category=books`.
2. **Path Parameters** – Defined within the URL path, e.g., `/items/{item_id}`.
3. **Request Body** – Sent in the body of the HTTP request, typically used for POST, PUT, and PATCH requests.

## Path Parameters

### Path Parameters Definition

A **path parameter** is a variable part of a URL. It is a placeholder in the URL that allows dynamic data to be passed through the request. 

For example, in the URL `/items/{item_id}`, `{item_id}` is a path parameter. When you access `/items/5`, the path parameter `item_id` will be `5`.

### How Path Parameters are Used

Path parameters are useful when we need to specify resources in a REST API. They allow you to access specific items, quotes, or other resources by their unique identifiers, such as an `id`.

### Path Parameter Characteristics:
- They are placed inside curly braces `{}` within the URL path.
- They are typically used to fetch specific resources like a product, user, or quote.
- They are required unless specified as optional.

### Example Use Cases:
- `/users/{user_id}`: Fetches user details by their unique ID.
- `/posts/{post_id}`: Fetches a specific blog post based on its ID.
- `/quotes/{quote_id}`: Fetches a specific quote by its ID.

### ✅ Supported Types in Path Parameters

FastAPI automatically performs type conversion and validation based on the type you define in your function parameters.

| Type  | Description              | Example URL         |
|-------|--------------------------|---------------------|
| `int` | Integer number           | `/items/123`        |
| `str` | Text or string           | `/users/john_doe`   |
| `float` | Decimal number         | `/price/45.67`      |
| `bool` | Boolean (true/false)    | `/active/true` or `/active/false` |

### 📌 Notes:
- FastAPI will return an error if the value in the path doesn't match the expected type.
- Boolean values are case-insensitive, so `True`, `true`, `FALSE`, etc. are all valid.

## Code Example

This FastAPI application demonstrates how to use path parameters in an API endpoint.

```python
from fastapi import FastAPI, Path
import httpx

app = FastAPI()

@app.get("/quotes/{quote_id}")
async def get_quote_by_id(
    quote_id: int = Path(
        ...,  # ... means the parameter is required
        title="The ID of the quote",
        description="A unique identifier for the quote",
        ge=1  # greater than or equal to 1
    )
):
    # External API URL for fetching a specific quote by ID
    url = f"https://dummyjson.com/quotes/{quote_id}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    # Check if response contains valid data
    if response.status_code == 404:
        return {"error": "Quote not found"}
    
    return response.json()
```

## Explanation:
- The endpoint /quotes/{quote_id} accepts a path parameter quote_id to fetch a specific quote.

- The parameter is required and must be an integer (ge=1 ensures the ID is greater than or equal 
  to 1).

- We use httpx.AsyncClient() to make an asynchronous call to the external API and fetch the quote
   by ID.

## Run the Application
To run this application locally:

1- Save the code in a file named app.py.

2- Install FastAPI and httpx using pip:

```bash
pip install fastapi httpx
```
3- Run the application with uvicorn:

```bash
uvicorn app:app --reload
```
4- Open your browser or use a tool like Postman to test the endpoints:

 - To fetch a quote by ID, visit:

```arduino
http://127.0.0.1:8000/quotes/5
```
 - Replace 5 with any valid quote_id (must be greater than or equal to 1).

## Testing the Application
You can test the FastAPI app using Pytest. Below is a sample test case for checking the quote_id path parameter:

```python
from fastapi.testclient import TestClient
from path_parameter import app

client = TestClient(app)

def test_get_quote_by_id():
    # Test with valid quote_id
    response = client.get("/quotes/5")
    assert response.status_code == 200
    assert "quote" in response.json()

    # Test with invalid quote_id (not found)
    response = client.get("/quotes/99999")  # Assuming this ID doesn't exist
    assert response.status_code == 200
    assert response.json() == {"error": "Quote not found"}
```

### Error Handling
When using path parameters, errors might occur due to invalid input or missing data. For example:

 - If the user requests a quote_id that does not exist, we return a custom error message:

```json
{
  "error": "Quote not found"
}
```
FastAPI automatically handles common validation errors such as:

- Invalid type: If the quote_id is not an integer.

- Missing required parameter: If the quote_id is not provided.

- Value errors: If the quote_id is less than 1 (due to ge=1).

## Conclusion
This project demonstrates how to handle path parameters in FastAPI, allowing you to create RESTful APIs that accept dynamic data in the URL. By using FastAPI’s built-in validation and documentation features, we can easily create robust APIs.

Path parameters are useful when you need to specify resources by their unique identifier, such as fetching data for a specific quote, user, or product.


---

### Key Points Included in the `README.md`:

1. **Introduction to Path Parameters** – Explanation of what path parameters are and how they are used in API endpoints.
2. **Code Example** – A FastAPI code example demonstrating the use of path parameters.
3. **How to Run** – Instructions on how to set up and run the FastAPI application.
4. **Testing** – Instructions for testing the application using Pytest.
5. **Error Handling** – How FastAPI handles common errors related to path parameters.

# 🔍 Query Parameters in FastAPI

Query parameters are key-value pairs that appear after a `?` in the URL. They are used to filter, paginate, or customize the response of an API endpoint.

### 📘 Example URL:

```python
/items?q=laptop&skip=0&limit=10
```

### ✅ FastAPI Query Parameter Features:
- FastAPI uses `Query()` to add validations and metadata.
- You can set:
  - Default values
  - Required/optional behavior
  - Type enforcement
  - Value limits (min, max)

### ✅ Example Code:
```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str | None = Query(
        None,
        title="Query string",
        description="Query string for searching items",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    return {"q": q, "skip": skip, "limit": limit}
```

## 📌 Features Explained:
- q: Optional string with 3–50 character limit.

- skip: Integer ≥ 0 (used for pagination).

- limit: Integer ≤ 100 (max items to return).

# 📘 Using Multiple Parameters Together in FastAPI

This example shows how to combine different types of parameters in a single FastAPI endpoint:
- Path Parameter
- Query Parameter
- Request Body

---

## ✅ Code Example

```python
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel
```

- FastAPI, Path, Query, and Body are imported to define different parameter types.

- BaseModel from Pydantic is used to define request body structure.

```python
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
```
- This defines the shape of the JSON data (request body).

- name: required string

- description: optional string

- price: required float (decimal number)

```python
app = FastAPI()
```

- Create the FastAPI app.

```python
@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="Optional item data (JSON body)")
):
```

## 🔹 Parameters Explained:
### - Path Parameter (item_id)

- Required (...)

- Must be an integer

- Must be greater than or equal to 1

- Metadata: title = "Item ID"

### - Query Parameter (q)

- Optional string in the URL query

- Minimum length: 3 characters

### - Request Body Parameter (item)

- Optional JSON body sent with the request

- Based on the Item model

```python
    result = {"item_id": item_id}
```

- Start the response with the item_id.

```python
    if q:
        result.update({"q": q})
```

- If q is provided, add it to the result.

```python
    if item:
        result.update({"item": item.model_dump()})
```

- If request body is provided, convert it to a dictionary and add it.

```python
    return result
```

- Return the combined response.

## 🧪 Sample Request
### PUT /items/validated/5?q=laptop
#### JSON Body:

```json
{
  "name": "HP EliteBook",
  "description": "Business Laptop",
  "price": 950.50
}
```

### ✅ Response:

```json
{
  "item_id": 5,
  "q": "laptop",
  "item": {
    "name": "HP EliteBook",
    "description": "Business Laptop",
    "price": 950.5
  }
}
```
## 🧠 Summary

- You can combine Path, Query, and Request Body in one route.

- FastAPI automatically validates each parameter.

- This makes your APIs clean, well-documented, and easy to use.

# 📬 HTTP Request Components in FastAPI (Simple Definitions)

This document explains common HTTP request components in simple and easy-to-understand language.

---

## 📦 Request Body

**Definition:**  
Data that is sent in the body of an HTTP request — often in JSON format — especially when submitting or creating new data.

**Example Use:**  
When you send user registration data like name, email, and password via a POST request.

```json
{
  "name": "Ali",
  "email": "ali@example.com"
}
```

## 📑 Headers
### Definition:
Headers are extra key-value pairs sent with an HTTP request to share metadata like authentication tokens, content type, etc.

#### Example Use:

```pgsql
Authorization: Bearer <your_token_here>
Content-Type: application/json
```
#### Use Case:
Send a token to authenticate a user, or tell the server what kind of data is being sent.

## 🍪 Cookies
### Definition:
Cookies are small pieces of data sent by the server to the browser, and sent back from the browser in future requests.

#### Example Use:
To remember a user's login session or preferences between requests.

```makefile
Cookie: session_id=abc123xyz
```

## 📝 Form Data
### Definition:
Form data is information submitted by users through HTML forms (like input fields, radio buttons, etc.). Sent in application/x-www-form-urlencoded format.

#### Example Use:

A login form with username and password fields.

```bash
POST /login
Content-Type: application/x-www-form-urlencoded

username=admin&password=1234
```

## 📁 File Uploads
### Definition:
When users upload files (images, PDFs, etc.) through a web form, this data is sent as multipart/form-data.

#### Example Use:
Uploading a profile picture or document from a form input field.

```python
@app.post("/upload/")
async def upload(file: UploadFile):
    return {"filename": file.filename}
```

## ✅ Summary Table

| Component      | Description                                 | Common Use                          |
|----------------|---------------------------------------------|-------------------------------------|
| **Request Body** | Main content (usually JSON) sent in the request | Creating or updating data (POST/PUT) |
| **Headers**       | Metadata about the request                    | Auth tokens, content type, etc.     |
| **Cookies**       | Small data from the client                    | Sessions, user preferences          |
| **Form Data**     | Data from HTML forms                          | Login, signup forms                 |
| **File Uploads**  | Files submitted by user                       | Profile images, documents, etc.     |

💡 Tip: In FastAPI, each of these components can be handled with dedicated functions and decorators like Body(), Header(), Cookie(), Form(), and File().








