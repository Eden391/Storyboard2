# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define l = Character("lady")

# The game starts here.

label start:

    python:
        name = renpy.input ("What is your name, magical person?")
        name = name.strip()
    
    define mc = Character("[name]")


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg apocolyptic


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show npc1 distress

    # These display lines of dialogue.

    mc "I look out over to the vast oceans, and think about the now ruined, post-apocalyptic world, when-"
    l "Hello? I need help!!"

    mc "A lady in distress comes running towards me."

    l "Please, my house is coming apart and my friend is under the rubble! Please! Help!"

    "Will you help this lady or not?"

menu:
    "Yes.":
        jump choice1_yes

    "No.":
        jump choice2_no
label choice1_yes:
    $ menu_flag = True

    mc "We then rush to the scene."
    mc "I see her friend underneath a large, thick piece of concrete which seemed to have come from the roof."
    mc "an hour later, all is finally resolved."
    l "Thank you! Thank you so much!"
    hide npc1 distress
    show main char happy:
        xalign 0.5
        yalign 1.0

    mc "No worries. It's all I'm here for."
    
    "Your health (20) has gone down by 10. The more you give people your magic, the more your health goes down."
    "If you decide to stop giving people your magic...then so be it."

    jump person2     

label choice2_no:
    $ menu_flag = False
    hide npc1 distress
    show main char happy
    "Your health is currently at 20. The more people you give your magic to, the more your health decreases each time by 10.Be careful. If your health goes down to zero, it is game over."
    "If you choose not to help others...so be it."

label person2:
    scene apocalyptic morning bg
    show eileen happy
    e "Hey!! Hello!? I really need some help over here!"
    e ""



    # This ends the game.