from tkinter import *
from tkinter.ttk import Checkbutton, Radiobutton, Combobox

#https://pythonru.com/uroki/obuchenie-python-gui-uroki-po-tkinter
#https://ts-python.fandom.com/ru/wiki/Tkinter_ttk_(модуль)
#https://lavrynenko.com/tkinter-chto-eto-s-primerami-na-russkom/
#https://ru.wikiversity.org/wiki/Курс_по_библиотеке_Tkinter_языка_Python

def clicked():
    lbl.configure(text=selected.get())
    #lbl.configure(text=combo.get())
    print(season.get())
    print(view_price.get())
    print(chk_state.get())
    print(quantity.get())

window = Tk()
window.title("Template Test")
window.geometry('400x250')

season_text = Label(window, text='Категория')
quantity_text = Label(window, text='Наличие')
view_price_text = Label(window, text='Отображение цены')

chk_state = BooleanVar()
chk_state.set(False)  # задайте проверку состояния чекбокса
chk = Checkbutton(window, text='Выбрать', var=chk_state)
chk.grid(column=0, row=0)

season = Combobox(window)
season['value'] = ("Все платья", "Весна", "Лето", "Осень", "Зима")
season.current(0)

view_price = Combobox(window)
view_price['value'] = ("Отобразить", "Скрыть")
view_price.current(0)

quantity = Combobox(window)
quantity['value'] = ("Все", "В наличии")
quantity.current(0)

spin = Spinbox(window, from_=0, to=100, width=10)

selected = IntVar()
rad1 = Radiobutton(window, text='Первый', value=1, variable=selected)
rad2 = Radiobutton(window, text='Второй', value=2, variable=selected)
rad3 = Radiobutton(window, text='Третий', value=3, variable=selected)
btn = Button(window, text="Клик", command=clicked)
lbl = Label(window)
rad1.grid(column=1, row=0)
rad2.grid(column=2, row=0)
rad3.grid(column=3, row=0)
btn.grid(column=5, row=0)
lbl.grid(column=0, row=1)
spin.grid(column=1, row=1)

season.grid(column=1, row=3)
season_text.grid(column=0, row=3)
view_price_text.grid(column=0, row=4)
view_price.grid(column=1, row=4, sticky=W, padx=10, pady=10)
quantity_text.grid(column=0, row=5, padx=(10, 100))
quantity.grid(column=1, row=5, padx=(10, 100))





window.mainloop()


# collection = ""
# proc = int(input("Введите размер от искомого:"))
# name_output_catalog = str(input("Введите имя каталога:"))
# if_quantity = create_bool(str(input("Отобразить по наличию? Да/Нет:")))
# if_material = create_bool(str(input("Ткань отображать? Да/Нет:")).lower())
# if_collection = create_bool(str(input("Отображать поры года?Да/Нет")))
# if if_collection:
#     collection = str(input("Введите сезоны для отображения:"))
# if_characteristics = create_bool(str(input("Отображать состав? Да/Нет:")))
# if_descr = create_bool(str(input("Размеры отображать? Да/Нет:")).lower())
# descr_resize = 0
# if_price_resize = 100
# if if_descr:
#     if_descr_resize = create_bool(str(input("Размеры изменять? Да/Нет:")).lower())
#     if if_descr_resize:
#         descr_resize = int(input("Введите число изменения размеров:"))
# if_price = create_bool(str(input("Отображать цену в каталоге? Да/Нет:")).lower())
# if if_price:
#     valute = str(input("Введите валюту (BY, RUR, EUR, USD:"))
#     if_price_resize = int(input("Введите коэфициент:"))
# if_create_logo = create_bool(str(input("Печатать логотип? Да/Нет:")).lower())