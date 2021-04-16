#!/usr/bin/env python3

import arcade as ac


class MyGame(ac.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        ac.set_background_color(ac.color.ASH_GREY)

        self.stones: list[Ball] = []

    def on_draw(self):
        ac.start_render()

        for s in self.stones:
            s.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == ac.MOUSE_BUTTON_LEFT:
            self.stones.append(Ball(x, y))

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == ac.key.LEFT:
            self.stones = self.stones[:-1]


class Ball:
    def __init__(self, x, y, r=15, color=ac.color.AUBURN) -> None:
        self.x = x
        self.y = y
        self.radius = r
        self.color = color

    def draw(self):
        ac.draw_circle_filled(self.x, self.y, self.radius, self.color)


def main():
    window = MyGame(600, 400, "Example")
    ac.run()


if __name__ == "__main__":
    main()
