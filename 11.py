from tkinter import *
from tkinter import ttk, messagebox, filedialog, scrolledtext
from tkinter.ttk import Combobox

def calculaytor():
    digit1 = entry1.get()
    digit2 = entry2.get()
    znak = combobox.get()
    try:
        if znak == '+':
            answer = int(digit1) + int(digit2)
        elif znak == '-':
            answer = int(digit1) - int(digit2)
        elif znak == '*':
            answer = int(digit1) * int(digit2)
        elif znak == '/':
            answer = int(digit1) / int(digit2)
        answer_lable.configure(text=f'={answer}')
    except Exception as ex:
        answer_lable.configure(text='=Error!!!')


def radbuton():
    a = selector.get()
    if a == 1:
        messagebox.showinfo('Ты выбрал', 'Вариант №1')
    elif a == 2:
        messagebox.showinfo('Ты выбрал', 'Вариант №2')
    elif a == 3:
        messagebox.showinfo('Ты выбрал', 'Вариант №3')

def open_text():
    f = filedialog.askopenfilename(defaultextension='txt')
    with open(f, '+r') as file:
        a = file.read()
        text_window.insert(1.0, a)


#главное окно
main = Tk()
main.title('UB-41_Antonenko')
main.geometry('500x200')
main.resizable(height=False, width=False)


#разделение на вкладки
main_frame = ttk.Notebook(main)#поле для всех вкладок
zadanie1, zadanie2, zadanie3 = ttk.Frame(main_frame), ttk.Frame(main_frame), ttk.Frame(main_frame)
main_frame.add(zadanie1, text='Задание №1')
main_frame.add(zadanie2, text='Задание №2')
main_frame.add(zadanie3, text='Задание №3')
main_frame.pack(fill='both', expand=True)#как располагаются вкладки


#окно для задания 1
entry1 = Entry(zadanie1, width=10)
entry1.grid(row=1, column=1)

combobox = Combobox(zadanie1, width=1)
combobox['values'] = ('+', '-', '*', '/')
combobox.grid(row=1, column=2)

entry2 = Entry(zadanie1, width=10)
entry2.grid(row=1, column=3)

button = Button(zadanie1, text='Посчитать', command=calculaytor)
button.grid(row=2, column=1)

answer_lable = Label(zadanie1, text='=')
answer_lable.grid(row=1, column=4)


#окно для задания 2
selector = IntVar()#область хранения значения для rad_button

rad_button_1 = Radiobutton(zadanie2, text='Вариант №1', value=1, variable=selector)
rad_button_1.grid(row=1, column=1)

rad_button_2 = Radiobutton(zadanie2, text='Вариант №2', value=2, variable=selector)
rad_button_2.grid(row=1, column=2)

rad_button_3 = Radiobutton(zadanie2, text='Вариант №3', value=3, variable=selector)
rad_button_3.grid(row=1, column=3)

vibor = Button(zadanie2, text='Что именно я выбрал?', command=radbuton)
vibor.grid(row=1, column=4)


#окно для задания 3
but_otcr = Button(zadanie3, text='Открыть файл', command=open_text)
but_otcr.grid(row=1, column=1)

text_window = scrolledtext.ScrolledText(zadanie3, width=59, height=9, fg='blue')
text_window.grid(row=2, column=1)


main.mainloop()