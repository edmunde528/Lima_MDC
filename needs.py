import requests
import json 
fileObject = open("c:\\Python\\tigergraph\\needs.json", "r")
jsonContent = fileObject.read()
oldlist = json.loads(jsonContent)

url = r'https://www.givefood.org.uk/api/2/needs/'
r = requests.get(url)
response = r.json() + oldlist
unique_items = list({ request['id'] : request for request in response }.values())

with open("c:\\Python\\tigergraph\\needs.json", 'w') as f:
    json.dump(unique_items, f)