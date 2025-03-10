import requests
import json

url = "https://my.api.mockaroo.com/sport_data.json?key=7dc3b8c0"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    with open(r"C:\Users\P15\Desktop\ETL\data\data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully in 'data.json'")
else:
    print(f"Error: {response.status_code}")
