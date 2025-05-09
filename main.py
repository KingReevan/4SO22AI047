from fastapi import FastAPI, HTTPException
from number_fetcher import fetch_numbers

app = FastAPI()

@app.get("/get-numbers")
async def get_numbers():
    try:
        result = await fetch_numbers()
        return {"numbers": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
