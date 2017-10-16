import virtkey, os, inspect, json, time

def PressKey(keysym):
    vk = virtkey.virtkey()
    vk.press_keysym(keysym)


def ReleaseKey(keysym):
    vk = virtkey.virtkey()
    vk.release_keysym(keysym)

def TypeKey(keysym):
    vk = virtkey.virtkey()
    vk.press_keysym(keysym)
    vk.release_keysym(keysym)

def test():
    # get keysyms code from json file ./keysyms.json
    # keysyms code is from https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
    file_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    file_name = 'keysyms.json'

    if len(file_dir) == 0:
        file_dir = file_name
    else:
        file_dir = file_dir + '/' + file_name
    with open(file_dir, 'r') as file:
        code = json.load(file)

    # ctrl + alt + t
    PressKey(code["Control_L"])
    PressKey(code["Alt_L"])
    PressKey(code["t"])
    ReleaseKey(code["t"])
    ReleaseKey(code["Alt_L"])
    ReleaseKey(code["Control_L"])

    time.sleep(2)
    # l + s + enter
    TypeKey(code["l"])
    TypeKey(code["s"])
    TypeKey(code["KP_Enter"])


