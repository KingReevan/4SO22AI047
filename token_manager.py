import httpx
import time

TOKEN_URL = "http://127.0.0.1:9000/api/token"  #Affordmeds token endpoint
USERNAME = "reevan"
PASSWORD = "dmello"

# Store token and expiry time
_token = None
_token_expiry = 0

async def get_token():
    global _token, _token_expiry

    current_time = time.time()

    # If token is expired or doesn't exist, fetch a new one
    if _token is None or current_time >= _token_expiry:
        async with httpx.AsyncClient() as client:
            response = await client.post(TOKEN_URL, json={    #confirm the expected keys with Affordmed
                "username": USERNAME,
                "password": PASSWORD
            })
            response.raise_for_status()
            data = response.json()

            print("debugLine: Affordmeds token response =", data)

            _token = data["token"]  #adjust according to the response
            _token_expiry = current_time + (5 * 60) - 10  # buffer of 10s before expiry

    return _token
