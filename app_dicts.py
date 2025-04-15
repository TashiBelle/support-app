import PySimpleGUI as sg
import time
import random


# welcGreetings for make_welc_layout / welcWindow
welcGreetings = [
    "How ya doin'?",
    "How's it hangin'?",
    "How are you today?",
    "What is ... *gestures to your entire being* ... this?",
    "How are you feeling?",
    "Is this crisis, denial, or are you aggressively 'fine'?",
    "Hey there, are we just 'fine' or are we burning it all down?",
    "What flavor of meltdown are we cooking with today?",
    "Welcome. I assume feelings developed against your will?",
    "Don't worry, I have no memory or external connections. \nGo on, tell me how you're really feeling."
]

# acknowlMsgs for make_acknowl_Layout / acknowlWindow 
acknowlMsgs = [
    "Oof :/  \nTime for some support.",
    "Looks like you're screwed. \nKIDDING! Let's get you some support.",
    "That's rough, buddy.",
    "Everyone gets that way sometimes. Thas otay. Maybe this will help.",
    "Oh nos! Quick, try this ...",
    "That blows. This will help. \nI know because my therapist told me so.",
    "Yeesh. Time to put the 'cope' in 'OH MY GODS EVERYTHING IS ON FIRE'.",
    "I'd offer you a hug, but I'm a digital construct. \nMaybe this will help?",
    "Aw :(  Here, try this! \nOr don't. I'll just be here waiting.",
    "Lame :P  \nThis would be the part where an NPC gives you a side quest.",
    "Woof. Triage time.",
    "Rada rada rada. \nUm ... mebbe this helps?"
]

# checkinMsgs for make_check_layout / checkWindow (y/n only)
checkinMsgs = [
    "Feeling any better?",
    "Did that help even just a little tiny bit?",
    "Checking-in! Feel better?",
    "<status report requested>; \nenter 'y' for net positive, otherwise enter 'n'",
    "Sooo, are we alive and slightly less fucked?",
    "Ready to stop being a sad soggy burrito now?",
    "Did it help, or are we still riding the emotional rollercoaster with no seatbelt?",
    "Enter 'y' if you good, enter 'n' for more support.",
    "Find a paddle to help you out of that shit creek? \n'Y' to end, 'N' to continue.",
    "'Y' if you've returned to the land of the semi-ok, otherwise click 'N'."
]

# successMsgs for Yeh :) popup in checkWindow

# deadBabJokes for make_deadBab_layout in deadBabWindow
deadBabJokes={
    1: {
        "prompt": "What's difference between a dead baby and a fish?",
        "punch": "You haven't flushed a fish down the toilet ... yet."
    },
    2: {
        "prompt": "What's better than a dead baby stapled to a tree?",
        "punch": "A dead baby stapled to 10 trees."
    },
    3: {
        "prompt": "Why did the dead baby cross the road?",
        "punch": "Because it was duct-taped to a chicken."
    },
    4: {
        "prompt": "How do you make a dead baby float?",
        "punch": "Two scoops of ice cream, one cup of root beer; blend with dead baby; serve cold."
    },
    5: {
        "prompt": "What's the difference between a dead baby and a trampoline?",
        "punch": "You take your boots off before you jump on a trampoline."
    },
    6: {
        "prompt": "What's the difference between a dead baby and a peanut butter cup?",
        "punch": "One's in your lunchbox, the other's in your freezer. You know which is which."
    },
    7: {
        "prompt": "Why can't you microwave a dead baby?",
        "punch": "The metal coat hanger would spark too much."
    },
    8: {
        "prompt": "What's the difference between a dead baby and a watermelon?",
        "punch": "You can't eat a watermelon with a pitchfork (but you can try)."
    },
    9: {
        "prompt": "How do you stop a baby from crawling in circles?",
        "punch": "Nail it's other hand to the floor."
    },
    10: {
        "prompt": "How many dead babies does it take to paint a house?",
        "punch": "Depends on how hard you throw them."
    }
}

