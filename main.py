import requests

user = 'python24'
password = 'parol'
sender = 'python24'
receiver = '79177856789'
text = 'Hello world!'

url = f'https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}'
print(url)
response = requests.get(url)
print(response)

if response.status_code == 200:
    print('Успешно')
else:
    print(f'Ошибка {response.status_code}')