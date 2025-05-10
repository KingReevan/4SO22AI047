import httpx
from token_manager import get_token

BASE_URL = "http://20.244.56.144/evaluation-service"

VALID_TYPES = {
    "p": "primes",
    "f": "fibo",
    "e": "even",
    "r": "rand"
}

async def fetch_numbers(number_type: str):
    if number_type not in VALID_TYPES:
        raise ValueError("Invalid number type. Use one of: p, f, e, r")

    endpoint = VALID_TYPES[number_type]
    url = f"{BASE_URL}/{endpoint}"    #Endpoint will dynamically change based on the type of number requested by whoever

    token = await get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        async with httpx.AsyncClient(timeout=0.5) as client:  # 500ms timeout
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            print("debugLine: Received JSON response from Affordmed:", data)
            return data
    except httpx.RequestError:
        print("Request failed")
        return {"numbers": []}
