import tkinter as tk
import tkinter.ttk as ttk

# --- functions ---

def on_select(event=None):
    print('----------------------------')

    if event: # <-- this works only with bind because `command=` doesn't send event
        print("event.widget:", event.widget.get())

    for i, x in enumerate(all_comboboxes):
        print("all_comboboxes[%d]: %s" % (i, x.get()))

# --- main ---

root = tk.Tk()

values = {"RadioButton 1" : "1",
        "RadioButton 2" : "2",
        "RadioButton 3" : "3",
        "RadioButton 4" : "4",
        "RadioButton 5" : "5"}

for (text, value) in values.items():
    ttk.Radiobutton(root, text = text,
        value = value).pack(ipady = 5)


all_comboboxes = []

cb = ttk.Combobox(root, values=("1", "2", "3", "4", "5"))
cb.set("1")
cb.pack()
cb.bind('<<ComboboxSelected>>', on_select)

all_comboboxes.append(cb)

cb = ttk.Combobox(root, values=("A", "B", "C", "D", "E"))
cb.set("A")
cb.pack()
cb.bind('<<ComboboxSelected>>', on_select)

cl = ttk.Label(root, text="Текст лэйбл")
cl.pack()


cr = ttk.Radiobutton(root, text='Sale')
cr.pack()
all_comboboxes.append(cb)

b = tk.Button(root, text="Show all selections", command=on_select)
b.pack()

root.mainloop()