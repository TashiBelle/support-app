import PySimpleGUI as sg
import time
import random

from app_dicts import welcGreetings
from app_dicts import acknowlMsgs
from app_dicts import checkinMsgs
from app_dicts import deadBabJokes
from app_dicts import storiesList
from app_dicts import playlistNames
from app_dicts import songsList
from app_dicts import valuesList
from app_dicts import roastList
from app_dicts import motMsgs
from app_dicts import followUpMsgs

sg.theme('DarkPurple1')


# empty variables for later
feelInput = None #records input from feelsLayout emotion
checkInput = None #decides whether to go back to welc or go to feels2


# layout functions
def make_blank_layout():
    return[[
        sg.Column(
            [
                [sg.Button("done", size=(5,1), font=('Courier', 12))]],
            justification='center',
            element_justification='center',
            expand_x=True
        )
    ]]

def make_feels_layout():
    return[[
        sg.Column(
            [
            [sg.Text("So...how ya feelin'?", justification='center', font=('Courier', 20))],
            [sg.Button("fine.", size=(40,1), font=('Courier', 12))],
            [sg.Button(">__<", size=(40,1), font=('Courier', 12))],
            [sg.Button("drowning...", size=(40,1), font=('Courier', 12))],
            [sg.Button("dO i HaVe a PerSoNaLitY dIsORdEr?", size=(40,1), font=('Courier', 12))],
            [sg.Button("*makin' moltovs*", size=(40,1), font=('Courier', 12))]
            # add 'none of these' button to randomly pick from all 10 activities
        ],
        justification='center',
        element_justification='center',
        expand_x=True
        )
    ]]

def make_welc_layout():
    return[[
        sg.Column(
            [
                [sg.Text("────⋆˖⁺‧₊☽◯☾₊‧⁺˖⋆────", justification='center', font=('Courier', 20))],
                # welcGreetings dict
                [sg.Text("Ready to get started?", justification='center', font=('Courier', 20))],
                [sg.Text(" ", font=('Courier', 20))],
                [sg.Button("▶", size=(10,1), font=('Courier', 18))]
            ],
        justification='center',
        element_justification='center',
        expand_x=True
        )
    ]]

def make_acknowl_layout():
    return[[
        sg.Column(
        [
            [sg.Text(" ", size=(1,3))],
            # acknowlMsgs dict
            [sg.Text("That's rough, buddy.", justification='center', font=('Courier', 18))],
            [sg.Text(" ", size=(1,1))],
            [sg.Button("▶", size=(10,1), font=('Courier', 12))]
        ],
        justification='center',
        element_justification='center',
        expand_x=True
        )
    ]]

def make_check_layout():
    return[[
        sg.Column(
        [
            # checkinMsgs dict
            [sg.Text("Sooooo...feelin' any better?", justification='center', font=('Courier', 18))],
            [sg.Text(" ", font=('Courier', 20))],
            [sg.Button("yeh :)", size=(6,1), font=('Courier', 12)),
             sg.Text("          ", justification='center', font=('Courier', 12)),
             sg.Button("no.", size=(3,1), font=('Courier', 12))]
        ],
        justification='center',
        element_justification='center',
        expand_x=True
        )
    ]]

def make_followup_layout():
    return[[
        sg.Column(
            [
                # followUpMsgs dict
                [sg.Text("Wow, look at you doing the thing!", justification='center', font=('Courier', 20))],
                [sg.Text("Deep breath...", justification='center', font=('Courier', 14))],
                [sg.Text(" ", font=('Courier', 20))],
                [sg.Button("continue", size=(10,1), font=('Courier', 12))]
            ],
            justification='center',
            element_justification='center',
            expand_x=True
        )
    ]]

def make_feels2_layout():
    return[[
        sg.Column(
        [
            [sg.Text("What would be most helpful right now?", justification='center', font=('Courier', 20))],
            [sg.Text(" ", font=('Courier', 20))],
            [sg.Combo(
                values=['Surprise Me',
                        'Dead Baby Jokes',
                        'Vent (scream in the void)',
                        'Storytime',
                        'Random Rage Playlist',
                        'Coping Strategy Reminders',
                        'Reminders of Your Value',
                        'Motivational Messaging',
                        'Roast Me',
                        'Mini Game',
                        'Imagine the Brutal Deaths of my Enemies'
                        ],
                default_value='Surprise Me',
                key='copingOpts_dropdown',
                font=('Courier', 12),
                size=(40,1),
                enable_events=True,
                readonly=True
            )],
            [sg.Text(" ", font=('Courier', 20))],
            [sg.Button("Ready!", size=(10,1), font=('Courier', 12))]
        ],
        justification='center',
        element_justification='center',
        expand_x=True
        )
    ]]

