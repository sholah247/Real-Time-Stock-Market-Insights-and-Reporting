import requests
import json

json_response = []

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"datatype":"json","output_size":"compact","interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":"MSFT"}

headers = {
	"x-rapidapi-key": "0ab1f07ab0mshfe5d0329fc817f5p115dcejsn9cd0b62f8cca",
	"x-rapidapi-host": "alpha-vantage.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

json_response.append(data)

print(json.dumps(json_response, indent = 3))

#print(response.json())