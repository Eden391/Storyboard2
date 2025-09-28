# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define l = Character("Lady")

# The game starts here.

label start:

    python:
        name = renpy.input ("What is your name, magical person?")
        name = name.strip()
        hp = 20
    
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

    mc "A lady in distress appears in front of me."

    l "Please, my house is coming apart and my friend is under the rubble! Please! Help!"

    "Will you help this lady, or not?"

menu:
    "Yes.":
        jump choice1_yes

    "No.":
        jump choice2_no
label choice1_yes:
    $ menu_flag = True
    mc "We then rush to the scene."
    mc "I see her friend underneath a large, thick piece of concrete which seemed to have come from the roof."
    mc "An hour later, all is finally resolved."
    show npc1 happy
    l "Thank you! Thank you so much!"
    hide npc1 happy
    show main char happy:
        xalign 0.5
        yalign 1.0

    mc "No worries. It's all I'm here for."
    hide main char happy
    show mc_distress
    show health_10:
        xalign 1.0
        yalign 0.0
    python:
        hp -= 10
    "Your health (20) has gone down by 10. The more you give people your magic, the more your health goes down."
    "If you decide to stop giving people your magic...then so be it."
    
    jump person2     

label choice2_no:
    $ menu_flag = False
    hide npc1 distress
    show mc_very_distress
    show health_20:
        xalign 1.0
        yalign 0.0
    python:
        hp = 20
    "Your health is currently at 20. The more people you give your magic to, the more your health decreases each time by 10.Be careful. If your health goes down to zero, it is game over."
    "If you choose not to help others...so be it."

label person2:
    scene apocalyptic morning bg
    show mc_distress
    play sound "Grass 1"
    mc "It is another day, and I am left feeling uneasy.. as if something is wrong with myself."
    mc "As I walk through fields of grass and tall plants, I hear voices coming from a small house."
    e "AARGH!! Hello!? ANYONE?? I really need some help over here!"
    mc "..Another person?"
    mc "It sounds as if they are stuck."
    hide mc_distress
    show npc2_distress
    e "Ple-aSe! I'm stUck and the vines.. aRe strangling me!!"
    "Will you decide to help this person, and lose the last piece you have of yourself?"

menu:
    "Yes.":
        jump choice3_yea

    "No, I will save myself.":
        jump choice4_nou

label choice3_yea:
    $ menu_flag = True
    "You chose to save them."
    hide main char happy
    hide npc2_distress
    show npc2_thanks
    e "*Gasp* Thank you! Oh my gosh, I thought I was going to-"
    e "Hello?"
    show npc2huuh
    "Your magic ran out... you are no longer a part of this world."
    hide npc2huuh
    show mc ayo:
        xalign 0.75
        yalign 1.0
    "..."
    jump end


label choice4_nou:
    $ menu_flag = False
    e "You're- are you..."
    e "I thought...!"
    "The vines strangle him right in front of you."
    hide npc2_distress
    show mc_very_distress
    "You chose to save yourself."
    "You chose to leave them."
    mc "I still have a bit of my magic left... but that changes nothing."
    "The overwhelming guilt towers over you, and you feel even worse than before."

label end:
    scene bg game over
    "You lost."

#things left to do:
#need to add choice for: do not help lady but help guy
#ADDED HP VARIABLE (if hp = 20 when helping guy, other ending)
#STILL NEED TO ADD TITLE (PLEASE) OR ELSE GO BACK TO SANITY
#sound design (i have a sound app on my ipad if nothing goes right)

return


    # This ends the game.