# storiesList for make_story_layout in storyWindow
storiesList = {
    1: {
        "title": "Squirrel Swirl",
        "line1": "There once was a burnout therapist.",
        "line2": "She canceled all sessions, closed her practice, and decided to live the life she always dreamed.",
        "line3": "After weeks of hard work, she finally did it. ",
        "line4": "She opened her own bakery: Squirrel Swirl.",
        "line5": "Only squirrels were allowed to enter the shop.",
        "line6": "It quickly became a squirrel sanctuary.",
        "line7": "Squirrels from all around found shelter from the vicious dogs and house cats.",
        "line8": "But, as we all know, squirrels aren't real.",
        "line9": "They're governement spies, of course.",
        "line10": "The bakery became a social security office."
    },
    2: {
        "title": "Boot Metamorphasis",
        "line1": "'Wh-where am I?'",
        "line2": "The boot, now endowed with sentience, surveyed the room.",
        "line3": "His partner (the other boot) sat perfectly in line next to him ...",
        "line4": "... a folded uniform was placed just so atop the freshly made bed ...",
        "line5": "... and a framed photo of Nicholas Cage teetered on the edge of the nightstand.",
        "line6": "The boot then realized that he could also hear, feel, taste, reason, and emote.",
        "line7": "But worst of all ...",
        "line8": "... he could smell.",
        "line9": "The strong odor wafting from inside him was too much to bear. ",
        "line10": "He promptly shuffled his way down the hall and filed for worker's comp."
    },
    3: {
        "title": "Foreclosure",
        "line1": "I once met a Gen-X'er (a la 1984…..you know the ones) who just couldn't keep up with the mortgage.",
        "line2": "She didn't have fancy degrees or combat training or the kind of resilience you have.",
        "line3": "She did have one special skill, though ...",
        "line4": "The power of the Latch-Key Kid ™.",
        "line5": "Abilities include: runnin', lock-pickin', and buildin' sand castles.",
        "line6": "Weaknesses include: paying bills, emotional regulation, and maintaining a grip on reality.",
        "line7": "Eventually, she declared banruptcy and lost her house ...",
        "line8": "... so she built a huge sand castle with a pillow fort in every room.",
        "line9": "But ... you know how these things go ...",
        "line10": "She discovered that the sand castle was built atop a hellmouth, and it was soon foreclosed."
    },
    4: {
        "title": "Calcifer Documentation",
        "line1": "Client Name: Calcifer",
        "line2": "Presenting Problem: Client reports being 'trapped in a bargain with a mediocre wizard'.",
        "line3": "Appearance: Aggressively sentient fireball-- conveys emotions via flaring /simmering ...",
        "line4": "... pointedly Left soot on the couch.",
        "line5": "Affect: Labile. Cycles between smug, panicked, and flirty.",
        "line6": "Preliminary Dx: Rule out Flame-Related Delusional Disorder (F-RDD), Complex Fire Trauma, and Magical Codependency.",
        "line7": "Treatment Plan: Narrative therapy to untangle contract-based trauma. Reduce bacon intake as coping strategy.",
        "line8": "Additional Notes: Refused grounding exercises, claiming 'I am the ground'.",
        "line9": "Burned 3 intake forms and attempted to barter for emotional safety using soot sprites.",
        "line10": "Session ended abruptly when client caught sight of the fire extingusher by the desk."
    }
}

# playlistNames for make_playlist_layout in playlistWindow
playlistNames = [
    "Bitchcraft: Audio Assault ",
    "FUCK 'EM UP",
    "god puncher",
    "Moltovs & Mascara",
    "Cry-Scream-Slay",
    "Why is there glitter in my puke?",
    "Fucked, Insecure, Neurotic, Emo",
    "Fighin' Bugs",
    "Pure Gryffiindor Rage",
    "SPITE",
    "Slaughter counts as self-care, right?",
    "don't talk to me or my trauma ever again",
    "keep my name out your moThEr FUckIng mOUtH",
    "Barbie Don' Snapped",
    "they all bout to die"
]

