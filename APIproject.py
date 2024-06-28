import requests

url = "https://tasty.p.rapidapi.com/recipes/list"
querystring = {"from":"0","size":"20","tags":"under_30_minutes"}

headers = {
	"x-rapidapi-key": "7268c35a14mshd1f8682123f484bp19d057jsnedc2299f51ed",
	"x-rapidapi-host": "tasty.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())