import requests
import re
import json

def check_balance(login, password):
    url = 'http://my3.webcom.mobi/json/balance.php'
    headers = {'Content-type': 'text/json; charset=utf-8'}

    data = {'login': login,
            'password': password}
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            print(f'Баланс: {response_data['money']} руб.')
        else:
            print(f'Ошибка: {response.status_code}')
    except Exception as e:
        print(f'Произошла ошибка: {e}')


def validate_phone_number(phone_number):
    pattern = r'^79\d{9}$'
    return bool(re.match(pattern, phone_number))

user = 'A'
password = 'parol'
sender = 'python'
receiver = '79127855659'
text = 'Hello world!'

if not validate_phone_number(receiver):
    print('Ошибка! Некорректный номер телефона')
else:
    url = f'https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}'
    print(url)
    try:
        response = requests.get(url)
        print(response)

        if response.status_code == 200:
            print('Успешно')
        else:
            print(f'Ошибка {response.status_code}')
    except Exception as e:
        print(f'Ошибка: {e}')