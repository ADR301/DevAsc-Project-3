import requests

# api access keys
access_key = "661dab76849728d753a528454517fc99"
url = f"https://api.ipapi.com/api/check?access_key={access_key}"

# send request to api
response = requests.get(url)

# print json
data = response.json()

print("\nUnformatted values:\n")
for key, value in data.items():
   print(f"{key}: {value}")

# print selected values
print("\nFormated Values:\n")
print(f"IP: {data.get('ip')}")
print(f"Country: {data.get('country_name')}")
print(f"Region: {data.get('region_name')}")
print(f"City: {data.get('city')}")
print(f"ZIP: {data.get('zip')}")
print(f"Latitude: {data.get('latitude')}")
print(f"Longitude: {data.get('longitude')}")
print(f"Flag: {data.get('location', {}).get('country_flag_emoji')}")
print(f"Calling Code: +{data.get('location', {}).get('calling_code')}")