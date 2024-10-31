import requests

user = 'A'
password = 'parol'
sender = 'python'
receiver = '79127855656'
text = 'Hello world!'
try:
    url = f'https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}'
    print(url)
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        print('Успешно')
    else:
        print(f'Ошибка {response.status_code}')
except Exception as e:
    print(f'Ошибка: {e}')