#!/usr/bin/env python3

import arcade as ac
import numpy as np

grid_width = 20
grid_height = 20
grid_margin = 5
row_count = 10
column_count = 10
width = grid_width * column_count + grid_margin * (column_count + 1)
height = grid_height * row_count + grid_margin * (row_count + 1)


class MyGame(ac.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Grid")

        self.grid = np.zeros((row_count, column_count), dtype=int)
        self.grid[1, 5] = 1

    def setup(self):
        ac.set_background_color(ac.color.BLACK)

    def on_draw(self):
        ac.start_render()

        for column in range(column_count):
            for row in range(row_count):
                x = column * grid_width + grid_margin * (column + 1)
                y = row * grid_height + grid_margin * (row + 1)
                color = ac.color.WHITE
                if self.grid[row, column] == 1:
                    color = ac.color.GREEN
                self.draw_box(x, y, color)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        column = x // (grid_width + grid_margin)
        row = y // (grid_height + grid_margin)
        print(f"Coordinates: ({x}, {y}), grid: ({row}, {column})")
        if row < row_count and column < column_count:
            self.grid[row, column] = 1

    def draw_box(self, x, y, color=ac.color.WHITE):
        center_x = x + grid_width / 2
        center_y = y + grid_height / 2
        ac.draw_rectangle_filled(center_x, center_y, grid_width, grid_height, color)


def main():
    window = MyGame(width, height)
    window.setup()
    ac.run()


if __name__ == "__main__":
    main()
