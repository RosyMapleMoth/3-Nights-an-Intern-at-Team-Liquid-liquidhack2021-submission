# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

init python:
    if renpy.windows:
        config.tts_voice = "Zira"
    elif renpy.macintosh:
        config.tts_voice = "Samantha"
    elif renpy.linux:
        config.tts_voice = "english_rp"

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

    define gui.text_size = 15

    "My qualifications for running Team Liquids social media team? Oh honey, I run the entire internet. Why do you think cat videos are so popular on your tiktok feed? The only thing bigger than frogs on the internet are cats. Mmmmeow. "

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
        url = WEBHOOK_URL_HERE
        data = {"content": myText}
        result = requests.post(url, json = data)

    return
