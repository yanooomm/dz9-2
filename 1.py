import tkinter as tk
from tkinter import *
import calendar


def func():
    rt = tk.Tk()
    rt.title = ("Календарь")
    rt.geometry('250x220')
    year1 = int(year_entry.get())
    month1 = int(month_entry.get())
    cal = tk.Label(rt, text = calendar.month(year1, month1, 7, 2))
    cal.grid(row = 0, column = 1)
    rt.mainloop()

root = tk.Tk()
root.title("Календарь")
root.geometry('450x300')
year = tk.Label(root, text = "Введите год: ")
year.grid(row = 0, column = 0)
year_entry = tk.Entry(root)
year_entry.grid(row = 0, column = 1)
month = tk.Label(root, text = "Введите месяц: ")
month.grid(row = 1, column = 0)
month_entry = tk.Entry(root)
month_entry.grid(row = 1, column = 1)
button = tk.Button(root, text = "Посмотреть календарь", command = func)
button.grid(row = 2, column = 1)
root.mainloop()