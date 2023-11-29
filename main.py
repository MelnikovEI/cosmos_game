import random
import time
import curses

from animation.fire_animation import fire
from animation.spaceship_animation import animate_spaceship
from animation.stars_animation import blink

TIC_TIMEOUT = 0.1
STARS_QUANTITY = 50
BORDER_WIDTH = 1


def draw(canvas):
    canvas.border()
    curses.curs_set(False)
    canvas.nodelay(True)
    with open('animation/rocket_frame_1.txt', 'r') as r1:
        frame1 = r1.read()
    with open('animation/rocket_frame_2.txt', 'r') as r2:
        frame2 = r2.read()

    window_height, window_width = canvas.getmaxyx()
    coroutines = [
        blink(
            canvas,
            random.randint(BORDER_WIDTH, window_height - BORDER_WIDTH - 1),
            random.randint(BORDER_WIDTH, window_width - BORDER_WIDTH - 1),
            random.randint(1, 10),
            random.choice('+*.:')
        )
        for _ in range(STARS_QUANTITY)
    ]

    coroutines.append(fire(canvas, window_height//2, window_width//2))
    coroutines.append(animate_spaceship(canvas, frame1, frame2, 0))
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
