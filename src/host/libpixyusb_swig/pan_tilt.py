from pixy import *
from ctypes import *

import sys
import termios
import tty
import os
import time

# https://www.jonwitts.co.uk/archives/896, Jon Witts addapted from
# https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def setPosition(ch, pos):

    pixy_rcs_set_position(ch, pos)
    val = pixy_rcs_get_position(ch)

    if ch == 0:
        print("x: {}".format(val))
    else:
        print("y: {}".format(val))

# Pixy Python SWIG get blocks example #


print("Pixy Python SWIG Example -- Pan Tilt")

# Initialize Pixy Interpreter thread #
pixy_init()

start_pos_x = 500

pixy_rcs_set_position(0, start_pos_x)
pixy_rcs_set_position(1, start_pos_x)
val = pixy_rcs_get_position(1)
print(val)

button_delay = 0.2

print("Use w, a, s, d keys to move.")
print("Press q to quit.")
while True:
    char = getch()
    time.sleep(0.1)

    if (char == "q"):
        print("Stop!")
        exit(0)

    if (char == "a"):
        setPosition(0, start_pos_x - 50)
        time.sleep(button_delay)

    elif (char == "d"):
        setPosition(0, start_pos_x + 50)
        time.sleep(button_delay)

    elif (char == "w"):
        setPosition(1, start_pos_x - 50)
        time.sleep(button_delay)

    elif (char == "s"):
        setPosition(1, start_pos_x + 50)
        time.sleep(button_delay)

    elif (char == "1"):
        print("Number 1 pressed")
        time.sleep(button_delay)
