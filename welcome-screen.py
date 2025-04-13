import PySimpleGUI as sg
import time
import random

sg.theme('DarkPurple1')

# layouts
welcLayout = [
    [sg.Column(
        [
            [sg.Text("────⋆˖⁺‧₊☽◯☾₊‧⁺˖⋆────", justification='center', font=('Courier', 20))],
            [sg.Text("Ready to get started?", justification='center', font=('Courier', 20))],
            [sg.Button("▶", size=(3,1), font=('Courier', 20))]],
        justification='center',
        element_justification='center',
        expand_x=True
    )]
]

feelsLayout = [
    [sg.Column(
        [
            [sg.Text("So...how ya feelin'?", justification='center', font=('Courier', 20))],
            [sg.Button("fine.", size=(5,1), font=('Courier', 12))],
            [sg.Button(">__<", size=(5,1), font=('Courier', 12))],
            [sg.Button("drowning...", size=(12,1), font=('Courier', 12))],
            [sg.Button("dO i HaVe a PerSoNaLitY dIsORdEr?", size=(40,1), font=('Courier', 12))],
            [sg.Button("*makin' moltovs*", size=(20,1), font=('Courier', 12))]
        ],
        justification='center',
        element_justification='center',
        expand_x=True
    )]
]

# acknowlLayout good - connect button to next (randoly chosen based on pre sel) screen
# add dictionary to randomize "that's rough, buddy" msg
acknowlLayout = [
    [sg.Column(
        [
            [sg.Text(" ", size=(1,3))],
            [sg.Text("That's rough, buddy.", justification='center', font=('Courier', 18))],
            [sg.Text(" ", size=(1,1))],
            [sg.Button("▶", size=(12,1), font=('Courier', 12))]
        ],
        justification='center',
        element_justification='center',
        expand_x=True
    )]
]


welcWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", welcLayout, size=(500,400)).finalize()
feelsWindow = None

# give the GUI a breather
time.sleep(0.1)

# now let's practice swtiching to a new window upon button click

while True:
    try:
        window, event, values = sg.read_all_windows()
    except:
        continue
    
    # if welcome screen is closed directly
    if window == welcWindow and event == sg.WINDOW_CLOSED:
        welcWindow.close()
        if feelsWindow:
            feelsWindow.close()
        break
    
    # if "▶" is clicked from welcWindow
    if window == welcWindow and event == "▶":
        feelsWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", feelsLayout, size=(500,400)).finalize()
        welcWindow.hide()
    
    # if "fine." is clicked from feelsWindow -> deadBabyWindow or ventWindow
    # if ">__<" is clicked from feelsWindow -> storyWindow or playlistWindow
    # if "drowning..." is clicked from feelsWindow -> copeWindow or valuesWindow
    # if "dO i HaVe a PerSoNaLitY dIsORdEr?" is clicked from feelsWindow -> motMsgWindow or roastWindow
    # if "*makin' moltovs*" is clicked from feelsWindow -> miniGameWindow or brutalDeathsWindow
    if feelsWindow and window == feelsWindow and (event == sg.WINDOW_CLOSED or (event == "fine." or event ==">__<" or event == "drowning..." or event == "dO i HaVe a PerSoNaLitY dIsORdEr?" or event == "*makin' moltovs*")):
        feelsWindow.close()
        break
