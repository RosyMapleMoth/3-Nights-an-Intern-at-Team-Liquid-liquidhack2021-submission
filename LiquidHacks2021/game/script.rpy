# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    e "Okay, time for you to write your own story!"
    e "In less than or equal to 200 characters, write about prompt x!"

    # This ends the game.

    # shows screen with dissolve, then fades out with dissolve and shows return value
    call screen creative_writing_minigame_displayable with dissolve
    with pixellate
    $ myText = _return

    "You wrote [myText], huh? Let's webhook you to Discord while we wait for Twitter Dev approval."

    # Temporarily
    python:
        import requests
        url = 'https://discord.com/api/webhooks/906723323747135488/uvCV67O9azqbBsuBEWbi5vl9oBrRDg2oBIuOtK_uVyIqu17KS-VdiimJ6ldw8c1qC097'
        data = {"content": myText}
        result = requests.post(url, json = data)

    return
