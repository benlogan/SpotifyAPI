import requests

# Define the API URL
# 4dpARuHxo51G3z768sgnrY (Adele)
# 6eUKZXaKkcviH0Ku9w2n3V (Ed Sheeran)
url = 'https://api.spotify.com/v1/artists/6eUKZXaKkcviH0Ku9w2n3V'

# Define the headers with the Authorization token
headers = {
    'Authorization': 'Bearer X'
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the response data
    print(data)
    print(data['followers']['total'])
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")
