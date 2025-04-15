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

def make_welc_layout(greeting):
    return[[
        sg.Column(
            [
                [sg.Text("────⋆˖⁺‧₊☽◯☾₊‧⁺˖⋆────", justification='center', font=('Courier', 20))],
                [sg.Text('', size=(1,1))],
                [sg.Text(greeting, justification='center', font=('Courier', 18), size=(40, 3), auto_size_text=False)],
                [sg.Text(" ", font=('Courier', 20))],
                [sg.Button("▶", size=(10,1), font=('Courier', 18))]
            ],
        justification='center',
        element_justification='center',
        expand_x=True
        )
    ]]

def make_acknowl_layout(acknowl):
    return[[
        sg.Column(
        [
            [sg.Text(" ", size=(1,3))],
            # acknowlMsgs dict
            [sg.Text(acknowl, justification='center', font=('Courier', 18), size=(40, 3), auto_size_text=False)],
            [sg.Text(" ", size=(1,1))],
            [sg.Button("▶", size=(10,1), font=('Courier', 12))]
        ],
        justification='center',
        element_justification='center',
        expand_x=True
        )
    ]]

def make_check_layout(checkin_msg):
    return[[
        sg.Column(
        [
            [sg.Text('', size=(1,1))],
            [sg.Text(checkin_msg, justification='center', font=('Courier', 18), size=(40, 4), auto_size_text=False)],
            [sg.Text(" ", font=('Courier', 20))],
            [sg.Button("yeh :)", size=(10,1), font=('Courier', 12)),
             sg.Text("          ", justification='center', font=('Courier', 12)),
             sg.Button("not yet", size=(10,1), font=('Courier', 12))]
        ],
        justification='center',
        element_justification='center',
        expand_x=True
        )
    ]]

