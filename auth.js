const axios = require('axios');
const base64 = require('base-64');

// Define your client_id and client_secret
const client_id = 'YOUR_CLIENT_ID';
const client_secret = 'YOUR_CLIENT_SECRET';

// Encode client_id and client_secret in base64
const base64Credentials = base64.encode(`${client_id}:${client_secret}`);

// Define the token request parameters
const tokenUrl = 'https://accounts.spotify.com/api/token';
const headers = {
  'Authorization': `Basic ${base64Credentials}`,
  'Content-Type': 'application/x-www-form-urlencoded',
};
const data = new URLSearchParams();
data.append('grant_type', 'client_credentials');

// Send a POST request to get the token
axios.post(tokenUrl, data, { headers })
  .then(response => {
    // Check if the request was successful (HTTP status code 200)
    if (response.status === 200) {
      // Extract the access token from the response data
      const access_token = response.data.access_token;
      console.log(`Access Token: ${access_token}`);
    } else {
      // Print an error message if the request was not successful
      console.error(`Error: ${response.status} - ${response.statusText}`);
    }
  })
  .catch(error => {
    // Handle any errors that occur during the request
    console.error(`Error: ${error.message}`);
  });
