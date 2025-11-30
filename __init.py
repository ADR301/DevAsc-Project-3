import requests

# api access keys
access_key = "661dab76849728d753a528454517fc99"

# ask user if they want to see their IP information
user_input = input("Would you like to see your IP information? (yes/no): ").strip().lower()

if user_input in ['yes', 'y']:
    url = f"https://api.ipapi.com/api/check?access_key={access_key}"

    try:
        # send request to api
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # print json
        data = response.json()

        print("\nRaw Values:\n")
        for key, value in data.items():
            print(f"{key}: {value}")

        # print selected values
        print("\nSelected Data:\n")
        print(f"IP: {data.get('ip')}")
        print(f"Country: {data.get('country_name')}")
        print(f"Region: {data.get('region_name')}")
        print(f"City: {data.get('city')}")
        print(f"ZIP: {data.get('zip')}")
        print(f"Latitude: {data.get('latitude')}")
        print(f"Longitude: {data.get('longitude')}")
        print(f"Flag: {data.get('location', {}).get('country_flag_emoji')}")
        print(f"Calling Code: +{data.get('location', {}).get('calling_code')}")
    
    except requests.exceptions.ConnectionError:
        print("\nError: Unable to connect to the API. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("\nError: The request timed out. Please try again later.")
    except requests.exceptions.HTTPError as e:
        print(f"\nError: HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"\nError: An error occurred while making the request: {e}")
    except ValueError:
        print("\nError: Unable to parse the API response.")
else:
    print("Okay, exiting program.")
