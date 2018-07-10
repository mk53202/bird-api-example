import requests

url = "https://api.bird.co/user/login"

body_payload = "{\"email\": \"yourmom@aol.com\"}" # Use unique email!
device_GUID = "12345678-12ab-34cd-56ef-fhdhfdjh8w8d" # Random generated unique 16bit GUID

headers = {
    'Platform': "ios",
    'Device-id': device_GUID,
    'Content-type': "application/json",
    'Cache-Control': "no-cache"
}

response = requests.request("POST", url, data=body_payload, headers=headers)

print(response.text) # If an unique email is used, it will return a token for the GET request in show-birds.py
