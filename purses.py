import curses
import time

curses.initscr()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-11
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
