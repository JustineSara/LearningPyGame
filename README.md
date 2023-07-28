# LearningPyGame
Learning PyGame

## Basics

The goal of this folder is to code the basics bricks that will allow one to buld a game.

### [empty game window](./basics/emptygamewindow.py)
here we generate an empty game window and an empty game loop.


Learn to : 
1. import pygame
2. create a game window
3. make an infinte loop (game loop)
4. exit the game loop and close the game


### [print event](./basics/printevents.py)
This piece of code prints the event detected by pygame

Can see different types of events :
* mouse entering the window : `<Event(32768-ActiveEvent {'gain': 1, 'state': 0})>` and `<Event(32783-WindowEnter {'window': None})>`
* mouse leaving the window : `<Event(32768-ActiveEvent {'gain': 0, 'state': 0})>` and `<Event(32784-WindowLeave {'window': None})>`
* mouse mooving : `<Event(1024-MouseMotion {'pos': (35, 285), 'rel': (1, -1), 'buttons': (0, 0, 0), 'touch': False, 'window': None})>`
    * `pos` would be the position of the mouse in the window
    * `rel` seems to be the relative position to the previous position detected
    * `buttons` are if a button is pressed down (left, middle, center)
    * `touch` : no idea (have to check the doc of pygame)
    * `window` : probably if more than one window is created it gives the index or name of the window (need to check that)
* a key is pushed down : `<Event(768-KeyDown {'unicode': '', 'key': 1073741903, 'mod': 4096, 'scancode': 79, 'window': None})>`
    * if it's a letter the `unicode` is not empty : `<Event(769-KeyUp {'unicode': 'j', 'key': 106, 'mod': 4096, 'scancode': 13, 'window': None})>`
* a key is let up : `<Event(769-KeyUp {'unicode': '', 'key': 1073741903, 'mod': 4096, 'scancode': 79, 'window': None})>`
* `TextInput` seems to be an event to help with typing as it happens when a text key is used and appears again if the key is kept down (an arrow key does not generate such events for example) : `<Event(771-TextInput {'text': 'j', 'window': None})>`

### [draw](./basics/drawing.py)
Here we learn to draw simple shapes on the game window

To practice and have fun, I added a cat's head (maybe)


## beyond basics

In this folder, I learn to do simple things using the basics. The goal is to use only two or three to do something simple but fun

### [Black and White Paint](./beyondbasics/BlackAndWhitePaint.py)

This game is to paint things in white or black.
We first implemented a small feature to exchange the black and white color
Then we detect the MouseMove events and check if the left mouse button is down, we add that to a list of points we will then draw

Potential addition :
* more colors
* change the size with the wheel of the mouse
    * small addition if ok to change all the points' size at once
    * more work if change only the new points (different structure of the picture saved needed)
* add a timer that erase/forget the points drawn (need to handle time --> new 'game'?)

Remark :
* if we were not switching colors, we could probably draw the points directly on the surface and not have to save it. Might also be faster to not redraw the whole picture everytime!