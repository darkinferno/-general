# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define doom = Character("Doomcraft")
define heisen = Character("Heisenberg")
define yog = Character("Yogurt")
define Brita = Character("Brita")
define Zass = Character("Zass")
define n = Character("Narrator")
define discord = Character("Discord-Chan")
define pov = Character("[povname]")

define gender = 0
#pronoun one like : he she they
define pro = ""
#pronoun two like him her them
define protwo = ""

# The game starts here.

label start:

    #Doomcraft: I leave this in here for later purposes.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg void

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    "An odd girl appears in front of you."

    #show discord happy

    discord happy "Hoi! I'm Discord-chan!"
    discord "That's funny... I don't recognize you... are you a new user perhaps?"
    discord "What is your gender?"
    menu:
        "I'm male"
            pro = "He"
            protwo = "Him"

        "I'm female"
            pro = "He"
            protwo = "Him"

        "I'm neither"
            pro = "He"
            protwo = "Him"

    discord "That is so cool."
    discord "What's your name?"
    
    
    povname = renpy.input("What is your name?")
    povname = povname.strip()

    if not povname:
         pov = "Pat Smith"

    pov "My name is [pov]!"
    discord "[pov] That's a cute name! hehe"
    discord "Anyways... you're all set!"
    discord "But you don't have any friends... do you?"
    discord "Don't worry, I know the perfect place!"

    scene bg classroom

    yog "I'm telling you guys! Persona 5 is the best of the series!"
    doom "Persona 5 is style over substance" 
    n "Doomcraft shackes his head in disbelieve."


    n "Here is where the game starts. It's pretty WIP rn."

    jump morning
    # This ends the game.

    return
