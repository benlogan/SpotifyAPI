const request = require('request');

// Define your client_id and client_secret
const client_id = 'YOUR_CLIENT_ID';
const client_secret = 'YOUR_CLIENT_SECRET';

// Encode client_id and client_secret
const credentials = Buffer.from(`${client_id}:${client_secret}`).toString('base64');

// Define the token request parameters
const tokenUrl = 'https://accounts.spotify.com/api/token';
const headers = {
  'Authorization': `Basic ${credentials}`,
  'Content-Type': 'application/x-www-form-urlencoded',
};
const data = {
  grant_type: 'client_credentials',
};

// Send a POST request to get the token
request.post({
  url: tokenUrl,
  headers: headers,
  form: data
}, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    // Parse the response JSON
    const token_data = JSON.parse(body);
    // Extract the access token from the response data
    const access_token = token_data.access_token;
    console.log(`Access Token: ${access_token}`);
  } else {
    // Print an error message if the request was not successful
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
  }
});
