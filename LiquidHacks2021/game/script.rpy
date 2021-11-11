# The script of the game goes in this file.

# Define Characters Below
define janet = Character("Janet")

# Define Settings
define gui.namebox_borders = Borders(5, 5, 5, 5)

# Set up TTS
init python:
    if renpy.windows:
        config.tts_voice = "Zira"
    elif renpy.macintosh:
        config.tts_voice = "Samantha"
    elif renpy.linux:
        config.tts_voice = "english_rp"


# The game starts below.
label start:
    call screen preferences with dissolve

    scene bg room
    show zoe neutral at center with dissolve:
        zoom 0.5

    janet "Effective marketing campaigns and copywriting are all about being a good storyteller!"

    janet "It's about creating compelling narratives. Fun engagement about eSports teams, mascots, and more to build unique branding."
    janet "Why don't you give it a shot? I'll give you a prompt, try to craft something in 250 characters or less."
    janet "You can only get better at writing if you practice! Give it your best!"

    # shows screen with dissolve, then fades out with dissolve and shows return value
    call screen creative_writing_minigame_displayable with dissolve
    with dissolve
    $ tweet_copy = _return

    janet "Wow!! '[tweet_copy]' sounds amazing."
    janet "Do you mind if we share your work on our fan Twitter?"

    menu:
        "Go ahead!":
            # Tweet from bot TL_BlueBae via IFTTT
            python:
                import requests
                url = 'https://maker.ifttt.com/trigger/TL_Webhook/with/key/cHoM4JW3d286vn-TZX_siJ'
                data = {"value1": tweet_copy}
                result = requests.post(url, json = data)
            janet "Woohoo! You can find your writing on {b}{a=https://twitter.com/TL_BlueBae}Twitter @TL_BlueBae{/a}.{/b}"
            janet "You can also read what other people have written! I wouldn't be surprised if Vivian was the first to comment under your Tweet. She really loves storytelling and writing!"

        "No thanks.":
            janet "No worries. If you'd ever like to share later, just let me know!"
            janet "If you'd like to see what others have written and get inspired, visit {a=https://twitter.com/TL_BlueBae}Twitter @TL_BlueBae{/a}."

    return
