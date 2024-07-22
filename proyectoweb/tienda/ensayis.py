import requests

url = "https://numbers-to-words1.p.rapidapi.com/api/converter/"

payload = {
	"number": 141.2234,
	"delete_from_sentence": None,
	"currency": "euros",
	"decimal_currency": "millimes",
	"separator": "et",
	"decimal": 3,
	"language": "fr"
}
headers = {
	"x-rapidapi-key": "3f8f9c086bmsh2560f35958e2861p187b94jsn45c4186b790d",
	"x-rapidapi-host": "numbers-to-words1.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())