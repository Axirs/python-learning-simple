import requests
import json

based_url = "https://openlibrary.org/search.json"

def book():
    my_param = {"title": "Harry Potter", "page": 1}

    response = requests.get(based_url, params=my_param)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))
        
book()
