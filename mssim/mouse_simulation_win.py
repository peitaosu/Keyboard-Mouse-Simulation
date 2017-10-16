import ctypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

def Move(x, y):
    user32.SetCursorPos(x, y)

def Press(x, y, button=1):
    Move(x, y)
    button_action = 2 ** ((2 * button) - 1)
    user32.mouse_event(button_action, x, y)

def Release(x, y, button=1):
    Move(x, y)
    button_action = 2 ** (2 * button)
    user32.mouse_event(button_action, x, y)

def Click(x, y, button=1):
    Move(x, y)
    button_action = 2 ** ((2 * button) - 1)
    user32.mouse_event(button_action, x, y)
    button_action = 2 ** (2 * button)
    user32.mouse_event(button_action, x, y)

def DClick(x, y, button=1):
    Move(x, y)
    button_action = 2 ** ((2 * button) - 1)
    user32.mouse_event(button_action, x, y)
    button_action = 2 ** (2 * button)
    user32.mouse_event(button_action, x, y)
    button_action = 2 ** ((2 * button) - 1)
    user32.mouse_event(button_action, x, y)
    button_action = 2 ** (2 * button)
    user32.mouse_event(button_action, x, y)

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
