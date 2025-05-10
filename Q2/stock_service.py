import httpx

BASE_URL = "http://20.244.56.144/evaluation-service/stocks"

async def get_average_price_data(ticker: str, minutes: int):
    url = f"{BASE_URL}/{ticker}?minutes={minutes}"

    try:
        async with httpx.AsyncClient(timeout=0.5) as client:
            response = await client.get(url)
            response.raise_for_status()
            price_history = response.json()

            if not price_history:
                return {
                    "averageStockPrice": 0.0,
                    "priceHistory": [],
                }

            prices = [entry["price"] for entry in price_history]
            avg_price = sum(prices) / len(prices)

            return {
                "averageStockPrice": round(avg_price, 6),
                "priceHistory": price_history,
            }

    except httpx.RequestError:
        raise Exception("Failed to fetch data: API request error")
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")


