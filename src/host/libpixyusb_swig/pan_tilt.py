from pixy import *
from ctypes import *

import curses
import sys
import time


def setPosition(ch, pos):

    # Write position until you get same readback
    for i in range(0, 10):
        pixy_rcs_set_position(ch, pos)
        readback = pixy_rcs_get_position(ch)

        if readback == pos:
            if ch == 0:
                print("\rx: {}".format(readback))
            else:
                print("\ry: {}".format(readback))
            return readback

    raise Exception("setPosition: timeout reached.")


if __name__ == "__main__":

    # Initialize Pixy Interpreter thread #
    pixy_init()

    # pixy starting position
    start_pos = 500
    pixy_rcs_set_position(0, start_pos)
    pixy_rcs_set_position(1, start_pos)
    val = pixy_rcs_get_position(1)
    print(val)

    button_delay = 0.5

    # init screen
    screen = curses.initscr()
    curses.cbreak()
    screen.keypad(1)
    key = ''

    try:
        while key != ord('q'):  # press <Q> to exit the program

            time.sleep(button_delay)

            key = screen.getch()  # get the key
            screen.refresh()

            # the same, but for <Up> and <Down> keys:
            if key == curses.KEY_UP:
                setPosition(1, start_pos - 50)
            elif key == curses.KEY_DOWN:
                setPosition(1, start_pos + 50)
            elif key == curses.KEY_LEFT:
                setPosition(0, start_pos - 50)
            elif key == curses.KEY_RIGHT:
                setPosition(0, start_pos + 50)
            else:
                print("\rMove with arrows. Press q to quit.")

    # catch ctrl+c
    except KeyboardInterrupt:
        print("bye")
        curses.endwin()
        sys.exit()

    curses.endwin()
