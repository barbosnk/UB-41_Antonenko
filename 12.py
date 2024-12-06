import tkinter as tk
from tkinter import Entry, Button, scrolledtext, messagebox
import requests


def start():
    e = entry.get()
    if e == '2':  # Проверка ввода
        username = "barbosnk"  # Имя пользователя github
        url = f"https://api.github.com/users/{username}"  # URL для запроса

        # Делаем запрос и получаем данные в формате JSON
        user_data = requests.get(url).json()

        # Форматируем данные для отображения
        a = {
            'company': user_data['company'],
            'created_at': user_data['created_at'],
            'email': user_data['email'],
            'id': user_data['id'],
            'name': user_data['name'],
            'url': user_data['html_url']  # Вместо 'url' используем 'html_url'
        }

        # Очищаем и вставляем данные в текстовое окно
        text_window.delete(1.0, tk.END)
        text_window.insert(1.0, f'{a}')
    else:
        text_window.delete(1.0, tk.END)  # Очищаем текстовое поле
        text_window.insert(1.0, 'ошибка ввода')  # Выводим сообщение об ошибке


# Создание главного окна
window = tk.Tk()
window.title('UB-41_Antonenko')
window.geometry('500x300')
window.resizable(height=False, width=False)

# Поле ввода
entry = Entry(window, width=30)
entry.grid(row=1, column=1)

# Кнопка запуска
button = Button(window, text='start', command=start)
button.grid(row=1, column=2)

# Текстовое окно для отображения данных
text_window = scrolledtext.ScrolledText(window, width=45, height=16, fg='blue')
text_window.grid(row=2, column=1)

# Запуск главного цикла обработки событий
window.mainloop()