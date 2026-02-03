import requests
import json

# API URL
API_URL = "https://randomuser.me/api/"

def fetch_user_data():
    try:
        response = requests.get(API_URL)

        # Check HTTP status code
        if response.status_code == 200:
            data = response.json()

            # Save full response to file
            with open("api_response.json", "w") as file:
                json.dump(data, file, indent=4)

            # Extract required fields
            user = data["results"][0]
            name = user["name"]
            location = user["location"]

            print(" User Data Fetched Successfully\n")
            print(f"Name   : {name['title']} {name['first']} {name['last']}")
            print(f"Email  : {user['email']}")
            print(f"Phone  : {user['phone']}")
            print(f"Country: {location['country']}")

        else:
            print(f" Failed to fetch data. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(" API request failed")
        print(e)

# Run function
fetch_user_data()