# songList for make_playlist_layout in playlistWindow
songsList = [
    "'Jekyll and Hyde' - Five Finger Death Punch",
    "'Under and Over' - Five Finger Death Punch",
    "'Duality' - Slipknot",
    "'Down with the Sickness' - Disturbed",
    "'Freak on a Leash' - Korn",
    "'Chop Suey!' - System of a Down",
    "'Killing in the Name' - Rage Against the Machine",
    "'Throne' - Bring Me the Horizon",
    "'STUPID' - Ashnikko ft. Yung Baby Tate",
    "'Deal With It' - Ashnikko ft. Kelis",
    "'Vroom Vroom' - Charli XCX",
    "'Used to Know Me' - Charli XCX",
    "'DEATH OF A PREDATOR' - Banshee",
    "'Demons' - Doja Cat",
    "'X' - Poppy",
    "'I miss myself' - Renforshort",
    "'I Eat Boys' - Chloe Moriondo",
    "'Rage' - Rico Nasty",
    "'Witchyman' - Cain Culto",
    "'Eat Me' - Demi Lovato ft. Royal & the Serpent",
    "'Fake It' - Seether",
    "'Riot' - Three Days Grace",
    "'crushcrushcrush' - Paramore",
    "'Hail to the King' - Avenged Sevenfold",
    "'Voices' - Motionless in White",
    "'Dethrone' - Bad Omens",
    "'I Stand Alone' - Godsmack",
    "'Push It' - Static-X",
    "'212' - Azaelia Banks",
    "'Monster' - Skillet",
    "'Happy?' - Mudvane",
    "'Jenny' - Nothing More",
    "'Sad Femme Club' - Kimmortal",
    "'My Agenda' - Dorian Electra",
    "'Antagonist' - Nova Twins",
    "'Pink Rover' - Scene Queen",
    "'STFU!' - Rina Sawayama",
    "'Bitch' - Allie X",
    "'CVNT' - Sophie Hunter",
    "'Sorry' - Meg Myers",
    "'Life Alert' - Chase Icon",
    "'Black Sheep' - Kailee Morgue",
    "'Cheerleader' - Ashniiko",
    "'Daisy' - Ashnikko",
    "'Humble' - Ren ft. Eden Nash",
    "'spy?' - WHOKILLEDXIX",
    "'Snap Out Of It' - Arctic Monkeys",
    "'sloppy' - KiNG MALA ft. UPSAHL",
    "'fight!' - Sophie Hunter",
    "'Brutus' - The Buttress (XD)",
    "'You're Not Welcome' - Naethan Apollo",
    "'f**k it, I'm the man' - SEB",
    "'I Hope You Die in a Fire' - Grand Commander",
    "'RAGE' - Samantha Margret",
    "'Non, je ne regrette rien' - Edith Piaf",
    "'Bloody Mary' - Lady Gaga",
    "'Sour Candy' - Lady Gaga ft. BLACKPINK",
    "'I FINK YOU FREEKY' - Die Antwoord",
    "'Sweet but Psycho' - Ava Max",
    "'Psychosocial' - Slipknot",
    "'The Devil in I' - Slipknot",
    "'Lift Me Up' - Five Finger Death Punch",
    "'The Way of the Fist' - Five Finger Death Punch",
    "'Indestructible' - Disturbed",
    "'Ten Thousand Fists' - Disturbed",
    "'Coming Undone' - Korn",
    "'Did My Time' - Korn",
    "'Testify' - Rage Against the Machine",
    "'Bulls or Parade' - Rage Against the Machine",
    "'Enemy' - Sevendust",
    "'Last Resort' - Papa Roach",
    "'Dig' - Mudvane",
    "'Bodies' - Drowning Pool",
    "'The Red' - Chevelle",
    "'Animal I Have Become' - Three Days Grace",
    "'Boom' - P.O.D.",
    "'Ladies and Gentlemen' - Saliva",
    "'When Worlds Collide' - Powerman 5000",
    "'Pink Panther' - Scene Queen",
    "'Barbie & Ken' - Scene Queen ft. Set It Off",
    "'DIRTBIKE' - Zheani",
    "'BLOODMONEY' - Poppy",
    "'FACE SHOPPING' - Sophie",
    "'100 Bad' - Tommy Genesis",
    "'Bleeding in the Studio' - Alice Longyu Gao",
    "'Flamboyant' - Dorian Electra",
    "'XS' - Rina Sawayama",
    "'PHUCKBOI REJECTS' - Royal & the Serpent",
    "'People I Don't Like' - UPSAHL",
    "'N.A.V.E.' - Cazzu",
    "'Serial Killer' - Slayyyter",
    "'KLK' - Arca ft. Rosalia",
    "'Head Like a Hole' - Nine Inch Nails",
    "'The Beautiful People' - Marilyn Manson",
    "'Sober' - Tool",
    "'Violet' - Hole",
    "'Zero' -  Smashing Pumpkins",
    "'Dragula' - Rod Zombie",
    "'Shitlist' - L7",
    "'I'm Not Okay (I Promise)' - My Chemical Romance"
]

