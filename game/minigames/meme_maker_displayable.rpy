# PATHS
define THIS_PATH = 'minigames/'
define IMG_DIR = 'images/'
define MEM_IMG_NAME = "meme maker "

define RIGHT_ARROW = THIS_PATH + IMG_DIR + "arrow right.png"
define LEFT_ARROW = THIS_PATH + IMG_DIR + "arrow left.png"


define variable = ""
# IMAGES




# MINIGAME
screen meme_maker_minigame_displayable():
    default meme_maker_displayable = MemeMakerDisplayable()

    add Solid('#000')
    add meme_maker_displayable
    layer "master"

    vbox:
        xpos 50 ypos 20 spacing 100
        text '⚒️ {b}Meme Creation Challenge{/b}':
             color '#fff'

    vbox:
        xpos 50 ypos 50 spacing 100
        text 'Activity: Create a meme for our social media presense, press the side arrows to select an image, type out your caption when ready!':
             color '#fff'

    viewport:
        ypos 550
        xpos 400
        xysize 400, 200
        input color "#000" xmaximum 700 ymaximum 300  length 400 text_align 0.5




init python:
    import pygame

    class MemeMakerDisplayable(renpy.Displayable):
        def __init__(self):
            super(MemeMakerDisplayable, self).__init__()

            self.hasFinished = False;
            self.curimage = 0
            x,y = renpy.get_physical_size()
        
            self.images = []
            self.imagesize = []
            for x in range(0,7):
                self.images.append(Image(THIS_PATH + IMG_DIR + MEM_IMG_NAME + str(x+1) + '.png', xcenter=600, ycenter=400,))
                Transform(self.images[x], 0.5)
        

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            x,y = renpy.get_physical_size()


            img_to_render = self.images[self.curimage]
            render.place(img_to_render)

            render.place(Image(RIGHT_ARROW),x=1100,y=200)
            render.place(Image(LEFT_ARROW),x=0,y=200)

            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.pos[0] < 1750 and ev.pos[0] > 1600 and ev.pos[1] > 300 and ev.pos[1] < 400 :
                if (self.curimage >= 6):
                    self.curimage = 0
                else:
                    self.curimage = self.curimage + 1
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.pos[0] < 200 and ev.pos[0] > 50 and ev.pos[1] > 300 and ev.pos[1] < 400 :
                if (self.curimage <= 0):
                    self.curimage = 6
                else:
                    self.curimage = self.curimage - 1
            