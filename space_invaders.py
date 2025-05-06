from pygame import *

screen = display.set_mode((800,600))

RED = (255, 0, 0)    # ALL CAPS is used for constants
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    # ----------------------------------


    # ----------------------------------
    display.flip()

quit()