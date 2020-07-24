# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define doom = Character("Doomcraft")
define heisen = Character("Heisenberg")
define yog = Character("Yogurt")
define Brita = Character("Brita")
define Zass = Character("Zass")
define n = Character("Narrator")

# The game starts here.

label start:

    #Doomcraft: I leave this in here for later purposes.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    n "Hello boys and girls. Tonight is a night unlike any night you have witnissed before"
    n "Tonight is the night I will tell you the tale of the People that survived the war..."
    n "Of the thieves and the ghosts."
    n "It was a fierceful battle that resulted in a lot of deaths. A lot of comrades have fallen on both sides."
    doom "Please fill some cool story about how the war has been a tie and everyone is now living in peace on a school or something"
    n "And this is where our story starts."
    jump morning
    # This ends the game.

    return
