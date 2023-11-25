import asyncio

from animation.curses_tools import draw_frame


async def animate_spaceship(canvas, start_row, start_column, frame1, frame2):
    while True:
        draw_frame(canvas, start_row, start_column, frame1, negative=False)
        for _ in range(3):
            await asyncio.sleep(0)
        draw_frame(canvas, start_row, start_column, frame1, negative=True)
        draw_frame(canvas, start_row, start_column, frame2, negative=False)
        for _ in range(3):
            await asyncio.sleep(0)
        draw_frame(canvas, start_row, start_column, frame2, negative=True)
