import curses
from curses import wrapper

# Convenience functions
# Middle of the screen function calculator
# Initializing the colors we want to be able to output


def rowPos(stdscr, step):
    width = stdscr.getmaxyx()
    rPos = width[1] // step
    return rPos
    
        



# Start menu
def start_screen(stdscr):
    
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # (id for the pair, foreground color, background color)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    
    # Evaluates the center of of the console so you can use it as an argument.
    rPos = rowPos(stdscr, step=2)
    
    dialogue = { 'welcomeTxt' : "Welcome to the Speed Typing Test", 'toStart' : "Press any key to Begin"}


    stdscr.clear() # Ensures blank slate 
    stdscr.addstr(0, rPos - len(dialogue['welcomeTxt']) // 2, dialogue['welcomeTxt'],  curses.color_pair(4)) # (row [up|down], col [left|right], string output, color)
    stdscr.addstr("\n" + dialogue['toStart'])
    stdscr.refresh()
    stdscr.getkey()

# our main
def main(stdscr):
    
    start_screen(stdscr)

wrapper(main)