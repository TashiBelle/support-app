import PySimpleGUI as sg
import time

sg.theme('DarkPurple1')

# testing view of layouts only
# see welcome-screen.py here or test-psg.py on local for whole script

# blank to test transition buttons
blankLayout = [
    [sg.Text("")]
]

# welcLayout good - "▶" fn'ing
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

# feelsLayout good - need to connect buttons to screens
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

# deadBabyLayout not started
# ventLayout not started
# storyLayout not started
# playlistLayout not started
# copeLayout not started
# valuesLayout not started
# motMsgLayout not started
# roastLayout not started
# miniGameLayout not started
# brutalDeathsLayout not started

welcWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", welcLayout, size=(500,400)).finalize()
testWindow = None
blankWindow = None

# give the GUI a breather
time.sleep(0.1)

while True:
    try:
        window, event, values = sg.read_all_windows()
    except:
        continue
    
    # if welcome screen is closed directly
    if window == welcWindow and event == sg.WINDOW_CLOSED:
        welcWindow.close()
        if testWindow:
            testWindow.close()
        break
    
    # if "▶" is clicked from welcWindow
    if window == welcWindow and event == "▶":
        testWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", testLayout, size=(500,400)).finalize()
        welcWindow.hide()
    
    # if "▶" is clicked from testWindow
    if testWindow and window == testWindow and event == "▶":
        blankWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", blankLayout, size=(500,400)).finalize()

    # close the blankWindow during testing properly
    if blankWindow and window == blankWindow and event == sg.WINDOW_CLOSED:
        blankWindow.close()
        if testWindow:
            testWindow.close()
        break

    # if "test close" button is pressed in whatever layout is being tested
    if testWindow and window == testWindow and (event == sg.WINDOW_CLOSED or event == "test close"):
        testWindow.close()
        break
    
    
    
    # if "fine." is clicked from feelsWindow -> deadBabyWindow or ventWindow
    # if ">__<" is clicked from feelsWindow -> storyWindow or playlistWindow
    # if "drowning..." is clicked from feelsWindow -> copeWindow or valuesWindow
    # if "dO i HaVe a PerSoNaLitY dIsORdEr?" is clicked from feelsWindow -> motMsgWindow or roastWindow
    # if "*makin' moltovs*" is clicked from feelsWindow -> miniGameWindow or brutalDeathsWindow