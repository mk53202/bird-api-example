# Quick Bird example, need to add the routine to generate the auth_key
import requests

url = "https://api.bird.co/bird/nearby"
city_lat = "43.0500"
city_lon = "-87.8982"
city_radius = "1000"
auth_key = "XNlcl9pZCI6IjlmY2NjMGMxLTBkNzktNDA3Ni1hMTkyLp349Oc6Ik" # Not a real auth_key. use get-bird-auth.py to get one
device_GUID = "12345678-12ab-34cd-56ef-fhdhfdjh8w8d" # Random generated unique 16bit GUID

querystring = { "latitude" : city_lat, "longitude" : city_lon, "radius" : city_radius }

headers = {
    'Authorization': "Bird " + auth_key,
    'Device-id': device_GUID,
    'App-Version': "3.3.0",
    'Location': "{\"latitude\":43.0500,\"longitude\":-87.8982\"altitude\":500,\"accuracy\":100,\"speed\":-1,\"heading\":-1}",
    'Cache-Control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
