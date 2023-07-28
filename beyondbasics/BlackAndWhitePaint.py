import pygame, sys
from pygame.locals import *


## Define globals ##

# window size in pixels
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
# set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)


def main():
# main : main function with the game loop

    pygame.init()
    displaysurf = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption('Have fun painting!')
    # this is the name of the window, typically the name of the game

    # initiate values
    background_color = WHITE
    drawing_color = BLACK
    paint_pos = []

    # this is the game loop
    while True :

        # consider all events
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    background_color, drawing_color = switch_elements(background_color, drawing_color)        


        # update the view of the game
        
        displaysurf.fill(background_color)
        for p in paint_pos :
            pygame.draw.circle(displaysurf, drawing_color, p, 1, 0)

        pygame.display.update()


def switch_elements(c1,c2):
    return (c2,c1)

if __name__ == '__main__':
    main()