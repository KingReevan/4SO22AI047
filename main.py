from fastapi import FastAPI, HTTPException
from number_fetcher import fetch_numbers
from number_store import add_numbers, get_all_numbers, get_average, get_count, reset_numbers

app = FastAPI()

@app.get("/numbers/{number_type}")
async def get_numbers(number_type: str):
    try:
        result = await fetch_numbers(number_type)  # Pass type to fetch_numbers
        prev_state = get_all_numbers().copy()
        add_numbers(result["numbers"])
        curr_state = get_all_numbers()

        return {
            "windowPrevState": prev_state,
            "windowCurrState": curr_state,
            "numbers": result["numbers"],
            "avg": round(get_average(), 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/average")
def average():
    avg = get_average()
    return {"average": avg}

@app.get("/all")
def all_numbers():
    return {"all_numbers": get_all_numbers()}

