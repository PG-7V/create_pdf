# import PySimpleGUI as sg
# # set global options for window
# background = '#F0F0F0'
# sg.SetOptions(background_color=background,
#     element_background_color=background,
#     text_element_background_color=background,
#     window_location=(0, 0),
#     margins=(0,0),
#     text_color = 'Black',
#     input_text_color ='Black',
#     button_color = ('Black', 'gainsboro'))
#
# layout = [[sg.Button('Ok'), sg.Button('Cancel')]]
#
# window = sg.Window('Test Window', layout, grab_anywhere=False, size=(800, 480), return_keyboard_events=True, finalize=True)
#
# window.Maximize()
# window.BringToFront()
# while True:
#     event, values = window.read()
#     if event in (None, 'Cancel'):
#         break
#     else:
#         sg.Popup('Ok clicked', keep_on_top=True)


import PySimpleGUI as sg
"""
    Demo - 2 simultaneous windows using read_all_window

    Window 1 launches window 2
    BOTH remain active in parallel

    Both windows have buttons to launch popups.  The popups are "modal" and thus no other windows will be active

    Copyright 2020 PySimpleGUI.org
"""

def make_win1():
    layout = [[sg.Text('This is the FIRST WINDOW'), sg.Text('      ', k='-OUTPUT-')],
              [sg.Text('Click Popup anytime to see a modal popup')],
              [sg.Button('Launch 2nd Window'), sg.Button('Popup'), sg.Button('Exit')]]
    return sg.Window('Window Title', layout, location=(800,600), finalize=True)


def make_win2():
    layout = [[sg.Text('The second window')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(25,1), k='-OUTPUT-')],
              [sg.Button('Erase'), sg.Button('Popup'), sg.Button('Exit')]]
    return sg.Window('Second Window', layout, finalize=True)

window1, window2 = make_win1(), None        # start off with 1 window open

while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'Popup':
        sg.popup('This is a BLOCKING popup','all windows remain inactive while popup active')
    elif event == 'Launch 2nd Window' and not window2:
        window2 = make_win2()
    elif event == '-IN-':
        window['-OUTPUT-'].update(f'You enetered {values["-IN-"]}')
    elif event == 'Erase':
        window['-OUTPUT-'].update('')
        window['-IN-'].update('')
window.close()

