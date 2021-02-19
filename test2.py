# import PySimpleGUI as sg
#
# layout = [[sg.Combo(['choice 1', 'choice 2', 'choice 3'], enable_events=True, key='combo')],
#           [sg.Button('Test'), sg.Exit()]
#           ]
#
# window = sg.Window('combo test', layout, size=(700, 500))
#
# while True:
#     event, values = window.Read()
#     if event is None or event == 'Exit':
#         break
#
#     if event == 'Test':
#         combo = values['combo']  # use the combo key
#         print(combo)
#
# window.Close()


import PySimpleGUI as sg

with sg.FlexForm('File Compare') as form:
    form_rows = [[sg.Text('Enter 2 files to comare')],
                 [sg.Text('File 1', size=(8, 1)), sg.InputText(), sg.FileBrowse()],
                 [sg.Text('File 2', size=(8, 1)), sg.InputText(), sg.FileBrowse()],
                 [sg.Submit(), sg.Cancel()]]

    button, values = form.LayoutAndShow(form_rows)

print(button, values)