# make_deadBab_layout() not started: mid -- rand msg, click to reveal, refresh button ("Another?"), done button
    # deadBabJokes dict
    
# make_story_layout() not started: mid -- click to reveal, scrollbar, done button
    # storiesList dict
    
# make_copingOpts_layout -- ask if they need another coping rem (loop back to copingOptsWindow), done button
def make_copingOpts_layout():
    return[[
        sg.Column(
            [
                [sg.Text("Everyone needs a reminder every now and then ^_^", justification='center', font=('Courier', 12))],
                [sg.Text(" ", font=('Courier', 20))],
                [sg.Combo(
                    values=['Choose for me', 'Guided Meditation', '54321 Grounding', 'TIPP Cheat Sheet', 'What We Monitor, We Modify', 'Trainspotting Tracer'],
                    default_value='Choose for me',
                    key='stratsOpts_dropdown',
                    font=('Courier', 12),
                    size=(30,1),
                    enable_events=True,
                    readonly=True
                )],
                [sg.Text(" ", font=('Courier', 20))],
                [sg.Button("Let's begin", size=(15,1), font=('Courier', 12))]
            ],
            justification='center',
            element_justification='center',
            expand_x=True
        )
    ]]

# make_guidedMed_layout not started: hard (links/gifs) + are you sure? popup

# make_grounding_layout not started: mid + are you sure? popup

# make_tipp_layout not started: mid, images + are you sure? popup

# make_monMod_layout not started: mid + are you sure? popup

# make_train_layout not started: mid + are you sure? popup

# make_game_layout not started: hard...what the mother-forker

def make_vent_layout():
    return[[
        sg.Column(
            [
                [sg.Text("Go ahead. Let it all out.", 
                        justification='center',
                        font=('Courier', 14))],
                [sg.Text("Nothing you type will be saved, and this app has no internet access.", 
                        justification='left',
                        font=('Courier', 8))],
                [sg.Text("You're all good to say it like it is!", 
                        justification='left',
                        font=('Courier', 8))],
                [sg.Text("", font=('Courier', 8))],
                [sg.Multiline(
                    default_text='',
                    size=(50,15),
                    font=('Courier', 12),
                    key='ventBox',
                    border_width=2,
                    expand_x=True,
                    expand_y=True
                )],
                [sg.Text("", font=('Courier', 12))],
                [sg.Button("Done", size=(10,1), font=('Courier', 12))]
            ],
            justification='center',
            element_justification='center',
            expand_x=True
        )
    ]]

# make_deaths_layout not started: hard + are you sure? popup

# make_deathsPop_layout not started >> ?????????

# make_playlist_layout not started: mid -- rand5, refresh button ("Another?"), done button
    # playlistNames dict
    # songList dict

# make_values_layout not started: easy -- rand msg, refresh button ("Another?"), done button
    # valuesList dict

# make_roast_layout not started: mid -- rand msg, click to reveal, refresh button ("Another?"), done button
    # roastList dict

def make_motMsgs_layout():
    rand_motMsg = random.choice(motMsgs)
    return[[
        sg.Column(
            [
                [sg.Text(" ", size=(1,4))],
                [sg.Text(
                    f"{rand_motMsg}",
                    key='mot_msg',
                    justification='center',
                    font=('Courier', 18),
                    size=(35,4),
                    auto_size_text=False,
                    pad=(0,10)
                )],
                [sg.Text(" ", size=(1,1))],
                [sg.Text(" ", justification='center', font=('Courier', 20))],
                [sg.Button("Another?", size=(15,1), font=('Courier', 12)),
                 sg.Text("          ", justification='center', font=('Courier', 12)),
                 sg.Button("Done", size=(15,1), font=('Courier', 12))]
            ],
            justification='center',
            element_justification='center',
            vertical_alignment='center',
            expand_x=True,
            expand_y=True
        )
    ]]

# make_monModChart_layout not started >> ????????



