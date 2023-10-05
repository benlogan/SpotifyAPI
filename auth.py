import base64
import requests

# using the 'Client Credentials' flow
# https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow
# this basically generates a Spotify API bearer token, using your client ID & secret

# Define your client_id and client_secret
client_id = ''
client_secret = ''

# Encode client_id and client_secret in base64
base64_credentials = base64.b64encode(f"{client_id}:{client_secret}".encode('utf-8')).decode('utf-8')

# Define the token request parameters
token_url = 'https://accounts.spotify.com/api/token'
headers = {
    'Authorization': f'Basic {base64_credentials}'
}
data = {
    'grant_type': 'client_credentials'
}

# Send a POST request to get the token
response = requests.post(token_url, headers=headers, data=data)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the response JSON
    token_data = response.json()
    # Extract the access token
    access_token = token_data.get('access_token')
    print(f'Access Token: {access_token}')
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")
