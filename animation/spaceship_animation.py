import asyncio
import curses
from itertools import cycle

from animation.curses_tools import draw_frame, read_controls, get_frame_size


async def animate_spaceship(canvas, frame1, frame2):
    spaceship_frames = cycle([frame1, frame2])

    y_max, x_max = curses.window.getmaxyx(canvas)
    frame_max_row, frame_max_col = get_frame_size(frame1)
    row = y_max // 2
    col = x_max // 2 - frame_max_col // 2

    while True:
        spaceship_frame = next(spaceship_frames)
        rows_direction, columns_direction, space_pressed = read_controls(canvas)
        row += rows_direction
        col += columns_direction
        draw_frame(canvas, row, col, spaceship_frame)
        for _ in range(3):
            await asyncio.sleep(0)
        draw_frame(canvas, row, col, spaceship_frame, negative=True)


    # while True:
    #     draw_frame(canvas, row, col, frame1, negative=False)
    #     for _ in range(3):
    #         await asyncio.sleep(0)
    #     draw_frame(canvas, row, col, frame1, negative=True)
    #     draw_frame(canvas, row, col, frame2, negative=False)
    #     for _ in range(3):
    #         await asyncio.sleep(0)
    #     draw_frame(canvas, row, col, frame2, negative=True)

