import requests

url = "http://data.fixer.io/api/latest?access_key=0b1e4b2c4a8b47f333da4a930039ed6a"
rates = []
currency = []
response = requests.get(url)
json_data = response.json()
for i in json_data["rates"]:
    currency.append(json_data["rates"][i])

for olke, valyuta in zip(currency, json_data["rates"]):
    print("1 EUR=", olke, valyuta)
