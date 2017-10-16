# Keyboard & Mouse Simulation

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/peitaosu/Keyboard-Mouse-Simulation/master/LICENSE)

This module wrapper keyboard and mouse events and send to system to have same behavior with physical keyboard and mouse.

You can use it in your automation scripts, or as easy-to-use API when you want to send keyboard and mouse events to different desktop environment (Windows & X11) in same way.

## Setup

`Xlib` and `virtkey` are the libraries used to send `mouse_event` and `keyboard_event` on Linux with X11. So you need to install `python-xlib` and `python-virtkey` following the command below here, before use the scripts:

```
sudo apt-get install python-xlib python-virtkey
```

## Use

Import the package file into your script, call the functions.

```
# Example

import kbsim.keyboard_simulation as kb_sim
import mssim.keyboard_simulation as ms_sim

def run():
    kb_sim.TypeKey("a")
    # use shortcut, only TypeKey() supported
    kb_sim.TypeKey("ctrl+alt+t")
    ms_sim.Click(200, 200, 1)
```
