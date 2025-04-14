import PySimpleGUI as sg
import time
import random
import webbrowser

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

def choose_joke():
    joke = random.choice(list(deadBabJokes.values()))
    return joke["prompt"], joke["punch"]

def make_deadBab_layout(prompt, punch):
    return[[
        sg.Column(
            [
                [sg.Text(" ", size=(1,3))],
                [sg.Text(
                    prompt, 
                    key='joke_prompt', 
                    font=('Courier', 14), 
                    size=(50,2), 
                    justification='center')],
                [sg.Text(
                    '', 
                    key='joke_punch',
                    font=('Courier', 14),
                    size=(50,2),
                    justification='center')],
                [sg.Text(" ", size=(1,1))],
                [sg.Button("tell me", size=(20,1), font=('Courier', 12))],
                [sg.Text(" ", size=(1,1))],
                [sg.Button("Another?", size=(15,1), font=('Courier', 12)),
                 sg.Text("          ", size=(1,1)),
                 sg.Button("Done", size=(15,1), font=('Courier', 12))]
            ],
            justification='center',
            element_justification='center',
            vertical_alignment='center',
            expand_x=True,
            expand_y=True
        )
    ]]
    
def choose_story():
    story = random.choice(list(storiesList.values()))
    return [story["title"]] + [story[f"line{i}"] for i in range(1,11)]

def make_story_layout(title, *lines):
    layout = [
        [sg.Text(title, key='story_title', font=('Courier', 20), size=(70, 2), justification='center')]
    ]

    for i in range(1, 11):
        layout.append([sg.Text('', key=str(i), font=('Courier', 12), size=(1500, 1), justification='left')])

    layout += [
        [sg.Text(" ", size=(1, 2))],
        [sg.Button("Next", key="Next", size=(15, 1), font=('Courier', 12)),
         sg.Text(" " * 10),
         sg.Button("Done", key="Done", visible=False, size=(15, 1), font=('Courier', 12))]
    ]
    
    return[[
        sg.Column(layout,justification='center', element_justification='center', expand_x=True, expand_y=True)
    ]]
    
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
    # link to breathing gif: https://media0.giphy.com/media/dDXZ3qU5nRBIe82Uit/200w.gif?cid=6c09b9526vuwa6mbrcee1tuj1gbqqw28il5qcp1b3dpb3oyb&ep=v1_gifs_search&rid=200w.gif&ct=g
    # link to waterfall gif: https://i.makeagif.com/media/5-02-2018/8Ws2dD.gif
    # link to fish gif: https://i.makeagif.com/media/8-22-2019/RGJJYc.gif
    # link to calming swirl gif: https://images.squarespace-cdn.com/content/v1/581d54ccf5e231b25f89ed33/1568756642035-VX78WULS57OFDTDQB40J/Calming+Meditation+GIF+via+Worthy+Pause
    # link to cat gif: https://pa1.aminoapps.com/6768/4f220411571310edfff962dffff29a45d4e62b3d_hq.gif
    # link to orca gif: https://i.gifer.com/origin/64/64066a089d3076191d4e4366057dd0d4_w200.gif
    # link to sunshower gif: https://i.pinimg.com/originals/bb/c7/2e/bbc72e8f200db31027894f80eb00e2ae.gif
    # link to shore gif: https://i.pinimg.com/originals/d0/e2/a8/d0e2a8ae4195b8105ceb7477267367e1.gif 
    # link to globes gif: https://anxietyunited.com/wp-content/uploads/2018/01/breathing.gif
    # link to rainy day gif: https://i.pinimg.com/originals/b6/82/9c/b6829cb3569a724c620e8a100162c49b.gif
    # environment scan dialogue: Take a moment to look around. Are you in danger? What do you notice? Focus on the present moment and what your senses tell you.
    # body scan dialogue: Begin by focusing on your feet. Notice any sensations—warmth, tension, or relaxation. Slowly move your attention upward to your calves, knees, and thighs, observing each area without judgment until you reach the top of your head.

# make_grounding_layout not started: mid + are you sure? popup

# make_tipp_layout not started: mid, images + are you sure? popup

