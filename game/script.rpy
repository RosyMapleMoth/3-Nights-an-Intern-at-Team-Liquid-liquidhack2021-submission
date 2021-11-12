# The script of the game goes in this file.

# Define Characters Below
define janet = Character("Janet")
define yoshi = Character("Yoshi")
define blue = Character("Blue")

# Define Settings
define gui.namebox_borders = Borders(5, 5, 5, 5)
define transition_circle_iris_in = ImageDissolve("imagedissolve circleiris.png", 1.0, 8, reverse=True)
define transition_circle_iris_out = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)

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


    scene bg slack at top
    with transition_circle_iris_out

    show janet smiling at center with dissolve:
        zoom 0.5

    janet "Good morning Blue! Welcome to your first day at Team Liquid. My name is Janet, I use she/her pronouns, I am the EDU Esports Coordinator for TL!"
    janet "I cover most everything from our awesome hackathons to education events."
    janet "I know you were wanting to become TL’s next competitive Minecraft player, but I think you’re really going to fit in here with the education team!"
    janet "I'll also introduce you to some of the other awesome people in other teams and you can learn about other jobs here at TL and different careers in Esports."
    janet "We are all about collaboration, cooperation, and fun here so please ask away if you have any questions!"
    janet "Even though you’re going to be working with the education team, I’d encourage you to reach out to other people and ask them about their jobs!"

    label meet_menu:
        scene bg slack at top
        with transition_circle_iris_out

        show janet smiling at center with dissolve:
            zoom 0.5

        janet "Who would you like to meet today?"
        menu():
            "Zoe (Social Media Team)":
                jump meet_menu
            "Yoshi (Community Management)":
                jump moderation_minigame
            "Vivian (Copywriter)":
                jump creative_post_minigame
            "SeaGnome (Tournament Manager)":
                jump meet_menu

    # MODERATION MINIGAME --------------------------------------------------------
    label moderation_minigame:
        scene bg slack at top
        with transition_circle_iris_out

        show yoshi smiling at center with dissolve:
            zoom 0.5

        yoshi "Hiya I’m Yoshi. I use he/him pronouns. You’ve probably seen me hanging around the Team Liquid discord server or on the TL Minecraft server."
        yoshi "I'm a community manager, so I put together the awesome events Team Liquid hosts. I am by no means the face of Team Liquid, but rather doing a lot of the backend stuff, the weithers as it were."
        yoshi "I work with the community management team developing events. My role is that of a moderator and event planner! I keep the Discord server running smoothly, and also run the official Team Liquid Minecraft server!"
        yoshi "It’s really wonderful being a community manager. {i}Being in the shadows, in the community, behind something you love.{/i}"

        blue "\"So you basically have the career goals of a 12 year old?\""

        yoshi "Yeah pretty much. I think over that time I acquired a thick skin. You have to get used to the jokes, Minecraft SMPEarth references, and the mean stuff that people can say on the internet."
        yoshi "Are you sure you want to help out being a moderator? It’s challenging stuff!"

        show screen moderation_minigame_displayable with dissolve

        image _user1 = "mod mg user 1.png"  # rickroll naruto
        image _user2 = "mod mg user 2.png"  # future minecraft esports
        image _user3 = "mod mg user 3.png"  # free csgo skins
        image _user4 = "mod mg user 4.png"  # rp mommy giftcard warn
        image _user5 = "mod mg user 5.png"  # bot ban

        show _user1 at truecenter
        alt "Hello. Here they give out Liquid+ points for free. I think it won’t last long). Hurry up. https://bit.ly/3kEltin"

        $ pass_q1 = False
        label _user1:
            menu():
                "Help":
                    "Okay, guess you can 'help' them test that link. Try clicking on {a=https://bit.ly/3kEltin}https://bit.ly/3kEltin{/a}!"
                    "But seriously, in general people should not click on links they don't recognize or trust."

                "Warn":
                    "Correct! If you click, it's a harmless {a=https://bit.ly/3kEltin}video{/a}. Telling a person to stop is good enough if community members get annoyed."
                    $ pass_q1 = True

                "Ban":
                    "Banning is too harsh in this case. The {a=https://bit.ly/3kEltin}bit.ly link{/a} goes to a Rick Roll video and a warning can suffice if community members are annoyed."
        $ if not pass_q1: renpy.jump('_user1')
        hide _user1 with pixellate

        show _user2 at truecenter
        $ pass_q2 = False
        label _user2:
            menu():
                "Help":
                    "Yes! This kid has got dreams and you can point in the right direction to learn more about TL's Minecraft events."
                    $ pass_q2 = True

                "Warn":
                    "But what did the kid do wrong? :("

                "Ban":
                    "How could you crush this person's dreams?! :("
        $ if not pass_q2: renpy.jump('_user2')

        scene bg slack at top
        with transition_circle_iris_out
        show yoshi smiling at center with dissolve:
            zoom 0.5
        yoshi "Wow, you did an amazing job! Thanks for all your help."
        jump meet_menu
    # MODERATION FIN --------------------------------------------------------



    # CREATIVE WRITING POST MINIGAME --------------------------------------------------------
    label creative_post_minigame:
        scene bg slack at top
        with transition_circle_iris_out

        show janet smiling at center with dissolve:
            zoom 0.5

        janet "Effective marketing campaigns and copywriting are all about being a good storyteller!"

        janet "It's about creating compelling narratives. Fun engagement about eSports teams, mascots, and more to build unique branding."
        janet "Why don't you give it a shot? I'll give you a prompt, try to craft something in 250 characters or less."
        janet "You can only get better at writing if you practice! Give it your best."

        scene black
        with pushright

        # shows screen with dissolve, then fades out with dissolve and shows return value
        call screen creative_writing_minigame_displayable with dissolve
        $ tweet_copy = _return

        scene bg slack
        show janet smiling at center:
            zoom 0.5
        with pushleft

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
                janet "You can also read what other people have written! I wouldn't be surprised if my colleague Vivian was the first to comment under your Tweet. She really loves storytelling and writing too."

            "No thanks.":
                janet "No worries. If you'd ever like to share later, just let me know!"
                janet "If you'd like to see what others have written and get inspired, visit {a=https://twitter.com/TL_BlueBae}Twitter @TL_BlueBae{/a}."

        jump meet_menu
        # CREATIVE WRITING POST FIN --------------------------------------------------------

return
