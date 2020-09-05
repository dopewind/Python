#  all the imports
import getpass                        # for entering the password
import sys                            # for  typing effect
from os import system, name           # for clearing screen
from time import sleep                # for showing output for some time period
from subprocess import call           # import call method from subprocess module
# from pynput import keyboard            # for the keyboard shortcuts
import signal
import os
import subprocess
import random


def handler(signum, frame):
    print('You didn\'t say the magic word'), signum


# ------------------------------------installs-----------------------------------

# pip install pynput
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# ------------------------------------lists----------------------------------------------

greetings_as_intentions = [
    'hi', 'hello', 'hey', 'hola', 'hey there', "heylo"
]

goodbyes_as_intentions = [
    'bye', 'see ya', 'see you', 'see you later', 'goodbye'

]

ai_qn_as_intentions = [
    'who are you?', 'who are you', 'are you human', 'are you human?'

]

# ------------------------------------------------- FUNCTIONS -------------------------------------------------

# define our clear function


def clear():

    print("\n")
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def sleep_clear():
    sleep(1.5)
    clear()


# def pass_input():
#    typing_effect_ideal("Enter your password. Keep in mind that your password won't be visible on your screen as you type it")
#    password = getpass.getpass("Password = ")

def typing_effect_really_fast(texts):
    for char in texts:
        sleep(0.003)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")


def typing_effect_really_slow(texts):
    for char in texts:
        sleep(0.3)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")


def typing_effect_ideal(texts):
    for char in texts:
        sleep(0.019)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")


def typing_effect_really_fast_line(texts):
    for char in texts:
        sleep(0.003)
        sys.stdout.write(char)
        sys.stdout.flush()


def typing_effect_really_slow_line(texts):
    for char in texts:
        sleep(0.3)
        sys.stdout.write(char)
        sys.stdout.flush()


def typing_effect_ideal_line(texts):
    for char in texts:
        sleep(0.019)
        sys.stdout.write(char)
        sys.stdout.flush()


# Keyboard shortcut things begin


# The currently active modifiers
# current = set()

# # The key combination to check
# COMBINATIONS = [
#     {keyboard.Key.shift, keyboard.KeyCode(char='a')},
#     {keyboard.Key.shift, keyboard.KeyCode(char='A')}
# ]

# # The currently active modifiers
# current = set()

# def execute():
#     print ("Do Something")

# def on_press(key):
#     if any([key in COMBO for COMBO in COMBINATIONS]):
#         current.add(key)
#         if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
#             execute()

# def on_release(key):
#     if any([key in COMBO for COMBO in COMBINATIONS]):
#         current.remove(key)

# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()

def name_input():
    name = ''
    say_name = ['Gotta spill it dude', 'C\'mon say it', 'You can\'t see the rest without it',
                'Why so serious?', 'Just say it', 'imma call you princess otherwise', 'You don\'t get it do you?', "What\'s holding you back?", ':/']  # Random things to say if no name is given
    while True:
        try:
            typing_effect_ideal("What's your name?")
            name = input('Name = ')
            print('')
        except ValueError:
            typing_effect_ideal('Say what now?')
            sleep_clear()
        if name in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            say_this = random.choice(say_name)  # Generating a random thing
            typing_effect_ideal(say_this)
            sleep_clear()
            continue
        else:
            break
    typing_effect_ideal_line("You call yourself ")
    typing_effect_ideal(name)
    sleep_clear()
    typing_effect_ideal("Noice")
    sleep_clear()