# make_monMod_layout not started: mid + are you sure? popup

# make_train_layout not started: mid + are you sure? popup

# make_game_layout not started: hard...what the mother-forker
def launch_minesweeper():
    width = 10
    height = 8
    total_bombs = 10
    
    font = 'Courier 14 bold'
    size = (30, 30)
    color = [('grey', 'grey'), ('#e0e0ff', '#3a194c'), ('black', 'green'), ('black', 'green'), ('black', '#3a194c')]
    blank = ''
    im = ['', blank, '', '', '']
    bomb_layout = [[0 for _ in range(height)] for _ in range(width)]

    def count_bombs(x, y):
        if bomb_layout[x][y] == 10:
            return 10
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and bomb_layout[nx][ny] == 10:
                    count += 1
        return count

    def deal():
        bombs = random.sample(range(width * height), total_bombs)
        for x in range(width):
            for y in range(height):
                bomb_layout[x][y] = 10 if x * height + y in bombs else 0
        for x in range(width):
            for y in range(height):
                bomb_layout[x][y] = count_bombs(x, y)

    def button(x, y):
        return sg.Button(' ', size=(3, 1), key=(x, y), font=font, button_color=color[1], pad=(1, 1))

    deal()
    state = [[1 for _ in range(height)] for _ in range(width)]

    layout = [[
        sg.Button("Quit", key="-QUIT-", font=font)
    ]] + [[
        button(x, y) for x in range(width)
    ] for y in range(height)]

    win = sg.Window("Minesweeper", layout, finalize=True, modal=True)

    while True:
        revealed = sum(state[x][y] == 0 for x in range(width) for y in range(height))
        event, _ = win.read()
        if event == sg.WINDOW_CLOSED or event == "-QUIT-":
            break
        if isinstance(event, tuple):
            x, y = event
            if state[x][y] == 1:
                light_purple = '#5c3a6d'
                val = bomb_layout[x][y]
                state[x][y] = 0
                if val == 10:
                    win[event].update(text='💣', button_color=('white', light_purple))
                    again = sg.popup_yes_no("💀 Boom! You hit a bomb.\n\nWant to try again?", title="Game Over", font=('Courier', 14))
                    if again == 'Yes':
                        deal()
                        for x in range(width):
                            for y in range(height):
                                state[x][y]
                                win[(x, y)].update(text='', disabled=False, button_color=('white', '#2e183d'))
                    else:
                        break
                elif val == 0:
                    win[event].update(text=' ', button_color=('white', light_purple))
                else:
                    win[event].update(text=str(val), button_color=('white', light_purple))
                win[event].update(disabled=True)
        if revealed == width * height - total_bombs:
            sg.popup("✨ You won! ✨", title="Victory!", font=('Courier', 14))
            again = sg.popup_yes_no("💀 Boom! You hit a bomb.\n\nWanna try again?", title="Game Over", font=('Courier', 14))
            if again == 'Yes':
                deal()
                for x in range(width):
                    for y in range(height):
                        state[x][y]
                        win[(x, y)].update(text='', disabled=False, button_color=('white', '#2e183d'))
            else:
                break

    win.close()


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

def generate_playlist():
    return "\n".join(random.sample(songsList,5))

def gen_playlist_title():
    playlist_title = random.choice(playlistNames)
    return playlist_title

