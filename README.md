# Capital Time API

This returns the current local time and UTC offset for a capital city. The API is protected with a token and is hosted on a Google Cloud VM.

## What it Does

- You provide the name of a capital city in the URL
- The API returns the local time and UTC offset for that city
- If the city is not in the database or the token is missing or incorrect, it returns an error message

## Authorization

All requests must include the following header:

Authorization: Bearer supersecrettoken123

If the token is missing or incorrect, the API will return:

{
  "error": "Unauthorized"
}

## How to Use the API

URL format:

http://[YOUR_VM_IP]:5000/api/secure-data?city=CityName

Replace [YOUR_VM_IP] with your Google Cloud VM external IP.


## Supported Cities

- Paris
- London
- Washington
- Tokyo
- Delhi
- Canberra

## Example Request (Using curl)

curl -H "Authorization: Bearer supersecrettoken123" "http://[YOUR_VM_IP]:5000/api/secure-data?city=Paris"

## Example Success Response

{
  "city": "Paris",
  "local_time": "2025-04-20 23:12:45",
  "utc_offset": "+0200"
}

## Example Errors

Missing city:

{
  "error": "Please provide a capital city using ?city=CityName"
}

City not found:

{
  "error": "Atlantis not found in our list. Try another capital."
}

Missing or wrong token:

{
  "error": "Unauthorized"
}
