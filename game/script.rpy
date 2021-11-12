# The script of the game goes in this file.

# Define Characters Below
define janet = Character("Janet")
define yoshi = Character("Yoshi")
define blue = Character("Blue (You)")

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
    call screen preferences with pixellate
    play music gamemenu fadeout 1.0 fadein 1.0

    scene black with dissolve

    show text "\"There's a reason why Team Liquid hires so many remote employees... \
    \nthey're all centaurs...\"\
    \n~ Sarah"
    with dissolve
    pause 4
    with dissolve

    "\"I have real legs!\" ~ Gamerhcp" with dissolve
    hide text

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
    hide janet with dissolve

    blue "\"Thanks Janet! I can't wait to meet everyone.\""
    $ must_meet_zoe = True
    $ must_meet_yoshi = True
    $ must_meet_janet = True

    label meet_menu:
        scene bg slack at top with transition_circle_iris_out

        show janet smiling at center with dissolve:
            zoom 0.5

        janet "Alright, who would you like to meet today?"

        $ conclusion_activated = not (must_meet_zoe or must_meet_yoshi or must_meet_janet)

        menu():
            "Zoe (Social Media)" if must_meet_zoe:
                jump meet_menu
            "Yoshi (Community Management)" if must_meet_yoshi:
                jump moderation_minigame
            "Janet (Marketing & Writing)" if must_meet_janet:
                jump creative_post_minigame
            "Meme Mini game test": 
                jump meme_maker
            "I've met everyone!" if conclusion_activated:
                jump conclusion

    # MODERATION MINIGAME --------------------------------------------------------
    label moderation_minigame:
        scene bg slack at top
        with pixellate

        show yoshi smiling at center with dissolve:
            zoom 0.5

        yoshi "Hiya I’m Yoshi. I use he/him pronouns. You’ve probably seen me hanging around the Team Liquid discord server or on the TL Minecraft server."
        yoshi "I'm a community manager, so I put together the awesome events Team Liquid hosts. I am by no means the face of Team Liquid, but rather doing a lot of the back stuff, the weithers as it were."
        yoshi "I work with the community management team developing events. My role is that of a moderator and event planner! I keep the Discord server running smoothly, and also run the official Team Liquid Minecraft server!"
        yoshi "It’s really wonderful being a community manager. {i}Being in the shadows, in the community, behind something you love.{/i}"

        blue "\"So you basically have the career goals of a 12 year old?\""

        yoshi "Yeah pretty much. I think over that time I acquired a thick skin. You have to get used to the jokes, Minecraft SMPEarth references, and the mean stuff that people can say on the internet."
        yoshi "Are you sure you want to help out being a moderator? It’s challenging stuff!"

        show screen moderation_minigame_displayable with dissolve
        play music moderationminigame fadeout 1.0 fadein 1.0

        image _user1 = "mod mg user 1.png"  # rickroll naruto
        image _user2 = "mod mg user 2.png"  # future minecraft esports
        image _user3 = "mod mg user 3.png"  # fake doublelift scammer
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
        hide _user2 with pixellate

        show _user3 at truecenter
        $ pass_q3 = False
        label _user3:
            menu():
                "Help":
                    "Do you really think that's DoubleLift?"

                "Warn":
                    "Try again. Impersonation is really serious."

                "Ban":
                    "Yes, ban that impersonating scammer!!"
                    $ pass_q3 = True

        $ if not pass_q3: renpy.jump('_user3')
        hide _user3 with pixellate

        show _user4 at truecenter
        $ pass_q4 = False
        label _user4:
            menu():
                "Help":
                    "Ummm, read the community guidelines again and think this through."

                "Warn":
                    "That person is begging for money and is kinda being creepy and sexualized which goes against our community rules!"
                    "You could warn them but in this case, let’s go ahead and ban them."

                "Ban":
                    "Yep, this person needs to go. Let's keep the community safe and respectful."
                    $ pass_q4 = True

        $ if not pass_q4: renpy.jump('_user4')
        hide _user4 with pixellate

        show _user5 at truecenter
        $ pass_q5 = False
        label _user5:
            menu():
                "Help":
                    "What?! Why don't you read the community guidelines again?"

                "Warn":
                    "Nope, see that blue tag?! It's a bot!!"

                "Ban":
                    "Grab that ban hammer and send that scammer to the shadow realm!"
                    $ pass_q5 = True

        $ if not pass_q5: renpy.jump('_user5')
        hide _user5 with pixellate

        # Finish all Q's
        scene bg slack at top
        with transition_circle_iris_out
        show yoshi smiling at center with dissolve:
            zoom 0.5
        yoshi "Wow, you did an amazing job! Thanks for all your help."
        yoshi "Amazing work today. I hope you have a great night's rest."

        scene black with dissolve

        show text "Good job! You sleep for a few hours..." with dissolve
        pause 3
        with dissolve

        hide text
        "No more snoozing, it's time to get up!"

        $ must_meet_yoshi = False
        jump meet_menu
    # MODERATION FIN --------------------------------------------------------



    # CREATIVE WRITING POST MINIGAME --------------------------------------------------------
    label creative_post_minigame:
        scene bg slack at top
        with transition_circle_iris_out

        show janet smiling at center with dissolve:
            zoom 0.5

        janet "Oh hey, you want to talk more with me?"
        janet "Well, I can tell you more about writing and marketing since I run tons of events and create lots of educational content."
        janet "Effective marketing campaigns and copywriting are all about being a good storyteller!"

        janet "It's about creating compelling narratives. Fun engagement about eSports teams, mascots, and more to build unique branding."
        janet "Why don't you give it a shot? I'll give you a prompt, try to craft something in 250 characters or less."
        janet "You can only get better at writing if you practice! Give it your best."

        scene black
        with pushright

        # shows screen with dissolve, then fades out with dissolve and shows return value
        play music cwminigame fadeout 1.0 fadein 1.0
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

        # Finish all Q's
        janet "Woah, look at the time. Work-life balance is important! I hope you have a great night's rest."

        scene black with dissolve

        show text "Well done on your assignment. You sleep and lose a few games of TFT..." with dissolve
        pause 3
        with dissolve

        hide text
        "Time to stop horsing around, it's a new workday!"

        $ must_meet_janet = False
        jump meet_menu
        # CREATIVE WRITING POST FIN --------------------------------------------------------


    label meme_maker:
        scene bg slack at top
        with pixellate


        "Tester" "Hello, this is so very exciting today we will be making a meme" 

        call screen meme_maker_minigame_displayable


        # CONCLUSION BEGINS --------------------------------------------------------
    label conclusion:
        janet "Oh wow you've met a lot of people in your 3 days as an intern! I hope you learned a lot and had fun talking with some of the other departments."
        janet "You've done such a great job. You should apply on our {a=https://careers.teamliquid.com/}careers page{/a} so you can become #PaidBySteve too!"

        menu():
            "Let me submit my application right now!!":
                janet "Wow, I love your enthusiasm. I'm so glad you had a good time on your internship!"
                janet "Also, Blue?"
                pause
                janet "I just want you I'm really proud of you. You're not just a cute mastcot to me."
                janet "You're so smart, and I think you can do anything you put your mind to."
                janet "It's okay to not know what you want to do, and I'm glad you got to try out new things and find something new you're passionate about."
                pause
                show text "Janet sends you an e-hug gif..." with dissolve
                pause 3
                with dissolve

                hide text
                "Congrats on beating the game!"
                pause
                "{i}3 Nights an Intern at Team Liquid{/i} was made by Bellbellum, Ocarune, Brekcut, and Moth for LiquidHacks 2.0. Thanks for playing!"

            "Not right now, maybe later.":
                janet "Ah, okay, no worries! If you ever want someone to review your resume, we sometimes hold job fairs and other events!"
                janet "Alright, I'm off for a TFT break but I'll see you later. (PS Vex with Bramble is broken)"
                hide janet with dissolve

                # show Sarah's video

                # more text here

    # CONCLUSION FIN --------------------------------------------------------
return