def alpha():
    typing_effect_really_fast(""" 
 $$$$$$\                  $$\                  $$$$$$\  $$\           $$\                 
$$  __$$\                 $$ |                $$  __$$\ $$ |          $$ |                
$$ /  \__| $$$$$$\   $$$$$$$ | $$$$$$\        $$ /  $$ |$$ | $$$$$$\  $$$$$$$\   $$$$$$\  
$$ |      $$  __$$\ $$  __$$ |$$  __$$\       $$$$$$$$ |$$ |$$  __$$\ $$  __$$\  \____$$\ 
$$ |      $$ /  $$ |$$ /  $$ |$$$$$$$$ |      $$  __$$ |$$ |$$ /  $$ |$$ |  $$ | $$$$$$$ |
$$ |  $$\ $$ |  $$ |$$ |  $$ |$$   ____|      $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$  __$$ |
\$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$$\       $$ |  $$ |$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$ |
 \______/  \______/  \_______| \_______|      \__|  \__|\__|$$  ____/ \__|  \__| \_______|
                                                            $$ |                          
                                                            $$ |                          
                                                            \__|                          """)

    typing_effect_really_fast("""
                                                                         $$\                   
                                                                          \__|                  
$$$$$$$\  $$$$$$\ $$\  $$\  $$\        $$$$$$\ $$\   $$\$$$$$$$\ $$$$$$$\ $$\$$$$$$$\  $$$$$$\  
$$  __$$\$$  __$$\$$ | $$ | $$ |      $$  __$$\$$ |  $$ $$  __$$\$$  __$$\$$ $$  __$$\$$  __$$\ 
$$ |  $$ $$ /  $$ $$ | $$ | $$ |      $$ |  \__$$ |  $$ $$ |  $$ $$ |  $$ $$ $$ |  $$ $$ /  $$ |
$$ |  $$ $$ |  $$ $$ | $$ | $$ |      $$ |     $$ |  $$ $$ |  $$ $$ |  $$ $$ $$ |  $$ $$ |  $$ |
$$ |  $$ \$$$$$$  \$$$$$\$$$$  |      $$ |     \$$$$$$  $$ |  $$ $$ |  $$ $$ $$ |  $$ \$$$$$$$ |
\__|  \__|\______/ \_____\____/       \__|      \______/\__|  \__\__|  \__\__\__|  \__|\____$$ |
                                                                                      $$\   $$ |
                                                                                      \$$$$$$  |
                                                                                       \______/ """)

    sleep_clear()
    typing_effect_really_fast("""
$$$$$$$\ $$\                           $$\                                                             
$$  __$$\$$ |                          $$ |                                                            
$$ |  $$ $$ |$$$$$$$\        $$$$$$$\$$$$$$\   $$$$$$\  $$$$$$\        $$$$$$$\  $$$$$$\ $$\  $$\  $$\ 
$$$$$$$  $$ $$  _____|      $$  _____\_$$  _| $$  __$$\$$  __$$\       $$  __$$\$$  __$$\$$ | $$ | $$ |
$$  ____/$$ \$$$$$$\        \$$$$$$\   $$ |   $$ /  $$ $$ /  $$ |      $$ |  $$ $$ /  $$ $$ | $$ | $$ |
$$ |     $$ |\____$$\        \____$$\  $$ |$$\$$ |  $$ $$ |  $$ |      $$ |  $$ $$ |  $$ $$ | $$ | $$ |
$$ |     $$ $$$$$$$  |      $$$$$$$  | \$$$$  \$$$$$$  $$$$$$$  |      $$ |  $$ \$$$$$$  \$$$$$\$$$$  |
\__|     \__\_______/       \_______/   \____/ \______/$$  ____/       \__|  \__|\______/ \_____\____/ 
                                                       $$ |                                            
                                                       $$ |                                            
                                                       \__|                                            """)

    sleep_clear()

    typing_effect_really_fast("""
$$$$$$\   $$\             $$\        $$$$$$\          $$\                    $$\      $$\$$\$$\                              
$$  __$$\  $$ |            $$ |      $$  __$$\         $$ |                   $$ |     \__$$ $$ |                             
$$ /  \__$$$$$$\   $$$$$$\ $$ |      $$ /  \__|      $$$$$$\   $$$$$$\        $$ |  $$\$$\$$ $$ |      $$$$$$\$$$$\  $$$$$$\  
$$ |     \_$$  _| $$  __$$\$$ $$$$$$\$$ |            \_$$  _| $$  __$$\       $$ | $$  $$ $$ $$ |      $$  _$$  _$$\$$  __$$\ 
$$ |       $$ |   $$ |  \__$$ \______$$ |              $$ |   $$ /  $$ |      $$$$$$  /$$ $$ $$ |      $$ / $$ / $$ $$$$$$$$ |
$$ |  $$\  $$ |$$\$$ |     $$ |      $$ |  $$\         $$ |$$\$$ |  $$ |      $$  _$$< $$ $$ $$ |      $$ | $$ | $$ $$   ____|
\$$$$$$  | \$$$$  $$ |     $$ |      \$$$$$$  |        \$$$$  \$$$$$$  |      $$ | \$$\$$ $$ $$ |      $$ | $$ | $$ \$$$$$$$\ 
 \______/   \____/\__|     \__|       \______/          \____/ \______/       \__|  \__\__\__\__|      \__| \__| \__|\_______|
                                                                                                                              
                                                                                                                              
                                                                                                                              """)

    sleep_clear()
    sleep(3)

    typing_effect_really_fast("""
$$$$$$\                       $$$$$$\                        $$\                  
$$ ___$$\                     $$  __$$\                     $$$$ |                 
\_/   $$ |                    \__/  $$ |                    \_$$ |                 
  $$$$$ /                      $$$$$$  |                      $$ |                 
  \___$$\                     $$  ____/                       $$ |                 
$$\   $$ |                    $$ |                            $$ |                 
\$$$$$$  $$\$$\$$\$$\$$\$$\$$\$$$$$$$$\$$\$$\$$\$$\$$\$$\$$\$$$$$$\$$\$$\$$\$$\$$\ 
 \______/\__\__\__\__\__\__\__\________\__\__\__\__\__\__\__\______\__\__\__\__\__|
                                                                                   
                                                                                   
                                                                                   
    """)

    sleep_clear()

    typing_effect_really_fast("""
    
$$$$$$\ $$\         $$\         $$\       $$\     
$$  __$$\$$ |        \__|        $$ |      $$ |    
$$ /  $$ $$ |$$$$$$\ $$\ $$$$$$\ $$$$$$$\$$$$$$\   
$$$$$$$$ $$ $$  __$$\$$ $$  __$$\$$  __$$\_$$  _|  
$$  __$$ $$ $$ |  \__$$ $$ /  $$ $$ |  $$ |$$ |    
$$ |  $$ $$ $$ |     $$ $$ |  $$ $$ |  $$ |$$ |$$\ 
$$ |  $$ $$ $$ |     $$ \$$$$$$$ $$ |  $$ |\$$$$  |
\__|  \__\__\__|     \__|\____$$ \__|  \__| \____/ 
                        $$\   $$ |                 
                        \$$$$$$  |                 
                         \______/                  """)
