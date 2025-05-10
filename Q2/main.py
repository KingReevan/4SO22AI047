from fastapi import FastAPI, HTTPException, Query
from stock_service import get_average_price_data

app = FastAPI()

@app.get("/stocks/{ticker}")
async def average_stock_price(
    ticker: str,
    minutes: int = Query(..., gt=0),
    aggregation: str = Query("average")
):
    if aggregation != "average":
        raise HTTPException(status_code=400, detail="Only 'average' aggregation is supported")

    try:
        data = await get_average_price_data(ticker, minutes)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
