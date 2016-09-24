import requests
import json
from geopy.geocoders import Nominatim
from time import sleep
from csv_loader import*

apiKey = 'd5d5235772590ef035be0c3610f957a3'

url = 'http://api.reimaginebanking.com/enterprise/deposits?key={}'.format(apiKey)
header = {'content-type':'application/json'}

# Create a Savings Account
response = requests.get(
	url,
	headers=header,
	)

if response.status_code == 200:
	data = (json.loads(response.content.decode('utf-8')))
else:
	print(response.status_code)

output = []
index = 0
geolocator = Nominatim()

for deposit in data["results"]:
	if "transaction_date" in deposit:
		date = deposit["transaction_date"]
	else:
		continue
	amount = deposit["amount"]
	url2 = 'http://api.reimaginebanking.com/enterprise/accounts/{}?key={}'.format(deposit["payee_id"],apiKey)
	response2 = requests.get(
		url=url2,
		headers = header,
	)
	if response.status_code == 200:
		data2 = json.loads(response2.content.decode('utf-8'))
		if "customer_id" in data2:
			url3 = 'http://api.reimaginebanking.com/enterprise/customers/{}?key={}'.format(data2["customer_id"], apiKey)
			response3 = requests.get(
				url=url3,
				headers=header,
			)
		else:
			continue
	else:
		continue

	if response.status_code == 200:
		data3 = json.loads(response3.content.decode('utf-8'))
	else:
		continue
	address_info = data3["address"]
	address = address_info["street_number"]+' '+address_info["street_name"]+', '+address_info["city"]+', '+address_info["state"]
	print(address)

	location = geolocator.geocode(address)
	if location != None:
		output.append((index, location.latitude, location.longitude, amount, date))
		print(output)
	index += 1
	sleep(.15)
#id, long, lat, deposit_amount, timestamp