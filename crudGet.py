import requests
import json

class MakeApiCall:
    def get_data(self, api):
        response = requests.get(api)
        if response.status_code == 200:
            print("Successfully fetched the data")
            self.formatted_print(response.json())
        else:
            print(f"Error: {response.status_code}. Failed to fetch data")
            print("Response Content:", response.content)
    
    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self,api):
        self.get_data(api)

api_call = MakeApiCall("https://fakestoreapi.com/products/1")  