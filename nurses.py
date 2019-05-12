import curses
import time

curses.initscr()

def percentage():
    loading = 0
    while loading < 100:
        loading += 1
        time.sleep(0.01)
        update_progress(loading)


def update_progress(progress):
    win = curses.newwin(3, 32, 3, 30)
    win.border(0)
    rangex = (30 / float(100)) * progress
    pos = int(rangex)
    display = '#'
    if pos != 0:
        win.addstr(1, 1, "{}".format(display*pos))
        win.refresh()

percentage()