# ----------------------- ACTUAL PROGRAM ---------------------------------


clear()

alpha()

sleep_clear()

typing_effect_ideal("Hello")

sleep_clear()

typing_effect_ideal(
    "Just keep in mind that I'm just a stupid piece of code and I AM NOT as smart as you")

sleep_clear()

typing_effect_ideal("Yeah,       I meant it")

sleep_clear()

typing_effect_ideal("And just so that we are clear, please use proper grammar")

sleep_clear()

name_input()
# pass_input()


# just providing a separator for fun
typing_effect_really_fast(

    """                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\$$$$$$\ 
\______\______\______\______\______\______\______\______\______\______\______\______\______\______\______\______\______\______\______\______\______\______|
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           """)
print("\n")

typing_effect_ideal("Hello another random user")
print("\n")

typing_effect_ideal(
    "Please don't be fooled by my initial courteous language, I can get very annoying, as you saw with all the typing effects")

sleep_clear()

typing_effect_really_fast("I can go really fast like this")

sleep_clear()

typing_effect_really_slow("and really slow like this")

sleep_clear()

typing_effect_ideal("Or as slow at it gets, but I think you get the idea")

sleep_clear()

typing_effect_ideal(
    "So if you aren't ready for this, kill me now before you start regretting it")

sleep_clear()

typing_effect_really_slow("3......2.........1......")

# Set the signal handler
signal.signal(signal.SIGINT, handler)

sleep_clear()

typing_effect_ideal(
    "So just keep in mind that if I type really slow, it's just to annoy you")

sleep_clear()

typing_effect_ideal("Feeling annoyed yet :)")
print("")
typing_effect_ideal(
    "The guy who wrote this sure got annoyed by all the slow typing while debugging this :/ ")

sleep_clear()

typing_effect_ideal("May I ask what are you doing here?")
the_reason = input("--> ")

sleep_clear()

typing_effect_ideal("Why'd I ask?   Just to make conversation ")

sleep_clear()

typing_effect_ideal_line("Now this is why you came here ?  ----->  ")
# typing_effect_ideal_line("\"")
typing_effect_ideal(the_reason)
# typing_effect_ideal_line("\"")

sleep_clear()

typing_effect_really_slow("Duh")

sleep_clear()

typing_effect_ideal("Now lets cut to the chase")

sleep_clear()

typing_effect_ideal("What are you really here for?")

real_intention = input("--->")

#typing_effect_ideal_line("Now this is why you came here for real ?  ----->  ")
# typing_effect_ideal_line("\"")
# typing_effect_ideal(real_intention)
# typing_effect_ideal_line("\"")


if real_intention in greetings_as_intentions:
    typing_effect_ideal("How you doin'?")

else:
    if real_intention in goodbyes_as_intentions:
        typing_effect_ideal("See ya later")
