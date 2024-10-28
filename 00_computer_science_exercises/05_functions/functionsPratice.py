# Functions Pratice, Tyshawn Ricks, v0.0

import random

def helloWorldMulti(): # FUNCTION SIGNATURE
    """This function will output Hello, World! in a language the user chose. """ # DOCSTRING \
    # print a list of languages to the screen, at least three but no more than five.
    # allow the user to select (input) a choice for the language.
    # print "Hello, World!" to the screen in that language.

    print("""Hey, this will print which ever language shown below
        English
        Spanish
        Chinese\n""")

    language = input("Which of the languages above would you like\n").lower()

    if language == "english":
        print("Hello, World")
    elif language == "spanish":
        print("Hola, mundo")
    elif language == "chinese":
        print("世界您好")
    else:
        exit()

helloWorldMulti()