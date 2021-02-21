# Категория
# Отображение цены
# Отображение валюты
# Надбавка
# Множитель курса
# Изменение размеров
# Наличие
# С тканью
#
#         Sale New
#         Отображать состав

#
#
# Качество PDF

from tkinter import *
from tkinter.ttk import Checkbutton, Radiobutton, Combobox, Spinbox

def clicked():
    print(var.get())


window = Tk()
window.title("Template Test")
window.geometry('380x470')

# Категория
season_text = Label(window, text='Категория')
season = Combobox(window)
season['value'] = ("Все платья", "Весна", "Лето", "Осень", "Зима")
season.current(0)
season_text.grid(column=0, row=0, sticky=W, padx=10, pady=10)
season.grid(column=1, row=0, sticky=W, padx=10, pady=10)

# Отображение цены
view_price_text = Label(window, text='Отображение цены')
view_price = Combobox(window)
view_price['value'] = ("Отобразить", "Скрыть")
view_price.current(0)
view_price_text.grid(column=0, row=1, sticky=W, padx=10, pady=10)
view_price.grid(column=1, row=1, sticky=W, padx=10, pady=10)


# Отображение Валюты
if_price = Label(window, text='Отобразить валюту')
valute = Combobox(window)
valute['value'] = ('Нет', 'BY', 'RUR', 'EUR', 'USD')
valute.current(0)
if_price.grid(column=0, row=2, sticky=W, padx=10, pady=10)
valute.grid(column=1, row=2, sticky=W, padx=10, pady=10)


# Надбавка
if_price_resize_text = Label(window, text="Надбавка")
if_price_resize = Spinbox(window, from_=0, to=100, width=5)
if_price_resize_text.grid(column=0, row=3, sticky=W, padx=10, pady=10)
if_price_resize.grid(column=1, row=3, sticky=W, padx=10, pady=10)

# Наличие
quantity_text = Label(window, text='Наличие')
quantity = Combobox(window)
quantity['value'] = ("Все", "В наличии")
quantity.current(0)
quantity_text.grid(column=0, row=4, sticky=W, padx=10, pady=10)
quantity.grid(column=1, row=4, sticky=W, padx=10, pady=10)

# Ткань

if_material_text = Label(window, text="С тканью")
if_material = Combobox(window)
if_material['value'] = ("С тканью", "Скрыть")
if_material.current(0)
if_material_text.grid(column=0, row=5, sticky=W, padx=10, pady=10)
if_material.grid(column=1, row=5, sticky=W, padx=10, pady=10)

# Отобразить лого (Sale New)
if_create_logo_text = Label(window, text='Отображение цены')
if_create_logo = Combobox(window)
if_create_logo['value'] = ("Отобразить", "Скрыть")
if_create_logo.current(0)
if_create_logo_text.grid(column=0, row=6, sticky=W, padx=10, pady=10)
if_create_logo.grid(column=1, row=6, sticky=W, padx=10, pady=10)

# Отображать состав
if_characteristics_text = Label(window, text='Отображать состав')
if_characteristics = Combobox(window)
if_characteristics['value'] = ("Отобразить", "Скрыть")
if_characteristics.current(0)
if_characteristics_text.grid(column=0, row=7, sticky=W, padx=10, pady=10)
if_characteristics.grid(column=1, row=7, sticky=W, padx=10, pady=10)

# Качество PDF
proc_text = Label(window, text="Качество PDF")
var = IntVar()
var.set(50)
proc = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
proc_text.grid(column=0, row=8, sticky=W, padx=10, pady=10)
proc.grid(column=1, row=8, sticky=W, padx=10, pady=10)

btn = Button(window, text="Запустить", command=clicked)
lbl = Label(window)
btn.grid(column=1, row=9, padx=10, pady=10)


window.mainloop()