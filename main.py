from fastapi import FastAPI, HTTPException
from number_fetcher import fetch_numbers
from number_store import add_numbers, get_all_numbers, get_average, get_count, reset_numbers

app = FastAPI()

@app.get("/get-numbers")
async def get_numbers():
    try:
        result = await fetch_numbers()
        add_numbers(result["numbers"])  # Save the fetched numbers to memory
        return {"message": "Numbers fetched and stored", "new_numbers": result["numbers"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/average")
def average():
    avg = get_average()
    return {"average": avg}

@app.get("/count")
def count():
    return {"count": get_count()}

@app.get("/all")
def all_numbers():
    return {"all_numbers": get_all_numbers()}

@app.post("/reset")
def reset():
    reset_numbers()
    return {"message": "All numbers have been cleared"}
