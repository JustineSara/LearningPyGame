import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('nothign here')

while True: # the main game loop
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
