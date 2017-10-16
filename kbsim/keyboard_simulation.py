import os, sys, inspect, platform, json, time

code_type = "Undefined"
system = platform.system()
if system == "Windows":
    import keyboard_simulation_win as key
    code_type = "vk_code"
elif system == "Linux":
    import keyboard_simulation_linux as key
    code_type = "key_sym"

file_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
file_name = 'key_mapping.json'

if len(file_dir) == 0:
    file_dir = file_name
else:
    file_dir = file_dir + '/' + file_name
with open(file_dir, 'r') as file:
    code = json.load(file)

def PressKey(key_str):
    key.PressKey(code[key_str][code_type])

def ReleaseKey(key_str):
    key.ReleaseKey(code[key_str][code_type])

def TypeKey(key_str):
    key_str = key_str.lower().split('+')
    for key_press in key_str:
        key.PressKey(code[key_press][code_type])
    for key_release in key_str:
        key.ReleaseKey(code[key_release][code_type])

def test():
    if system == "Windows":
        # win + r
        PressKey("win")
        PressKey("r")
        ReleaseKey("r")
        ReleaseKey("win")
        time.sleep(2)
        # c + m + d
        TypeKey("c")
        TypeKey("m")
        TypeKey("d")
        # ENTER
        TypeKey("enter")
    elif system == "Linux":
        # ctrl + alt + t
        PressKey("ctrl")
        PressKey("alt")
        PressKey("t")
        ReleaseKey("t")
        ReleaseKey("alt")
        ReleaseKey("ctrl")
        TypeKey("ctrl+alt+t")
