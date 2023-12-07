import requests


# endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "Hello World!"}) # application programming interface
print(get_response.json())
print(get_response.status_code)
