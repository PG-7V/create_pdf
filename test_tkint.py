from tkinter import *
from tkinter.ttk import Checkbutton, Radiobutton, Combobox

#https://pythonru.com/uroki/obuchenie-python-gui-uroki-po-tkinter
#https://ts-python.fandom.com/ru/wiki/Tkinter_ttk_(модуль)
#https://lavrynenko.com/tkinter-chto-eto-s-primerami-na-russkom/
#https://ru.wikiversity.org/wiki/Курс_по_библиотеке_Tkinter_языка_Python

def clicked():
    lbl.configure(text=selected.get())
    #lbl.configure(text=combo.get())
    a = season.get()
    print(a)

window = Tk()
window.title("Template Test")
window.geometry('400x250')

season_text = Label(window, text='Категория')

chk_state = BooleanVar()
chk_state.set(False)  # задайте проверку состояния чекбокса
chk = Checkbutton(window, text='Выбрать', var=chk_state)
chk.grid(column=0, row=0)

season = Combobox(window)
season['value'] = ("Все платья", "Весна", "Лето", "Осень", "Зима")
season.current(0)

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





window.mainloop()