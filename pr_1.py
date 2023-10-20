from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk()
root.geometry("600x400")
root.title("Тип треугольника")
root["bg"] = "#89cff0"


def check():
    try:
        if (entry_1.get() and entry_2.get() and entry_3.get()) != "":
            a = int(entry_1.get())
            b = int(entry_2.get())
            c = int(entry_3.get())
            if 10000 >= a > 0 and 10000 >= b > 0 and 10000 >= c > 0:
                if a < b + c and b < a + c and c < b + a:
                    if a == b == c:
                        label["text"] = "Равносторонний"
                    elif (a == b != c) or (a == c != b) or (b == c != a):
                        label["text"] = "Равнобедренный"
                    else:
                        label["text"] = "Разносторонний"
                else:
                    label["text"] = "Не выполнились условия треугольника"
            else:
                label["text"] = "Введите числа больше нуля\nи меньше 10000!"
        else:
            label["text"] = "Заполните поля!"
        btn["text"] = "Заново"
    except ValueError:
        label["text"] = "Это не треугольник"


label = ttk.Label(
    text='Введите длины сторон треугольника\nне больше значения "10000"',
    font="Candara 20", background="#89cff0", justify=tk.LEFT)
label.place(x=80, y=100)
entry_1 = ttk.Entry()
entry_1.place(height=30, width=150, x=50, y=200)
entry_2 = ttk.Entry()
entry_2.place(height=30, width=150, x=220, y=200)
entry_3 = ttk.Entry()
entry_3.place(height=30, width=150, x=390, y=200)
btn = tk.Button(text="Проверить", font="Candara 20", background="#ffffad",
                command=check)
btn.place(height=50, width=150, x=220, y=270)

root.mainloop()
