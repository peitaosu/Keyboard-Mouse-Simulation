from Xlib import X
from Xlib.display import Display
from Xlib.ext.xtest import fake_input

display = Display()

def Move(x, y):
    fake_input(display, X.MotionNotify, x, y)

def Press(x, y, button=1):
    Move(x, y)
    '''
    Redefined right button flag 3 to 2
    '''
    if button == 2:
        button = 3
    fake_input(display, X.ButtonPress, button)

def Release(x, y, button=1):
    Move(x, y)
    '''
    Redefined right button flag 3 to 2
    '''
    if button == 2:
        button = 3
    fake_input(display, X.ButtonRelease, button)

def Click(x, y, button=1):
    Move(x, y)
    '''
    Redefined right button flag 3 to 2
    '''
    if button == 2:
        button = 3
    fake_input(display, X.ButtonPress, button)
    fake_input(display, X.ButtonRelease, button)

def DClick(x, y, button=1):
    Move(x, y)
    '''
    Redefined right button flag 3 to 2
    '''
    if button == 2:
        button = 3
    fake_input(display, X.ButtonPress, button)
    fake_input(display, X.ButtonRelease, button)

def test():
    # move mouse
    Move(100, 100)
    # mouse left press
    Press(150, 150, 1)
    # mouse right press
    Press(150, 150, 2)
    # mouse left release
    Release(150, 150, 1)
    # mouse right release
    Release(150, 150, 2)
    # mouse left click
    Click(200, 200, 1)
    # mouse right click
    Click(200, 200, 2)
    # mouse left double click
    DClick(100, 250, 1)
    # mouse right double click
    DClick(200, 250, 2)