# windows bank
welcWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_welc_layout(), size=(500,400)).finalize()
testWindow = None
acknowlWindow = None
feelsWindow = None
checkWindow = None
feels2Window = None
followUpWindow = None
deadBabWindow = None #no layout made
ventWindow = None 
storyWindow = None #no layout made
playlistWindow = None #no layout made
copingOptsWindow = None #no layout made
guidedMedWindow = None #not started
groundingWindow = None #not started
tippWindow = None #not started
monModWindow = None #not started
trainWindow = None #not started
valuesWindow = None #no layout made
motMsgsWindow = None 
roastWindow = None #no layout made
gameWindow = None #no layout made
deathsWindow = None #no layout made

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
    guidedMedWindow,
    groundingWindow,
    tippWindow,
    monModWindow,
    trainWindow,
    valuesWindow,
    motMsgsWindow,
    roastWindow,
    gameWindow,
    deathsWindow,
    blankWindow]

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
        feelsWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_feels_layout(), size=(500,400)).finalize()
        welcWindow.close()
        welcWindow = None
    
    # trans to acknowlWindow when any button is clicked from feelsLayout (testWindow)
    if feelsWindow and window == feelsWindow:
        if event in ("fine.", ">__<", "drowning...", "dO i HaVe a PerSoNaLitY dIsORdEr?", "*makin' moltovs*"):
            feelInput = event
            acknowlWindow = sg.Window (f"{event}", make_acknowl_layout(), size=(500,400)).finalize()
            feelsWindow.close()

    # trans to rand sel on next screen after "▶" is clicked from acknowlWindow
    if acknowlWindow and window == acknowlWindow and event == "▶":
        acknowlWindow.close()
        acknowlWindow = None
        
        if feelInput == "fine.":
            next_screen = random.choice(["fine1", "fine2"])
            if next_screen == "fine1":
                # placeholder for deadBabWindow
                deadBabWindow = sg.Window("fine1", make_blank_layout(), size=(500,400)).finalize()
            else:
                ventWindow = sg.Window("fine2", make_vent_layout(), size=(500,400)).finalize()
                
        elif feelInput == ">__<":
            next_screen = random.choice([">__<1", ">__<2"])
            if next_screen == ">__<1":
                # placeholder for storyWindow
                storyWindow = sg.Window(">__<1", make_blank_layout(), size=(500,400)).finalize()
            else:
                # placeholder for playlistWindow
                playlistWindow = sg.Window(">__<2", make_blank_layout(), size=(500,400)).finalize()
                
        elif feelInput == "drowning...":
            next_screen = random.choice(["drown1, drown2"])
            if next_screen == "drown1":
                # placeholder for copingWindow
                copingOptsWindow = sg.Window("drown1", make_blank_layout(), size=(500,400)).finalize()
            else:
                # placeholder for valuesWindow
                valuesWindow = sg.Window("drown2", make_blank_layout(), size=(500,400)).finalize()
                
        elif feelInput == "dO i HaVe a PerSoNaLitY dIsORdEr?":
            next_screen = random.choice(["persDis1", "persDis2"])
            if next_screen == "persDis1":
                motMsgsWindow = sg.Window("persDis1", make_motMsgs_layout(), size=(500,400)).finalize()
            else:
                # placeholder for roastWindow
                roastWindow = sg.Window("persDis2", make_blank_layout(), size=(500,400)).finalize()
    
        else:
            next_screen = random.choice(["moltovs1", "moltovs2"])
            if next_screen == "moltovs1":
                # placeholder for gameWindow
                gameWindow = sg.Window("moltovs1", make_blank_layout(), size=(500,400)).finalize()
            else:
                # placeholder for deathsWindow
                deathsWindow = sg.Window("moltovs2", make_blank_layout(), size=(500,400)).finalize()
    
    # logic for deadBabWindow
    
    # logic for ventWindow
    if ventWindow and window == ventWindow:
        vent_conf = sg.popup_yes_no(
            "Are you sure? You can't go back later.",
            title=("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•"),
            font=('Courier', 14)
        )
        if vent_conf == 'Yes': #YES, yes, or Yes?
            ventWindow.close()
            ventWindow = None
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
        elif vent_conf == 'No':
            pass
        
    # logic for storyWindow
    
    # logic for playlistWindow
    
    # logic for copingWindow
    
    # logic for valuesWindow
    
    # logic for motMsgsWindow
    if motMsgsWindow and window == motMsgsWindow:
        if event == "Another?":
            new_msg = random.choice(motMsgs)
            window['mot_msg'].update(new_msg)
        elif event == "Done":
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            motMsgsWindow.close()
            motMsgsWindow = None 
    
    # logic for roastWindow
    
    # logic for gameWindow
    
    # logic for deathsWindow
    

    # placeholder windows and "done" buttons for all activities during testing main screens
    if window and event == "done":
        if deadBabWindow:
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            deadBabWindow.close()
        elif storyWindow:
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            storyWindow.close()
        elif playlistWindow:
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            playlistWindow.close()
        elif copingOptsWindow:
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            copingOptsWindow.close() 
        elif valuesWindow:
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            valuesWindow.close() 
            
        elif roastWindow:
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            roastWindow.close() 
        elif gameWindow:
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            gameWindow.close() 
        else:
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            deathsWindow.close()
    
    # trans from followUpWindow to checkWindow
    if followUpWindow and window == followUpWindow and event == "continue":
        checkWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_check_layout(), size=(500,400)).finalize()
        followUpWindow.close()
        followUpWindow = None
    
    # trans from checkWindow > popups > exit OR follow2Window
    if checkWindow and window == checkWindow:
        if event == "yeh :)":
            checkInput = "yeh"
            result = sg.popup_ok(
                "Even a tiny bit better is a win :)  Have a great rest of your day!", 
                title="Yayyyyyyyy!", 
                font=('Courier', 14), 
            )
            if result != 'OK':
                pass
            else: 
                break
                
        elif event == "no.":
            checkInput = "naw"
            result = sg.popup_ok(
                "Rada. Let's try something else...",
                title="womp womp",
                font=('Courier', 14),
            )
            if result == 'OK':
                checkWindow.close()
                feels2Window = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_feels2_layout(), size=(500,400)).finalize()
            else:
                pass
    
    if feels2Window and window == feels2Window:
        if event == "Ready!":
            copSel = values['copingOpts_dropdown']
            
            if copSel == "Surprise Me":
                randAct = random.choice(['deadBabies',
                                         'vent',
                                         'story',
                                         'playlist',
                                         'strategies',
                                         'value',
                                         'motivation',
                                         'roast',
                                         'game',
                                         'deaths'
                                         ])
                copSel = {
                    'deadBabies': "Dead Baby Jokes",
                    'vent': "Vent (scream in the void)",
                    'story': "Storytime",
                    'playlist': "Random Rage Playlist",
                    'strategies': "Coping Strategy Reminders",
                    'value': "Reminders of Your Value",
                    'motivation': "Motivational Messaging",
                    'roast': "Roast Me",
                    'game': "Mini Game",
                    'deaths': "Imagine the Brutal Deaths of my Enemies"
                }[randAct]
                
            if copSel == "Dead Baby Jokes":
                feels2Window.close()
                feels2Window = None
                blankWindow = sg.Window("dead babies", make_blank_layout(), size=(500,400)).finalize()
                
            elif copSel == "Vent (scream in the void)":
                feels2Window.close()
                feels2Window = None
                ventWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_vent_layout(), size=(500,400)).finalize()
                
            elif copSel == "Storytime":
                feels2Window.close()
                feels2Window = None
                blankWindow = sg.Window("story", make_blank_layout(), size=(500,400)).finalize()
                
            elif copSel == "Random Rage Playlist":
                feels2Window.close()
                feels2Window = None
                blankWindow = sg.Window("playlist", make_blank_layout(), size=(500,400)).finalize()
                
            elif copSel == "Coping Strategy Reminders":
                feels2Window.close()
                feels2Window = None
                blankWindow = sg.Window("strategies", make_blank_layout(), size=(500,400)).finalize()
                
            elif copSel == "Reminders of Your Value":
                feels2Window.close()
                feels2Window = None
                blankWindow = sg.Window("values", make_blank_layout(), size=(500,400)).finalize()
                
            elif copSel == "Motivational Messaging":
                feels2Window.close()
                feels2Window = None
                motMsgsWindow = sg.Window("motivation", make_motMsgs_layout(), size=(500,400)).finalize()
            
            elif copSel == "Roast Me":
                feels2Window.close()
                feels2Window = None
                blankWindow = sg.Window("roast", make_blank_layout(), size=(500,400)).finalize()
                
            elif copSel == "Mini Game":
                feels2Window.close()
                feels2Window = None
                blankWindow = sg.Window("game", make_blank_layout(), size=(500,400)).finalize()
                
            elif copSel == "Imagine the Brutal Deaths of my Enemies":
                feels2Window.close()
                feels2Window = None
                blankWindow = sg.Window("deaths", make_blank_layout(), size=(500,400)).finalize()
