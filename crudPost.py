import requests
import json

def make_api_call():
    url = "https://fakestoreapi.com/products"
    data = {
        "title": "Testing Product",
        "price": 100,
        "description": "This is a test product"
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=data, headers=headers)
    print(response.json())
    print(f"StatusCode: {response.status_code}")
    
    
make_api_call()