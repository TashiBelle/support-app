import PySimpleGUI as sg

layout = [[sg.Text("Hey, Tashi!")], [sg.Button("Close")]]

window = sg.Window("Test GUI", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Close":
        break

window.close()