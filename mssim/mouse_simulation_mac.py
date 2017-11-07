import Quartz

press_id = [None, Quartz.kCGEventLeftMouseDown, Quartz.kCGEventRightMouseDown, Quartz.kCGEventOtherMouseDown]
release_id = [None, Quartz.kCGEventLeftMouseUp, Quartz.kCGEventRightMouseUp, Quartz.kCGEventOtherMouseUp]

def Move(x, y):
    move = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventMouseMoved, (x, y), 0)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, move)

def Press(x, y, button=1):
    event = Quartz.CGEventCreateMouseEvent(None, press_id[button], (x, y), button - 1)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)

def Release(x, y, button=1):
    event = Quartz.CGEventCreateMouseEvent(None, release_id[button], (x, y), button - 1)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)

def Click(x, y, button=1):
    Press(x, y, button)
    Release(x, y, button)

def DClick(x, y, button=1):
    Click(x, y, button)
    Click(x, y, button)
