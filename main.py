import random
import time
import curses

from animation.fire_animation import fire
from animation.spaceship_animation import animate_spaceship
from animation.stars_animation import blink

TIC_TIMEOUT = 0.1
STARS_QUANTITY = 20


def draw(canvas):
    canvas.border()
    curses.curs_set(False)
    canvas.nodelay(True)
    with open('animation/rocket_frame_1.txt', 'r') as r1:
        frame1 = r1.read()
    with open('animation/rocket_frame_2.txt', 'r') as r2:
        frame2 = r2.read()

    y_max, x_max = canvas.getmaxyx()
    coroutines = [
        blink(canvas, random.randint(1, y_max - 2), random.randint(1, x_max - 2), random.choice('+*.:'))
        for _ in range(STARS_QUANTITY)
    ]

    coroutines.append(fire(canvas, y_max//2, x_max//2))
    coroutines.append(animate_spaceship(canvas, frame1, frame2))
    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
        if len(coroutines) == 0:
            break
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
