import asyncio
from itertools import cycle

from animation.curses_tools import draw_frame, read_controls, get_frame_size


async def animate_spaceship(canvas, frame1, frame2):
    spaceship_frames = cycle([frame1, frame2])

    max_row, max_col = canvas.getmaxyx()
    frame_max_row, frame_max_col = get_frame_size(frame1)
    row = max_row // 2
    col = max_col // 2 - frame_max_col // 2
    border = 0

    while True:
        spaceship_frame = next(spaceship_frames)
        rows_direction, columns_direction, space_pressed = read_controls(canvas)
        new_row = row + rows_direction
        new_col = col + columns_direction

        if border < new_col < (max_col - frame_max_col - border):
            col = new_col
        if border < new_row < (max_row - frame_max_row - border):
            row = new_row

        draw_frame(canvas, row, col, spaceship_frame)
        for _ in range(3):
            await asyncio.sleep(0)
        draw_frame(canvas, row, col, spaceship_frame, negative=True)
