import curses
from curses import wrapper

# Convenience functions
# Middle of the screen function calculator
def rowPos(stdscr, step):
    width = stdscr.getmaxyx()
    rPos = width[1] // step
    return rPos
    

# Start menu
def start_screen(stdscr):
    
    # Evaluates the center of of the console so you can use it as an argument.
    rPos = rowPos(stdscr, step=2)
    
    dialogue = { 'welcomeTxt' : "Welcome to the Speed Typing Test", 'toStart' : "Press any key to Begin"}


    stdscr.clear # Ensures blank slate
    
    stdscr.addstr(0, rPos - len(dialogue['welcomeTxt']) // 2, dialogue['welcomeTxt']) # (row [up|down], col [left|right], string output, color)
    stdscr.addstr("\n" + dialogue['toStart'])
    stdscr.refresh()
    stdscr.getkey()


# our main
def main(stdscr):
    
    # Initializing the colors we want to be able to output
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # (id for the pair, foreground color, background color)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    
    
    stdscr.clear()
    
    # Adds stuff to our screen
    stdscr.addstr("Whoah look at this crazy ass color I can out put to the screen", curses.color_pair(1)) #(outputs text, references the color we want to use for the output)
    
    stdscr.addstr(1, 8, "Welcome", curses.color_pair(4)) # (what row [so up or down], How many spaces [left or right], string output, color choice)

    stdscr.refresh()
    stdscr.getkey() # You can store this in a variable

wrapper(start_screen)