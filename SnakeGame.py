import curses
import random

scr = curses.initscr()
curses.curs_set(0)
sh, sw = scr.getmaxyx()
win = curses.newwin(sh, sw, 0, 0)
win.keypad(1)
win.timeout(100)

snake_x = sw / 4
snake_y = sh / 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

food = [sh/2, sw/2]
win.addch(int(food[0]), int(food[1]), 'O')

key = curses.KEY_RIGHT

while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None

        win.addch(int(food[0]), int(food[1]), 'O')
    else:
        tail = snake.pop()
        win.addch(int(tail[0]), int(tail[1]), ' ')

    win.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)