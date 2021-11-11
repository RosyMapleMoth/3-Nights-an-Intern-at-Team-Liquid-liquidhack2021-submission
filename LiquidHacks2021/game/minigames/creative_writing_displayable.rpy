# PATHS
define THIS_PATH = 'minigames/'
define IMG_DIR = 'images/'

# IMAGES
define img_bg_tweet = THIS_PATH + IMG_DIR + "tweet_blank_full.jpg"
define pov = Character("[povname]")

# MINIGAME
screen creative_writing_minigame_displayable():
    default creative_writing_mg_displayable = CreativeWritingDisplayable()
    add Solid('#000')
    add img_bg_tweet:
        xpos 680 ypos 175
        xalign 340

    add creative_writing_mg_displayable



    fixed xpos 50 ypos 50 spacing 100:
        vbox:
            text '✍️ {b}Creative Writing Challenge{/b}':
                 color '#fff'
    fixed xpos 50 ypos 85 spacing 100:
        vbox:
            text 'Prompt: Write the next viral Team Liquid dad joke or fake team name origin story in 250 characters or less.':
                 color '#fff'

    viewport:
        ypos 300
        xpos 370
        xysize 530, 300
        input color "#fff" xmaximum 530 ymaximum 100 length 250


init python:
    import pygame

    class CreativeWritingDisplayable(renpy.Displayable):

        def __init__(self):
            super(CreativeWritingDisplayable, self).__init__()

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            return render
