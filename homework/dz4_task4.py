
import requests
import json
import datetime as dt
import time


URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(URL)
dict_json = json.loads(response.text)

while True:
    start = dt.datetime.utcnow() + dt.timedelta(hours=3)
    res_dollars = f"Курс USD на {start} равен {dict_json['Valute']['USD']['Value']}"
    res_euros = f"Курс EUR на {start} равен {dict_json['Valute']['EUR']['Value']}"
    res_pound = f"Курс GBP на {start} равен {dict_json['Valute']['GBP']['Value']}"
    print(res_dollars)
    print(res_euros)
    print(res_pound)
    time.sleep(5)