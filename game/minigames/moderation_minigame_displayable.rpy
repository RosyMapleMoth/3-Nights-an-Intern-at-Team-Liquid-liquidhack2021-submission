# PATHS
define THIS_PATH = 'minigames/'
define IMG_DIR = 'images/'

# IMAGES
define img_user1 = THIS_PATH + IMG_DIR + "mod mg user 1.png"  # rickroll naruto
define img_user2 = THIS_PATH + IMG_DIR + "mod mg user 2.png"  # future minecraft esports
define img_user3 = THIS_PATH + IMG_DIR + "mod mg user 3.png"  # free csgo skins
define img_user4 = THIS_PATH + IMG_DIR + "mod mg user 4.png"  # rp mommy giftcard warn
define img_user5 = THIS_PATH + IMG_DIR + "mod mg user 5.png"  # bot ban

# MINIGAME
screen moderation_minigame_displayable():
    default mod_mg_displayable = ModerationDisplayable()

    add Solid('#000')
    add mod_mg_displayable
    layer "master"

    vbox:
        xpos 50 ypos 50 spacing 100
        text '⚒️ {b}Moderation Challenge{/b}':
             color '#fff'

    vbox:
        xpos 50 ypos 85 spacing 100
        text 'Activity: For each person, decide whether to help/warn/ban \naccording to community guidelines of the official Team Liquid Discord. \
        \n\nTo refer the community guidelines, you can join the {b}{a=https://discord.gg/TeamLiquid}TL Discord{/a}{/b} or read {b}{a=https://i.gyazo.com/4ad5b45f736e4cb65ce03540628fe0ba.png}here{/a}{/b}.':
             color '#fff'



init python:
    import pygame

    class ModerationDisplayable(renpy.Displayable):

        def __init__(self):
            super(ModerationDisplayable, self).__init__()

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            return render
