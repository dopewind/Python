#  all the imports
import getpass                        # for entering the password
import sys                            # for  typing effect
from os import system, name           # for clearing screen
from time import sleep                # for showing output for some time period 
from subprocess import call           # import call method from subprocess module
from pynput import keyboard     # for the keyboard shortcuts              

#------------------------------------installs-----------------------------------

# pip install pynput

#------------------------------------------------- FUNCTIONS -------------------------------------------------

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

def name_input():
    typing_effect_ideal("What's your name?")
    name = input('Name = ')
    print("")


def pass_input():
    typing_effect_ideal("Enter your password. Keep in mind that your password won't be visible on your screen as you type it")
    password = getpass.getpass("Password = ")

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
current = set()

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


# ----------------------- ACTUAL PROGRAM ---------------------------------

clear()

name_input()
#pass_input()

clear()

# just providing a separator for fun
typing_effect_really_fast("-------------------------------------------------------------------------------------------------------")
print("\n")

typing_effect_ideal("Hello another random user")
print("\n")

typing_effect_ideal("Please don't be fooled by my initial courteous language, I can get very annoying, as you saw with all the typing effects")
clear()

typing_effect_really_fast("I can go really fast like this")

sleep_clear()

typing_effect_really_slow("and really slow like this")

sleep_clear()

typing_effect_ideal("So just keep in mind that if I type really slow, it's just to annoy you")

sleep_clear()

typing_effect_ideal("Feeling annoyed yet :)")
print("")
typing_effect_ideal("The guy who wrote this sure got annoyed by all the slow typing while debugging this :/ ")

sleep_clear()

typing_effect_ideal("May I ask what are you doing here?")
the_reason = input("--> ")

sleep_clear()

typing_effect_ideal("Why'd I ask?   Just to make conversation ")

sleep_clear()

typing_effect_ideal_line("Now this is why you came here ?  ----->  ")
typing_effect_ideal_line("\"")
typing_effect_ideal(the_reason)
typing_effect_ideal_line("\"")

sleep_clear()

typing_effect_really_slow("Duh")

sleep_clear()

typing_effect_ideal("Now lets cut to the chase")

sleep_clear()

typing_effect_ideal("What are you really here for?")

real_intention = input("--->")


