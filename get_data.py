import requests
import json
from csv_loader import*

apiKey = '9203847529304875'

url = 'http://api.reimaginebanking.com/enterprise/merchants/accounts?key={}'.format(apiKey)
payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,
}
# Create a Savings Account
response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('account created')