import pygame, sys
from pygame.locals import *


## Define globals ##

# window size in pixels
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300


def main():
# main : main function with the game loop

    pygame.init()
    displaysurf = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption('Hello World!')
    # this is the name of the window, typically the name of the game

    # this is the game loop
    while True :

        # consider all events
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        
        # update the view of the game
        pygame.display.update()




if __name__ == '__main__':
    main()