import requests
import json

url = 'http://my3.webcom.mobi/json/balance.php'
headers = {'Content-type': 'text/json; charset=utf-8'}

data={'login': 'A',
      'password': 'parol'}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    response_data = response.json()
    print(response_data)
    print(f'Баланс: {response_data['money']} руб.')
else:
    print(f'Ошибка: {response.status_code}')
