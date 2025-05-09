from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random
import time

mock_app = FastAPI()

# Dummy token storage
VALID_TOKEN = "access"

@mock_app.post("/api/token")
async def generate_token(request: Request):
    data = await request.json()
    if data["username"] == "reevan" and data["password"] == "dmello":
        return {"token": VALID_TOKEN}
    return JSONResponse(status_code=401, content={"error": "Invalid credentials"})

@mock_app.get("/api/numbers")
async def get_numbers(request: Request):
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {VALID_TOKEN}":
        return JSONResponse(status_code=401, content={"error": "Invalid or missing token"})

    # simulate delay of < 500ms
    time.sleep(0.3)

    return {"numbers": random.sample(range(1, 20), 5)}