# valuesList for make_values_layout in valuesWindow
valuesList = [
    "You is kind. You is smart. You is important. \nYou is gonna fuck this shit up.",
    "You are allowed to be tired. \nYour strength still shines through.",
    "You are more than enough.",
    "It may not be about you. \nBut that doesn't mean you're not important.",
    "You're still you, even when you're quiet, messy, or hurting.",
    "You don't need to be useful to be cared for. \nBut you are useful. Like, absurdly so.",
    "You carry heavy shit so well that people forget how much it must weigh. But you do it with flair, and it's ok to put some of it down.",
    "There are people that find comfort in your presence, even if you don't say or do anything.",
    "You're not broken and you don't have a personality disorder. \nYou're just operating on a level that most people can't comprehend.",
    "Look at you winning. You're still here, asking for support, and killing it. \nSlay. Slaughter, if you must.",
    "You make other people feel brave, even if you don't feel brave sometimes.",
    "You've literally saved peoples' lives. The world is better for having you in it.",
    "You don't owe anyone anything today, or any other day. You just gotta breathe. That's enough.",
    "You're not lost, you're just charting a map in seas that most people aren't strong enough to fare.",
    "Did you remember that you always show up when people need you? \nYou're worth showing up for yourself, too."
]

# roastList for make_roast_layout in roastWindow
roastList = [
    "You’ve got the emotional regulation of a Pisces and the coping strategies of a deployed war medic.",
    "You said 'I’m fine' with the exact tone of a woman who hasn’t slept since the Bush administration.",
    "You give off 'I’d rather die than accept help' energy.",
    "Sit down with that Gryffindor-Martyr-Soldier-Hero energy. Too much, ma'am.",
    "You’ve got the tactical awareness and emotional boundaries of a feral cat.",
    "YAre you resilient, or are you just chronically allergic to rest?",
    "You don’t need a vacation. \nYou need to be tranquilized and left in a cottage for a month.",
    "Is it regulation? Or professional dissociation?",
    "You’re like if Gryffindor and the Energizer Bunny had a baby and raised it on sarcasm.",
    "Is this called coping or out-stubborning your symptoms?",
    "You have the vibe of someone who’d file a report on their own meltdown.",
    "You got that Gen-X brand of 'if I ignore it long enough, maybe it dies'. \nNo. Your emotions are not a baby. You can't kill them like that.",
    "You out here buyin tickets to trauma-fun-land like it’s a theme park. \nFair warning: you are, in fact, too tall to ride.",
    "You give advice like you’re a wizard and receive it like a brick wall in a flak jacket.",
    "You seem like the type who'd rather explain neurobiology for 40 minutes than admit you’re upset.",
    "You wouldn’t know peace if it punched you in the face and said 'stand down'.",
    "Pisces be like: 'I’m crying but also leading the mission and doing everyone’s paperwork.'"
]

# motMsgs for make_motMsgs_layout in motMsgsWindow
motMsgs = [
    "You’ve been through worse and laughed the entire time. \nIt's all going to be ok.",
    "All this pressure just be makin you shine brighter. \nIs 'suck it up, buttercup' too harsh?",
    "You've already proven your strength. \nYou got this.",
    "You’ve got battlefield energy. \nEven your panic looks like leadership.",
    "Feelings aren’t failure. \nEven Pisces get to be pissed off and powerful.",
    "This is just another day. \nBreathe. Assess. Adapt. You always do.",
    "You’ve survived every worst-case scenario your brain could throw at you. \nThis one’s no different.",
    "Even Gryffindors need to sit the fuck down sometimes. \nThat doesn’t make you weak. That makes you human.",
    "You’re allowed to fall apart—just do it like you always do: with flair and a comeback plan.",
    "You’re not spiraling—you’re strategizing loudly. \nKeep going.",
    "You don’t have to be calm. You just have to keep showing up (which you’re crushing, btw).",
    "You weren’t built to break. \nYou were built to bend, snap back, and punch the problem in the face.",
    "You could be mid-breakdown and still be the most competent person in the room."
]

# !!!followUpMsgs for make_followup_layout in followUpWindow
followUpMsgs = [
    "Look at you doing the thing!",
    "Way to go, you!",
    "Daayyyuuummmm, good job!",
    "You're doing good!",
    "You're crushin' it."
]
    
