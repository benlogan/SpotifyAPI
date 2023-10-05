import requests

# this retrieves the top new releases from Spotify
# then checks for each artist whether they are 'big'
# so that we have 'big' new albums!

def follower_count(artist_id):
    url = 'https://api.spotify.com/v1/artists/' + artist_id
    headers = {
        'Authorization': 'Bearer X'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['followers']['total']
    else:
        print(f"Error: {response.status_code} - {response.text}")

# how far back does this go? rolling history of this would be quite useful

# Define the API URL
url = 'https://api.spotify.com/v1/browse/new-releases?limit=50'

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

    one_million_follower_albums = 0
    ten_million_follower_albums = 0

    #print(data['followers']['total'])
    for album in data['albums']['items']:
        print(album['name'])
        print(album['release_date'])

        # only care about artists that are over so many followers (i.e. big albums)
        print(album['artists'][0]['name'])
        artist_id = album['artists'][0]['id']
        print(artist_id)
        followers = follower_count(artist_id)
        print(followers)
        if followers >= 1000000:
            print('album by an artists with 1m+ followers - INCLUDE')
            one_million_follower_albums += 1
        if followers >= 10000000:
            print('album by an artists with 10m+ followers - INCLUDE')
            ten_million_follower_albums += 1

        print('**********************************')
    print('Album Count : ' + str(len(data['albums']['items'])))
    print('one_million_follower_albums : ' + str(one_million_follower_albums))
    print('ten_million_follower_albums : ' + str(ten_million_follower_albums))

else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")