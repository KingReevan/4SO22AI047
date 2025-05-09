import httpx
from token_manager import get_token

NUMBERS_URL = "http://127.0.0.1:9000/api/numbers"   #Affordmeds numbers endpoint

async def fetch_numbers():
    token = await get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient(timeout=0.5) as client:  # 500ms timeout
        response = await client.get(NUMBERS_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        print("debugLine: Received JSON response from company server:", data)

        return data
