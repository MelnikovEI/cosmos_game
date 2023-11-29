import asyncio
from itertools import cycle

from animation.curses_tools import draw_frame, read_controls, get_frame_size


async def animate_spaceship(canvas, frame1, frame2):
    spaceship_frames = cycle([frame1, frame1, frame2, frame2])

    window_height, window_width = canvas.getmaxyx()
    # https://docs.python.org/2/library/curses.html#curses.window.getmaxyx
    frame_max_row, frame_max_col = get_frame_size(frame1)
    row = window_height // 2
    col = window_width // 2 - frame_max_col // 2
    border = 0

    for spaceship_frame in spaceship_frames:
        rows_direction, columns_direction, space_pressed = read_controls(canvas)
        new_row = row + rows_direction
        new_col = col + columns_direction

        if border < new_col < (window_width - frame_max_col - border):
            col = new_col
        if border < new_row < (window_height - frame_max_row - border):
            row = new_row

        draw_frame(canvas, row, col, spaceship_frame)
        await asyncio.sleep(0)
        draw_frame(canvas, row, col, spaceship_frame, negative=True)
