# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define l = Character("lady")
define mc = Character("main")

# The game starts here.

label start:

python:
    name = renpy.input ("What is your name?")
    name = name.strip() or "Bob"


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg apocolyptic night


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.


    l "Hello? I need help!!"

    mc "A lady in distress comes running towards me."

    l "Please, my house is coming apart and my friend is under the rubble! Please! Help!"

    "Will you help this lady?"

menu:
    "Yes.":
        jump choice1_yes

    "No, I don't.":
        jump choice2_no
label choice1_yes:
    $ menu_flag = True

    mc "We then rush to the scene."
         
    return

label choice2_no:
    $ menu_flag = False

    "You go home."

    return

    # This ends the game.
