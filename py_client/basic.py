import requests


# endpoint = "https://httpbin.org/status/200/"
# endpoint ="https://httpbin.org/anything/anything"
endpoint = "http://127.0.0.1:8000/apix/"

get_response = requests.get(url=endpoint)  #Applcation  programming interface
# print(get_response.json())
# print(get_response.status_code)
print(get_response.json())