def make_followup_layout(followup_msg):
    return[[
        sg.Column(
            [
                # followUpMsgs dict
                [sg.Text('', size=(1,1))],
                [sg.Text(followup_msg, justification='center', font=('Courier', 20), size=(40, 2), auto_size_text=False)],
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
    
def make_copingOpts_layout():
    return[[
        sg.Column(
        [
            [sg.Text("Nothing fancy here. Just some reminders <3", justification='center', font=('Courier', 16))],
            [sg.Text("Pick an exercise from the dropdown!", justification='center', font=('Courier', 14))],
            [sg.Text(' ', size=(1,1))],
            [sg.Combo(
                values=['Choose for me',
                        'Guided Meditation',
                        'Grounding Exercise',
                        'Monitor & Modify Exercise',
                        'Trainspotting Exercise'
                        ],
                default_value='Choose for me',
                key='copingStrats_dropdown',
                font=('Courier', 12),
                size=(30,1),
                enable_events=True,
                readonly=True
            )],
            [sg.Text(' ', size=(1,2))],
            [sg.Button("Start", size=(10,1), font=('Courier', 12))]
        ],
        justification='center',
        element_justification='center',
        expand_x=True
        )
    ]]

def handle_coping_options(window, values):
    exSel = values['copingStrats_dropdown']

    if exSel == "Choose for me":
        randEx = random.choice(['med', 'ground', 'monMod', 'train'])
        exSel = {
            'med': "Guided Meditation",
            'ground': "Grounding Exercise",
            'monMod': "Monitor & Modify Exercise",
            'train': "Trainspotting Exercise"
        }[randEx]

    if exSel == "Guided Meditation":
        return "med"
    elif exSel == "Grounding Exercise":
        return "ground"
    elif exSel == "Monitor & Modify Exercise":
        return "monMod"
    elif exSel == "Trainspotting Exercise":
        return "train"
    return None

def make_guidedMed_layout():
    return[[
        sg.Column(
            [
                # Stuff you know, sure. Reminders are nice sometimes, though...right?
                [sg.Text("Stuff you know, sure. \nReminders are nice sometimes, though...right?", justification='center', font=('Courier', 20))],
                [sg.Text('', size=(1,1))],
                # First, check your environment...
                [sg.Text("First, check your surroundings.", justification='center', font=('Courier', 16))],
                [sg.Text("*  What is today's date, what time is it, and what city/state are you in?\n*  Do you feel safe? \n*  What do your senses tell you?\n*  Who else is in the room with you?\n*  What does the floor or chair beneath you feel like?", justification='left', font=('Courier', 12))],
                [sg.Text('', size=(1,1))],
                # Next, do a body scan...
                [sg.Text("Next, do a body scan.", justification='center', font=('Courier', 16))],
                [sg.Text("*  Start by focusing on your feet. \n*  Observe how they feel without judgement.\n*  Try breathing and releasing any tension you feel.\n*  Move up to your legs-- observe and release tension.\n*  Slowly move your way up to the top of your head one step at a time.", justification='left', font=('Courier', 12))],
                [sg.Text('', size=(1,1))],
                # Last, look at a pretty gif and breathe for a minute...
                [sg.Text("Cool, now look at a pretty gif and focus on breathing.", justification='center', font=('Courier', 16))],
                [sg.Button("⭕", key='breathGIF'),
                 sg.Text(" ", font=('Courier', 12)),
                 sg.Button("🌊", key='waterfallGIF'),
                 sg.Text(" ", font=('Courier', 12)),
                 sg.Button("🐟", key='fishGIF'),
                 sg.Text(" ", font=('Courier', 12)),
                 sg.Button("🌀", key='swirlGIF'),
                 sg.Text(" ", font=('Courier', 12)),
                 sg.Button("🐈", key='catGIF'),
                 sg.Text(" ", font=('Courier', 12)),
                 sg.Button("🐋", key='orcaGIF'),
                 sg.Text(" ", font=('Courier', 12)),
                 sg.Button("🌧️", key='sunRainGIF'),
                 sg.Text(" ", font=('Courier', 12)),
                 sg.Button("🏖️", key='shoreGIF'),
                 sg.Text(" ", font=('Courier', 12)),
                 sg.Button("🌎", key='globesGIF'),
                 sg.Text(" ", font=('Courier', 12)),
                 sg.Button("☂️", key='rainGIF')],
                [sg.Text('', size=(1,2))],
                [sg.Button("Done", size=(10,1), font=('Courier', 12))]
            ],
            scrollable=True,
            vertical_scroll_only=True,
            key='-SCROLLABLE-',
            justification='center',
            element_justification='center',
            expand_x=True,
            expand_y=True
        )
    ]]
  
def make_grounding_layout():
    # Pairs of prompts and their corresponding Multiline keys
    grounding_prompts = [
        ("5 things you can see:", 'seeBox'),
        ("4 things you can feel:", 'feelBox'),
        ("3 things you can hear:", 'hearBox'),
        ("2 things you can smell:", 'smellBox'),
        ("1 thing you can taste:", 'tasteBox'),
        ("1 thing that is true:", 'truthBox'),
        ("2 signs of life:", 'survivalBox'),
        ("3 things you can do next:", 'tasksBox'),
        ("4 of your strengths:", 'strengthsBox'),
        ("5 comforting things:", 'comfortBox')
    ]

    # Left column: just the prompt labels
    left_col = [[sg.Text(prompt, font=('Courier', 12), justification='left', pad=(0, 12.25))] for prompt, _ in grounding_prompts]

    # Right column: the input boxes
    right_col = [[
        sg.Multiline(
            key=key,
            size=(70, 2),
            font=('Courier', 12),
            border_width=2,
            expand_x=True,
            expand_y=False,
            pad=(0, 5)
        )
    ] for _, key in grounding_prompts]

    return [[
        sg.Column(
            [
                [sg.Text("Writing it out helps sometimes. Just remember none of this is saved!",
                         justification='center',
                         font=('Courier', 14),
                         pad=(0, 10))],

                [sg.Column(left_col, vertical_alignment='top', element_justification='left', pad=(0, 0)),
                 sg.Column(right_col, vertical_alignment='top', element_justification='left', pad=(10, 0))],

                [sg.Text('', size=(1, 1))],
                [sg.Button("Done", size=(10, 1), font=('Courier', 12), pad=(0, 20))]
            ],
            scrollable=True,
            vertical_scroll_only=True,
            size=(775, 400),
            key='-SCROLLABLE-',
            justification='center',
            expand_x=True,
            expand_y=True
        )
    ]]

def make_monMod_layout():
    # Pairs of prompts and their corresponding Multiline keys
    monMod_prompts = [
        ("Pulse/Heartrate:", 'pulseBox'),
        ("Breaths per minute:", 'breathsBox'),
        ("Total hours of sleep in the past 24hrs:", 'sleepBox'),
    ]

    # Left column: the prompt labels
    left_col = [[sg.Text(prompt, font=('Courier', 12), justification='left', pad=(0, 11))] for prompt, _ in monMod_prompts]

    # Right column: the input boxes
    right_col = [[
        sg.Multiline(
            key=key,
            size=(20, 1),
            font=('Courier', 12),
            border_width=1,
            expand_x=True,
            expand_y=False,
            pad=(0, 4)
        )
    ] for _, key in monMod_prompts]  # ← fixed from grounding_prompts

    # Full layout
    return [[
        sg.Column(
            [
                [sg.Text("Writing it out helps sometimes. Just remember none of this is saved!",
                         justification='center',
                         font=('Courier', 14),
                         pad=(0, 10))],

                [sg.Column(left_col, vertical_alignment='top', element_justification='right', pad=(0, 0)),
                 sg.Column(right_col, vertical_alignment='top', element_justification='left', pad=(10, 0))],
                
                [sg.Text('', size=(1, 1))],

                [sg.Text("About how many cups of caffiene have you had in the past 24 hours?", justification='center', font=('Courier', 12))],
                [sg.Slider(
                    range=(0, 10),
                    default_value=0,
                    orientation='h',
                    key='caff_slider',
                    size=(50, 20),
                    font=('Courier', 12),
                    enable_events=True,
                    disable_number_display=False
                )],

                [sg.Text('', size=(1, 1))],

                [sg.Text("Rate your pain. 1 = no pain, 10 = worst pain.", justification='center', font=('Courier', 12))],
                [sg.Slider(
                    range=(1, 10),
                    default_value=1,
                    orientation='h',
                    key='pain_slider',
                    size=(50, 20),
                    font=('Courier', 12),
                    enable_events=True,
                    disable_number_display=False
                )],
                
                [sg.Text('', size=(1, 1))],

                [sg.Text("Rate your level of dissociation. 1 = none, 10 = worst.", justification='center', font=('Courier', 12))],
                [sg.Slider(
                    range=(1, 10),
                    default_value=1,
                    orientation='h',
                    key='diss_slider',
                    size=(50, 20),
                    font=('Courier', 12),
                    enable_events=True,
                    disable_number_display=False
                )],
                
                [sg.Text('', size=(1, 1))],
                
                [sg.Text("Did you eat today?", justification='center', font=('Courier', 12))],
                [
                    sg.Checkbox("Yes", key="ate_yes", enable_events=True, font=('Courier', 8)),
                    sg.Checkbox("No", key="ate_no", enable_events=True, font=('Courier', 8))
                ],
                
                [sg.Text('', size=(1, 1))],
                
                [sg.Text("Did you take all your medications today?", justification='center', font=('Courier', 12))],
                [
                    sg.Checkbox("Yes", key="med_yes", enable_events=True, font=('Courier', 8)),
                    sg.Checkbox("No", key="med_no", enable_events=True, font=('Courier', 8))
                ],

                [sg.Text('', size=(1, 2))],
                [sg.Button("Done", size=(10, 1), font=('Courier', 12), pad=(0, 20))]
            ],
            scrollable=True,
            vertical_scroll_only=True,
            size=(775, 400),
            key='-SCROLLABLE-',
            justification='center',
            element_justification='center',
            expand_x=True,
            expand_y=True
        )
    ]]

def make_train_layout():
    # Pairs of prompts and their corresponding Multiline keys
    train_prompts = [
        ("Give the train a name.", 'trainName'),
        ("Describe its intensity.", 'trainSpeed'),
        ("Have you seen this before?", 'trainSeen'),
        ("If yes, what happened?", 'trainHist'),
        ("Where did it come from?", 'trainFrom'),
        ("Where might it go?", 'trainTo'),
        ("How might you derail it?", 'trainDerail')
    ]

    # Left column: just the prompt labels
    left_col = [[sg.Text(prompt, font=('Courier', 12), justification='left', pad=(0, 12.25))] for prompt, _ in train_prompts]

    # Right column: the input boxes
    right_col = [[
        sg.Multiline(
            key=key,
            size=(70, 2),
            font=('Courier', 12),
            border_width=2,
            expand_x=True,
            expand_y=False,
            pad=(0, 5)
        )
    ] for _, key in train_prompts]

    return [[
        sg.Column(
            [
                [sg.Text("Woosah. Just remember none of this is saved!",
                         justification='center',
                         font=('Courier', 14),
                         pad=(0, 10))],

                [sg.Column(left_col, vertical_alignment='top', element_justification='left', pad=(0, 0)),
                 sg.Column(right_col, vertical_alignment='top', element_justification='left', pad=(10, 0))],

                [sg.Text('', size=(1, 1))],
                [sg.Button("Done", size=(10, 1), font=('Courier', 12), pad=(0, 20))]
            ],
            scrollable=True,
            vertical_scroll_only=True,
            size=(775, 400),
            key='-SCROLLABLE-',
            justification='center',
            expand_x=True,
            expand_y=True
        )
    ]]

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

    def check_win():
        revealed = sum(state[x][y] == 0 for x in range(width) for y in range(height))
        if revealed == width * height - total_bombs:
            sg.popup("✨ You won! ✨", title="Victory!", font=('Courier', 14))
            again = sg.popup_yes_no("Play again?", title="Game Over", font=('Courier', 14))
            if again == 'Yes':
                deal()
                for x in range(width):
                    for y in range(height):
                        state[x][y] = 1
                        win[(x, y)].update(text='', disabled=False, button_color=('white', '#2e183d'))
            else:
                win.close()
                return True
        return False

    deal()
    state = [[1 for _ in range(height)] for _ in range(width)]

    layout = [[
        sg.Button("Quit", key="-QUIT-", font=font)
    ]] + [[
        button(x, y) for x in range(width)
    ] for y in range(height)]

    win = sg.Window("Minesweeper", layout, finalize=True, modal=True)

    while True:
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
                                state[x][y] = 1
                                win[(x, y)].update(text='', disabled=False, button_color=('white', '#2e183d'))
                        continue  # restart loop after resetting
                    else:
                        break
                else:
                    # Safe square
                    win[event].update(
                        text=' ' if val == 0 else str(val),
                        button_color=('white', light_purple),
                        disabled=True
                    )
                    if check_win():
                        break  # game ends after win check


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
                    size=(40, 5),
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
                    size=(40,5),
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
                    size=(40, 5),
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

rand_greeting = random.choice(welcGreetings)
acknowl = random.choice(acknowlMsgs)

# windows bank
welcWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_welc_layout(rand_greeting), size=(500,400)).finalize()
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
copingOptsWindow = None 
guidedMedWindow = None 
groundingWindow = None
monModWindow = None 
trainWindow = None 
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
            acknowlWindow = sg.Window ("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_acknowl_layout(acknowl), size=(500,400)).finalize()
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
                copingOptsWindow = sg.Window("•☽༻¨:·.────Coping────.·:¨༺☾•", make_copingOpts_layout(), size=(500,400)).finalize()
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
                followup_msg = random.choice(followUpMsgs)
                followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
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
            followup_msg = random.choice(followUpMsgs)
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
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
            followup_msg = random.choice(followUpMsgs)
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
    
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
            followup_msg = random.choice(followUpMsgs)
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
            storyWindow.close()
            storylistWindow = None 
    
    # logic for playlistWindow
    if playlistWindow and window == playlistWindow:
        if event == "Another?":
            window['playlist_title'].update(gen_playlist_title())
            window['songs'].update(generate_playlist())
        elif event == "Done":
            followup_msg = random.choice(followUpMsgs)
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
            playlistWindow.close()
            playlistWindow = None 
    
    # logic for copingWindow
    if copingOptsWindow and window == copingOptsWindow:
        if event == "Start":
            choice = handle_coping_options(window, values)
            copingOptsWindow.close()
            copingOptsWindow = None

            if choice == "med":
                guidedMedWindow = sg.Window("•☽༻¨:·.────Meditation────.·:¨༺☾•", make_guidedMed_layout(), size=(600,400)).finalize()
                open_windows.append(guidedMedWindow)
            elif choice == "ground":
                groundingWindow = sg.Window("•☽༻¨:·.────Grounding────.·:¨༺☾•", make_grounding_layout(), size=(800,400)).finalize()
                open_windows.append(groundingWindow)
            elif choice == "monMod":
                monModWindow = sg.Window("•☽༻¨:·.────Monitor & Modify────.·:¨༺☾•", make_monMod_layout(), size=(600,400)).finalize()
                open_windows.append(monModWindow)
            elif choice == "train":
                trainWindow = sg.Window("•☽༻¨:·.────Trainspotting────.·:¨༺☾•", make_train_layout(), size=(800,400)).finalize()
                open_windows.append(trainWindow)
    
    # logic for guidedMedWindow
    if guidedMedWindow and window == guidedMedWindow:
        if event == 'breathGIF':
            webbrowser.open('https://media0.giphy.com/media/dDXZ3qU5nRBIe82Uit/200w.gif?cid=6c09b9526vuwa6mbrcee1tuj1gbqqw28il5qcp1b3dpb3oyb&ep=v1_gifs_search&rid=200w.gif&ct=g')
        elif event == 'waterfallGIF':
            webbrowser.open('https://i.makeagif.com/media/5-02-2018/8Ws2dD.gif')
        elif event == 'fishGIF':
            webbrowser.open('https://i.makeagif.com/media/8-22-2019/RGJJYc.gif')
        elif event == 'swirlGIF':
            webbrowser.open('https://images.squarespace-cdn.com/content/v1/581d54ccf5e231b25f89ed33/1568756642035-VX78WULS57OFDTDQB40J/Calming+Meditation+GIF+via+Worthy+Pause')
        elif event == 'catGIF':
            webbrowser.open('https://pa1.aminoapps.com/6768/4f220411571310edfff962dffff29a45d4e62b3d_hq.gif')
        elif event == 'orcaGIF':
            webbrowser.open('https://i.gifer.com/origin/64/64066a089d3076191d4e4366057dd0d4_w200.gif')
        elif event == 'sunRainGIF':
            webbrowser.open('https://i.pinimg.com/originals/bb/c7/2e/bbc72e8f200db31027894f80eb00e2ae.gif')
        elif event == 'shoreGIF':
            webbrowser.open('https://i.pinimg.com/originals/d0/e2/a8/d0e2a8ae4195b8105ceb7477267367e1.gif')
        elif event == 'globesGIF':
            webbrowser.open('https://anxietyunited.com/wp-content/uploads/2018/01/breathing.gif')
        elif event == 'rainGIF':
            webbrowser.open('https://i.pinimg.com/originals/b6/82/9c/b6829cb3569a724c620e8a100162c49b.gif')
            
        elif event == "Done":
            #popups to confirm, to ask if user want to return to copingOptsWindow
            result = sg.popup_yes_no(
                "Are you sure? You can't go back later.",
                title=("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•"),
                font=('Courier', 14)
            )
            if result == 'Yes':
                next_result = sg.popup_yes_no(
                "Need to go back to the coping strategies dropdown window?",
                title=("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•"),
                font=('Courier', 14)
            )
                if next_result == 'Yes':
                    # go to copingWindow
                    guidedMedWindow.close()
                    guidedMedWindow = None
                    copingOptsWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_copingOpts_layout(), size=(500,400)).finalize()
                    
                elif next_result == 'No':
                    # go to followUpWindow
                    guidedMedWindow.close()
                    guidedMedWindow = None
                    followup_msg = random.choice(followUpMsgs)
                    followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
                    
            elif result == 'No':
                pass
    
    # logic for groundingWindow
    if groundingWindow and window == groundingWindow and event == "Done":
        result = sg.popup_yes_no(
            "Are you sure? You can't go back later.",
            title=("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•"),
            font=('Courier', 14)
        )
        
        if result == 'Yes':
            next_result = sg.popup_yes_no(
                "See, now wasn't that a fun spin on the classic 54321 exercise?\nNeed to go back to the coping strategies dropdown window?",
                title=("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•"),
                font=('Courier', 14)
            )
            if next_result == 'Yes':
                # go to copingWindow
                groundingWindow.close()
                groundingWindow = None
                copingOptsWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_copingOpts_layout(), size=(500,400)).finalize()
                
            elif next_result == 'No':
                # go to followUpWindow
                groundingWindow.close()
                groundingWindow = None
                followup_msg = random.choice(followUpMsgs)
                followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
                
        elif result == 'No':
            pass
    
    # logic for monModWindow
    if monModWindow and window == monModWindow and event == "Done":
        result = sg.popup_yes_no(
            "Are you sure? You can't go back later.",
            title=("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•"),
            font=('Courier', 14)
        )
        if result == 'Yes':
            next_result = sg.popup_yes_no(
                "Well, look at you! The good news is you're alive.\nAnd, you're still doing great 🫡\nNeed to go back to the coping strategies dropdown window?",
                title=("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•"),
                font=('Courier', 14)
            )
            if next_result == 'Yes':
                # go to copingWindow
                monModWindow.close()
                monModWindow = None
                copingOptsWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_copingOpts_layout(), size=(500,400)).finalize()
                
            elif next_result == 'No':
                # go to followUpWindow
                monModWindow.close()
                monModWindow = None
                followup_msg = random.choice(followUpMsgs)
                followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
                
        elif result == 'No':
            pass
    
    # logic for trainWindow
    if trainWindow and window == trainWindow and event == "Done":
        result = sg.popup_yes_no(
            "Are you sure? You can't go back later.",
            title=("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•"),
            font=('Courier', 14)
        )
        if result == 'Yes':
            next_result = sg.popup_yes_no(
                "Good job, you! That couldn't have been easy.\nNeed to go back to the coping strategies dropdown window?",
                title=("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•"),
                font=('Courier', 14)
            )
            if next_result == 'Yes':
                # go to copingWindow
                trainWindow.close()
                trainWindow = None
                copingOptsWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_copingOpts_layout(), size=(500,400)).finalize()
                
            elif next_result == 'No':
                # go to followUpWindow
                trainWindow.close()
                trainWindow = None
                followup_msg = random.choice(followUpMsgs)
                followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
                
        elif result == 'No':
            pass
    
    # logic for valuesWindow
    if valuesWindow and window == valuesWindow:
        if event == "Another?":
            new_val = random.choice(valuesList)
            window['val_msg'].update(new_val)
        elif event == "Done":
            followup_msg = random.choice(followUpMsgs)
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
            valuesWindow.close()
            valuesWindow = None 
    
    # logic for motMsgsWindow
    if motMsgsWindow and window == motMsgsWindow:
        if event == "Another?":
            new_msg = random.choice(motMsgs)
            window['mot_msg'].update(new_msg)
        elif event == "Done":
            followup_msg = random.choice(followUpMsgs)
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
            motMsgsWindow.close()
            motMsgsWindow = None 
    
    # logic for roastWindow
    if roastWindow and window == roastWindow:
        if event == "Another?":
            new_roast = random.choice(roastList)
            window['rand_roast'].update(new_roast)
        elif event == "Done":
            followup_msg = random.choice(followUpMsgs)
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
            roastWindow.close()
            roastWindow = None 
    
    # logic for deathsWindow

    # placeholder windows and "done" buttons for all activities during testing main screens
    if window and event == "done":
        if deathsWindow:
            followup_msg = random.choice(followUpMsgs)
            followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
            deathsWindow.close()
            deathsWindow = None

    # trans from followUpWindow to checkWindow
    if followUpWindow and window == followUpWindow and event == "continue":
        checkin_msg = random.choice(checkinMsgs)
        checkWindow = sg.Window("•☽༻¨:·.────Checking In────.·:¨༺☾•", make_check_layout(checkin_msg), size=(500,400)).finalize()
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
                
        elif event == "not yet":
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
                copingOptsWindow = sg.Window("•☽༻¨:·.────Coping────.·:¨༺☾•", make_copingOpts_layout(), size=(500,400)).finalize()
                open_windows.append(copingOptsWindow)
                
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
                followup_msg = random.choice(followUpMsgs)
                followUpWindow = sg.Window("•☽༻¨:·.────₊☽◯☾₊────.·:¨༺☾•", make_followup_layout(followup_msg), size=(500,400)).finalize()
                
            elif copSel == "Imagine the Brutal Deaths of my Enemies":
                feels2Window.close()
                feels2Window = None
                blankWindow = sg.Window("•☽༻¨:·.────Kill────.·:¨༺☾•", make_blank_layout(), size=(500,400)).finalize()
