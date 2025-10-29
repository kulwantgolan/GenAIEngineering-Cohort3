import requests
import json # readable format

url = "https://open-weather13.p.rapidapi.com/city"

querystring = {"city":"Adelaide","lang":"EN"}

headers = {
	"x-rapidapi-key": "ffdfa9e4e5msh09271debb0ed461p1648f4jsnf234664f6645",
	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(json.dumps(response.json(), indent=4))