def make_playlist_layout():
    playlist_title = random.choice(playlistNames)
    return[[
        sg.Column(
            [
                [sg.Text(" ", size=(1,1))],
                [sg.Text(
                    gen_playlist_title(),
                    key='playlist_title',
                    justification='center',
                    font=('Courier', 18, 'bold'),
                    size=(50, 1),
                    pad=(0, 10)
                )],
                [sg.Text(
                    generate_playlist(),
                    key='songs',
                    justification='left',
                    font=('Courier', 14),
                    size=(50,10),
                    auto_size_text=False,
                    pad=(0,10)
                )],
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

def make_values_layout():
    rand_val = random.choice(valuesList)
    return[[
        sg.Column(
            [
                [sg.Text(" ", size=(1,4))],
                [sg.Text(
                    f"{rand_val}",
                    key='val_msg',
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

def make_roast_layout():
    rand_roast = random.choice(roastList)
    return[[
        sg.Column(
            [
                [sg.Text(" ", size=(1,4))],
                [sg.Text(
                    f"{rand_roast}",
                    key='rand_roast',
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
deadBabWindow = None 
ventWindow = None 
storyWindow = None 
playlistWindow = None 
copingOptsWindow = None #inprog
guidedMedWindow = None #not started
groundingWindow = None #not started
tippWindow = None #not started
monModWindow = None #not started
trainWindow = None #not started
valuesWindow = None 
motMsgsWindow = None 
roastWindow = None 
deathsWindow = None #not started

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
    deathsWindow,
    blankWindow]

# give the GUI a breather
time.sleep(0.1)

prompt, punch = choose_joke()
title, *lines = choose_story()
story_counter = 1

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
            acknowlWindow = sg.Window ("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_acknowl_layout(), size=(500,400)).finalize()
            feelsWindow.close()

    # trans to rand sel on next screen after "▶" is clicked from acknowlWindow
    if acknowlWindow and window == acknowlWindow and event == "▶":
        acknowlWindow.close()
        acknowlWindow = None
        
        if feelInput == "fine.":
            next_screen = random.choice(["fine1", "fine2"])
            if next_screen == "fine1":
                deadBabWindow = sg.Window("•☽༻¨:·.────Dead Babies────.·:¨༺☾•", make_deadBab_layout(prompt, punch), size=(500,400)).finalize()
            else:
                ventWindow = sg.Window("•☽༻¨:·.────Vent It Out────.·:¨༺☾•", make_vent_layout(), size=(500,400)).finalize()
                
        elif feelInput == ">__<":
            next_screen = random.choice([">__<1", ">__<2"])
            if next_screen == ">__<1":
                storyWindow = sg.Window("•☽༻¨:·.────Story Time────.·:¨༺☾•", make_story_layout(title, *lines), size=(900,400)).finalize()
            else:
                playlistWindow = sg.Window("•☽༻¨:·.────Playlist Generator────.·:¨༺☾•", make_playlist_layout(), size=(500,400)).finalize()
                
        elif feelInput == "drowning...":
            next_screen = random.choice(["drown1, drown2"])
            if next_screen == "drown1":
                # placeholder for copingWindow
                copingOptsWindow = sg.Window("•☽༻¨:·.────Coping────.·:¨༺☾•", make_blank_layout(), size=(500,400)).finalize()
            else:
                valuesWindow = sg.Window("•☽༻¨:·.────Value Reminders────.·:¨༺☾•", make_values_layout(), size=(500,400)).finalize()
                
        elif feelInput == "dO i HaVe a PerSoNaLitY dIsORdEr?":
            next_screen = random.choice(["persDis1", "persDis2"])
            if next_screen == "persDis1":
                motMsgsWindow = sg.Window("•☽༻¨:·.────Motivation────.·:¨༺☾•", make_motMsgs_layout(), size=(500,400)).finalize()
            else:
                roastWindow = sg.Window("•☽༻¨:·.────Roast────.·:¨༺☾•", make_roast_layout(), size=(500,400)).finalize()
    
        else:
            next_screen = random.choice(["moltovs1", "moltovs2"])
            if next_screen == "moltovs1":
                launch_minesweeper()
                followUpWindow = sg.Window("•☽༻¨:·.────Mini Game────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            else:
                # placeholder for deathsWindow
                deathsWindow = sg.Window("•☽༻¨:·.────Kill────.·:¨༺☾•", make_blank_layout(), size=(500,400)).finalize()
    
    # logic for deadBabWindow
    if deadBabWindow and window == deadBabWindow:
        if event == "tell me":
            deadBabWindow['joke_punch'].update(punch)
        if event == "Another?":
            prompt, punch = choose_joke()
            deadBabWindow['joke_prompt'].update(prompt)
            deadBabWindow['joke_punch'].update('')
        if event == "Done":
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            deadBabWindow.close()
            deadBabWindow = None 
    
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
    if storyWindow and window == storyWindow:
        if event == "Next":
            if story_counter <= len(lines):
                storyWindow[str(story_counter)].update(lines[story_counter - 1])
                story_counter += 1
                if story_counter > len(lines):
                    storyWindow["Done"].update(visible=True)
                    storyWindow["Next"].update(visible=False)
   
        elif event == "Done":
            story_counter = 1
            title, *lines = choose_story()
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            storyWindow.close()
            storylistWindow = None 
    
    # logic for playlistWindow
    if playlistWindow and window == playlistWindow:
        if event == "Another?":
            window['playlist_title'].update(gen_playlist_title())
            window['songs'].update(generate_playlist())
        elif event == "Done":
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            playlistWindow.close()
            playlistWindow = None 
    
    # logic for copingWindow
    
    # logic for valuesWindow
    if valuesWindow and window == valuesWindow:
        if event == "Another?":
            new_val = random.choice(valuesList)
            window['val_msg'].update(new_val)
        elif event == "Done":
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            valuesWindow.close()
            valuesWindow = None 
    
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
    if roastWindow and window == roastWindow:
        if event == "Another?":
            new_roast = random.choice(roastList)
            window['rand_roast'].update(new_roast)
        elif event == "Done":
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            roastWindow.close()
            roastWindow = None 
    
    # logic for gameWindow << needed???
    
    # logic for deathsWindow
    

    # placeholder windows and "done" buttons for all activities during testing main screens
    if window and event == "done":
        if copingOptsWindow:
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            copingOptsWindow.close()
        else:
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
            deathsWindow.close()
    
    # trans from followUpWindow to checkWindow
    if followUpWindow and window == followUpWindow and event == "continue":
        checkWindow = sg.Window("•☽༻¨:·.────Checking In────.·:¨༺☾•", make_check_layout(), size=(500,400)).finalize()
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
                deadBabWindow = sg.Window("dead babies", make_deadBab_layout(prompt, punch), size=(500,400)).finalize()
                
            elif copSel == "Vent (scream in the void)":
                feels2Window.close()
                feels2Window = None
                ventWindow = sg.Window("•☽༻¨:·.────Vent It Out────.·:¨༺☾•", make_vent_layout(), size=(500,400)).finalize()
                
            elif copSel == "Storytime":
                feels2Window.close()
                feels2Window = None
                storyWindow = sg.Window("•☽༻¨:·.────Story Time────.·:¨༺☾•", make_story_layout(title, *lines), size=(900,400)).finalize()
                
            elif copSel == "Random Rage Playlist":
                feels2Window.close()
                feels2Window = None
                playlistWindow = sg.Window("•☽༻¨:·.────Playlist Generator────.·:¨༺☾•", make_playlist_layout(), size=(500,400)).finalize()
                
            elif copSel == "Coping Strategy Reminders":
                feels2Window.close()
                feels2Window = None
                blankWindow = sg.Window("•☽༻¨:·.────Coping────.·:¨༺☾•", make_blank_layout(), size=(500,400)).finalize()
                
            elif copSel == "Reminders of Your Value":
                feels2Window.close()
                feels2Window = None
                valuesWindow = sg.Window("•☽༻¨:·.────Value Reminders────.·:¨༺☾•", make_values_layout(), size=(500,400)).finalize()
                
            elif copSel == "Motivational Messaging":
                feels2Window.close()
                feels2Window = None
                motMsgsWindow = sg.Window("•☽༻¨:·.────Motivation────.·:¨༺☾•", make_motMsgs_layout(), size=(500,400)).finalize()
            
            elif copSel == "Roast Me":
                feels2Window.close()
                feels2Window = None
                roastWindow = sg.Window("•☽༻¨:·.────Roast────.·:¨༺☾•", make_roast_layout(), size=(500,400)).finalize()
                
            elif copSel == "Mini Game":
                feels2Window.close()
                feels2Window = None
                launch_minesweeper()
                followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(), size=(500,400)).finalize()
                
            elif copSel == "Imagine the Brutal Deaths of my Enemies":
                feels2Window.close()
                feels2Window = None
                blankWindow = sg.Window("•☽༻¨:·.────Kill────.·:¨༺☾•", make_blank_layout(), size=(500,400)).finalize()
