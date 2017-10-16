import platform

os = platform.system()
if os == "Windows":
    import mouse_simulation_win as mouse
elif os == "Linux":
    import mouse_simulation_linux as mouse

def Move(x, y):
    mouse.Move(x, y)

def Press(x, y, button):
    mouse.Press(x, y, button)

def Release(x, y, button):
    mouse.Release(x, y, button)

def Click(x, y, button):
    mouse.Click(x, y, button)

def DClick(x, y, button):
    mouse.DClick(x, y, button)

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