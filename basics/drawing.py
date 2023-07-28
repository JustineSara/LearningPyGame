import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500,400), 0, 32)
# size and ??? 

pygame.display.set_caption('Drawing!')

# set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE)
# everything is white

pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
# draw a green polygon , 5 points (defined by their pixel) are the corners

pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
# draw a line to DISPLAYSURF in BLUE from point A to B, 4 pixels wide (or 1)
# lines (plural) : drwa a line between each points listed

pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
# circle : center and radius and width (width = 0 => fill it)

pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)

pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

# Unfortunately, there isn’t a single function you can call that will set a single pixel to a color
# Creating a PixelArray object of a Surface object will "lock" the Surface object.
# can have individual pixels set by accessing them with two indexes
# To tell Pygame that you are finished drawing individual pixels, delete the PixelArray object with a del statement. This is will "unlock" the Surface object 
pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj
# Apparently that is wrong and there exists a function to change the color of pixels


pygame.draw.circle(DISPLAYSURF, BLACK, (250,200), 100, 0)
pygame.draw.polygon(DISPLAYSURF, WHITE, ((230,200),(270,200),(250,230)))
pygame.draw.ellipse(DISPLAYSURF, BLUE, (220,150,10,30))
pygame.draw.ellipse(DISPLAYSURF, BLUE, (280,150,10,30))
pygame.draw.aaline(DISPLAYSURF, WHITE, (250,210), (320,210))
pygame.draw.aaline(DISPLAYSURF, WHITE, (250,210), (180,210))
pygame.draw.aaline(DISPLAYSURF, WHITE, (250,210), (300,240))
pygame.draw.aaline(DISPLAYSURF, WHITE, (250,210), (300,180))
pygame.draw.aaline(DISPLAYSURF, WHITE, (250,210), (200,240))
pygame.draw.aaline(DISPLAYSURF, WHITE, (250,210), (200,180))
pygame.draw.polygon(DISPLAYSURF, BLACK, ((150,100), (180,130), (230,140), (230, 110)) )
pygame.draw.polygon(DISPLAYSURF, BLACK, ((350,100), (320,130), (230,140), (270, 110)) )



pygame.draw.rect(DISPLAYSURF, RED, (250, 0, 100, 50))

while True :
    for event in pygame.event.get() :

        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    pygame.display.update()

