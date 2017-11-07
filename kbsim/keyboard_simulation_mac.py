import Quartz


def PressKey(keycode):
    event = Quartz.CGEventCreateKeyboardEvent(None, keycode, 1)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)

def ReleaseKey(keycode):
    event = Quartz.CGEventCreateKeyboardEvent(None, keycode, 0)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)

def TypeKey(keycode):
    PressKey(keycode)
    ReleaseKey(keycode)
