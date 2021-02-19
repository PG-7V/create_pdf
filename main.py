import PySimpleGUI as sg

column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [
    [sg.Text('File 1'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('MD5'), sg.Checkbox('SHA1')
     ],
    [sg.Text('File 2'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('SHA256')
     ],
    [sg.Text('Введите имя каталога'), sg.Checkbox('Lf')],
    [sg.Output(size=(88, 20))],

    [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25))],
    [sg.Text('Here is some text.... and a place to enter text')],
    [sg.InputText('This is my text')],
    [sg.Checkbox('Checkbox'), sg.Checkbox('My second checkbox!', default=True)],
    [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
     sg.Multiline(default_text='A second multi-line', size=(35, 3))],
    [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),
     sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
    [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
     sg.Column(column1, background_color='#F7F3EC')],
    [sg.Text('_'  * 80)],
    [sg.Text('Choose A Folder', size=(35, 1))],
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
     sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(), sg.Cancel()]
    ]
window = sg.Window('File Compare', layout)
while True:                             # The Event Loop
    event, values = window.read()
    print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        print('cool')


# import PySimpleGUI as sg
# from math import pi
#
#
# layout = [
#     [sg.Text("Введите высоту между r1 и r2:")], [sg.Input(key="-IN-0")],
#     [sg.Text("Введите r1:")], [sg.Input(key="-IN-1")],
#     [sg.Text("Введите r2:")], [sg.Input(key="-IN-2")],
#     [sg.Text("Результат в Литрах", size=(30, 1), key="-OUT-")],
#     [sg.Text('File Types')],
#     [sg.Radio('Python file (start.py)', 1, key='-PY-')],
#     [sg.Radio('Web app (script.js, index.html, styles.css)', 1, key='-WEB-')],
#     [sg.Text('Project Name:'), sg.InputText(key='-NAME-')],
#     [sg.Button("OK"), sg.Button("Выход")],
#     [sg.Button("Стереть все")],
# ]
#
# window = sg.Window("Вычислятель объема", layout)
#
# while True:
#     event, values = window.read()
#     if event == "OK":
#         # если поля пустые - ничего не делаем
#         if "" in [values["-IN-0"], values["-IN-1"], values["-IN-2"]]:
#             continue
#         h = float(values["-IN-0"])
#         r1 = float(values["-IN-1"])
#         r2 = float(values["-IN-2"])
#         x = (1 / 3) * pi * h * (r1 ** 2 + r1 * r2 + r2 ** 2)
#         window["-OUT-"].update(x)
#     elif event == "Стереть все":
#         window["-IN-0"].update("")
#         window["-IN-1"].update("")
#         window["-IN-2"].update("")
#         window["-OUT-"].update("")
#     if event == "Выход" or event == sg.WIN_CLOSED:
#         break
#
#
# window.close()

