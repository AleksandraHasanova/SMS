import requests
import re
import json
from tkinter import *
from tkinter import messagebox as mb


def check_balance(login, password):
    url = 'http://my3.webcom.mobi/json/balance.php'
    headers = {'Content-type': 'text/json; charset=utf-8'}

    data = {'login': login,
            'password': password}
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            return response_data['money']
        else:
            mb.showerror('Ошибка', f'Ошибка: {response.status_code}')
            return None
    except Exception as e:
        mb.showerror('Ошибка',f'Произошла ошибка: {e}')


def validate_phone_number(phone_number):
    pattern = r'^79\d{9}$'
    return bool(re.match(pattern, phone_number))

def send_sms():
    user = 'A'
    password = 'parol'
    sender = 'python'
    receiver = receiver_entry.get()
    text = text_entry.get(1.0, END)

    if len(text) > 160:
        mb.showerror('Ошибка', f'Длина вашего сообщения {len(text)}, она не может превышать 160 символов')
        return
    balance = check_balance(user, password)
    if balance:
        if float(balance) > 10:
            if not validate_phone_number(receiver):
                mb.showerror('Ошибка!', 'Некорректный номер телефона')
            else:
                url = f'https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}'
                try:
                    response = requests.get(url)

                    if response.status_code == 200:
                        mb.showinfo('Успешно', 'Сообщение успешно отправлено')
                    else:
                        mb.showerror('Ошибка', f'Ошибка {response.status_code}')
                except Exception as e:
                    mb.showerror('Ошибка', f'Ошибка: {e}')
        else:
            mb.showinfo('Недостаточно средств','Баланс меньше 10 рублей')
    else:
        mb.showerror('Ошибка','Не удалось получить информацию о балансе')


window = Tk()
window.title('Отправка СМС')
window.geometry('300x270')

Label(text='Номер получателя в формате: 79*********').pack()
receiver_entry = Entry()
receiver_entry.pack(pady=10)

Label(text='Введите текст СМС').pack()
text_entry = Text(width=30, height=7)
text_entry.pack(pady=10)

send_button = Button(text='Отправить СМС', command=send_sms)
send_button.pack(pady=10)

window.mainloop()