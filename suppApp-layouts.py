# testing one layout and window at a time...

import PySimpleGUI as sg
import time
import random

sg.theme('DarkPurple1')

# blanks to test transition buttons
blankLayout = [
    [sg.Column(
        [[sg.Button("done", size=(5,1), font=('Courier', 12))]],
        justification='center',
        element_justification='center',
        expand_x=True
    )]
]

blank2Layout = [    
    [sg.Column(
        [[sg.Button("▶", size=(3,1), font=('Courier', 20))]],
        justification='center',
        element_justification='center',
        expand_x=True
    )]
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

#feelsLayout -- layout good; buttons good; trans to acknowlLayout good; saves input good
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

# !!!! Add back button
# acknowlLayout -- layout good; cont. button good; trans to rand. window based on input from feelsLayout good
acknowlLayout = [
    [sg.Column(
        [
            [sg.Text(" ", size=(1,3))],
            [sg.Text("That's rough, buddy.", justification='center', font=('Courier', 18))],
            [sg.Text(" ", size=(1,1))],
            [sg.Button("▶", size=(3,1), font=('Courier', 20))]
        ],
        justification='center',
        element_justification='center',
        expand_x=True
    )]
]

# checkLayout -- layout good, popups working (not formatted well), buttons good 
checkLayout = [
    [sg.Column(
        [
            [sg.Text("Sooooo...feelin' any better?", justification='center', font=('Courier', 18))],
            [sg.Button("Yeh :)", size=(6,1), font=('Courier', 12)),
             sg.Text("          ", justification='center', font=('Courier', 12)),
             sg.Button("no.", size=(3,1), font=('Courier', 12))]
        ],
        justification='center',
        element_justification='center',
        expand_x=True
    )]
]

# feelsLayout2 not started -- blank!
feels2Layout = [    
    [sg.Column(
        [[sg.Button("▶", size=(3,1), font=('Courier', 20))]],
        justification='center',
        element_justification='center',
        expand_x=True
    )]
]

# successPopLayout not started
# deadBabLayout not started
# storyLayout not started
# copingOptsLayout not started
# guidedMedLayout not started
# 54321Layout not started
# tippLayout not started
# monModLayout not started
# trainLayout not started
# miniGameLayout not started
# ventLayout not started
# deathsLayout not started
# deathsPopLayout not started
# playlistLayout not started
# valuesLayout not started
# roastLayout not started
# motMsgsLayout not started
# followUpLayout not started
# monModPopLayout not started
# suppRejPopLayout not started


welcWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", welcLayout, size=(500,400)).finalize()
testWindow = None
acknowlWindow = None
feelsWindow = None
checkWindow = None
feels2Window = None
followUpWindow = None

deadBabWindow = None #testing with feelsWindow and acknowlWindow, placeholders for activity vvv
ventWindow = None 
storyWindow = None
playlistWindow = None
copingOptsWindow = None
valuesWindow = None
motMsgsWindow = None
roastWindow = None
gameWindow = None
deathsWindow = None

blankWindow = None #testing screen needed to replace unmade follow-up screens

open_windows = [
    welcWindow, 
    testWindow, 
    acknowlWindow, 
    feelsWindow,
    checkWindow,
    feels2Window,
    followUpWindow,
    deadBabWindow,
    ventWindow,
    storyWindow,
    playlistWindow,
    copingOptsWindow,
    valuesWindow,
    motMsgsWindow,
    roastWindow,
    gameWindow,
    deathsWindow,
    blankWindow]

feelInput = None #records input from feelsLayout emotion
checkInput = None #decides whether to go back to welc or go to feels2

def make_followup_layout():
    return[[
        sg.Column(
            [[sg.Button("continue", size=(10,1), font=('Courier', 12))]],
            justification='center',
            element_justification='center',
            expand_x=True
        )
    ]]

# give the GUI a breather
time.sleep(0.1)


while True:
    try:
        window, event, values = sg.read_all_windows()
    except:
        continue
    
    # close all the damn windows when X clicked
    if event == sg.WINDOW_CLOSED:
        for win in open_windows:
            if win:
                win.close()
        break
    
    # trans to testWindow when "▶" is clicked from welcWindow
    if window == welcWindow and event == "▶":
        feelsWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", feelsLayout, size=(500,400)).finalize()
        welcWindow.hide()
    
    # trans to acknowlWindow when any button is clicked from feelsLayout (testWindow)
    if feelsWindow and window == feelsWindow:
        if event in ("fine.", ">__<", "drowning...", "dO i HaVe a PerSoNaLitY dIsORdEr?", "*makin' moltovs*"):
            feelInput = event
            acknowlWindow = sg.Window (f"{event}", acknowlLayout, size=(500,400)).finalize()
            feelsWindow.close()

    # trans to rand sel on next screen after "▶" is clicked from acknowlWindow
    if acknowlWindow and window == acknowlWindow and event == "▶":
        acknowlWindow.close()
        
        if feelInput == "fine.":
            next_screen = random.choice(["fine1", "fine2"])
            if next_screen == "fine1":
                # placeholder for deadBabWindow
                deadBabWindow = sg.Window("fine1", blankLayout, size=(500,400)).finalize()
            else:
                # placeholder for ventWindow
                ventWindow = sg.Window("fine2", blankLayout, size=(500,400)).finalize()
                
        elif feelInput == ">__<":
            next_screen = random.choice([">__<1", ">__<2"])
            if next_screen == ">__<1":
                # placeholder for storyWindow
                storyWindow = sg.Window(">__<1", blankLayout, size=(500,400)).finalize()
            else:
                # placeholder for playlistWindow
                playlistWindow = sg.Window(">__<2", blankLayout, size=(500,400)).finalize()
                
        elif feelInput == "drowning...":
            next_screen = random.choice(["drown1, drown2"])
            if next_screen == "drown1":
                # placeholder for copingWindow
                copingOptsWindow = sg.Window("drown1", blankLayout, size=(500,400)).finalize()
            else:
                # placeholder for valuesWindow
                valuesWindow = sg.Window("drown2", blankLayout, size=(500,400)).finalize()
                
        elif feelInput == "dO i HaVe a PerSoNaLitY dIsORdEr?":
            next_screen = random.choice(["persDis1", "persDis2"])
            if next_screen == "persDis1":
                # placeholder for motMsgsWindow
                motMsgsWindow = sg.Window("persDis1", blankLayout, size=(500,400)).finalize()
            else:
                # placeholder for roastWindow
                roastWindow = sg.Window("persDis2", blankLayout, size=(500,400)).finalize()
    
        else:
            next_screen = random.choice(["moltovs1", "moltovs2"])
            if next_screen == "moltovs1":
                # placeholder for gameWindow
                gameWindow = sg.Window("moltovs1", blankLayout, size=(500,400)).finalize()
            else:
                # placeholder for deathsWindow
                deathsWindow = sg.Window("moltovs2", blankLayout, size=(500,400)).finalize()
                
    # placeholder windows and "done" buttons for all activities during testing main screens
    if window and event == "done":
        if deadBabWindow:
            followUpWindow = sg.Window("placeholder for followUpLayout", make_followup_layout(), size=(500,400)).finalize()
            deadBabWindow.close()
        elif ventWindow:
            followUpWindow = sg.Window("placeholder for followUpLayout", make_followup_layout(), size=(500,400)).finalize()
            ventWindow.close()
        elif storyWindow:
            followUpWindow = sg.Window("placeholder for followUpLayout", make_followup_layout(), size=(500,400)).finalize()
            storyWindow.close()
        elif playlistWindow:
            followUpWindow = sg.Window("placeholder for followUpLayout", make_followup_layout(), size=(500,400)).finalize()
            playlistWindow.close()
        elif copingOptsWindow:
            followUpWindow = sg.Window("placeholder for followUpLayout", make_followup_layout(), size=(500,400)).finalize()
            copingOptsWindow.close() 
        elif valuesWindow:
            followUpWindow = sg.Window("placeholder for followUpLayout", make_followup_layout(), size=(500,400)).finalize()
            valuesWindow.close() 
        elif motMsgsWindow:
            followUpWindow = sg.Window("placeholder for followUpLayout", make_followup_layout(), size=(500,400)).finalize()
            motMsgsWindow.close() 
        elif roastWindow:
            followUpWindow = sg.Window("placeholder for followUpLayout", make_followup_layout(), size=(500,400)).finalize()
            roastWindow.close() 
        elif gameWindow:
            followUpWindow = sg.Window("placeholder for followUpLayout", make_followup_layout(), size=(500,400)).finalize()
            gameWindow.close() 
        else:
            followUpWindow = sg.Window("placeholder for followUpLayout", make_followup_layout(), size=(500,400)).finalize()
            deathsWindow.close()
    
    if followUpWindow and window == followUpWindow and event == "continue":
        checkWindow = sg.Window("just checkin' in...", checkLayout, size=(500,400)).finalize()
        followUpWindow.close()
             
    if checkWindow and window == checkWindow:
        if event == "Yeh :)":
            checkInput = "yeh"
            sg.popup_ok("Yayyyyy!!! You'll now return to the welcome screen :)")
        else:
            checkInput == "naw"
            sg.popup_ok("Rada rada rada... let's try something else...")
        
        # ISSUE 1: welcLayout already used...can I just .reopen()?
        # ISSUE 2: how to handlre continuous loop back to feels2 as needed?
        if checkInput == "yeh":
            welcWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", welcLayout, size=(500,400)).finalize()
        else:
            feels2Window = sg.Window("placeholder for feels2Layout", feels2Layout, size=(500,400)).finalize()