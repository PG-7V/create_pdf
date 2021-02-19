import PySimpleGUI as sg
from PySimpleGUI import Checkbox, Button
layout = [
    [sg.Checkbox('checkbox', key = 'checkbox')],
    [sg.Button ('ON', key = 'ON')],
    [sg.Button ('OFF', key = 'OFF')]
]
window = sg.Window ('StackOverflow 265052', layout) .Finalize ()
while True: # Event Loop
    event, values = window.read(timeout=100)
    if event in (None, 'Exit'):
        break
    elif event == 'ON':
        window ['checkbox']. Update (value = True)
    elif event == 'OFF':
        window ['checkbox']. Update (value = False)
window.close ()