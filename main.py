import requests
import re

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