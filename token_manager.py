import httpx
import time

TOKEN_URL = "http://20.244.56.144/evaluation-service/auth"  #Affordmeds token endpoint
USERNAME = "reevan"
PASSWORD = "dmello"

AUTH_PAYLOAD = {
    "email": "reevandmello@gmail.com",
    "name": "reevan d mello",
    "rollNo": "4so22ai047",
    "accessCode": "KjJAxP",
    "clientID": "52c67b27-de13-4f9a-9689-25e9f03902b0",
	"clientSecret": "sQFUMHxpypbQuSZq",
}

# Store token and expiry time
_token = None
_token_expiry = 0

async def get_token():
    global _token, _token_expiry

    current_time = time.time()

    # If token is expired or doesn't exist, fetch a new one
    if _token is None or current_time >= _token_expiry:
        async with httpx.AsyncClient() as client:
            response = await client.post(TOKEN_URL, json=AUTH_PAYLOAD)
            response.raise_for_status()
            data = response.json()

            print("debugLine: Affordmeds token response =", data)

            _token = data["access_token"]
            _token_expiry = data["expires_in"] - 10  # 10 sec buffer

    return _token
