import PySimpleGUI as sg

layout = [
    [sg.Text('User')],
    [sg.Input(key='User')],
    [sg.Text('Password')],
    [sg.Input(key='Password')],
    [sg.Button('login')],
    [sg.Text('', key='message')],
]

window = sg.Window('Login', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        password_aceppted = '1234'
        correct_user = 'MariaSales'
        user = values['User']
        password = values['Password']
        if password == password_aceppted and user == correct_user:
            window['message'].update('login sucessfully done')
        else:
            window['message'].update('incorrect password')