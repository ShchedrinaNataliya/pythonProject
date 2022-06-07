
import requests
import json



URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(URL)
dict_json = json.loads(response.text)

dollars = dict_json['Valute']['USD']['Value']
euros = dict_json['Valute']['EUR']['Value']
pound = dict_json['Valute']['GBP']['Value']

print('USD', dollars)
print('EUR', euros)
print('GBP', pound)