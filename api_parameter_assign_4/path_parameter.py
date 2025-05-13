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
