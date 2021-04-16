#!/usr/bin/env python3

import arcade as ac

box_scale = 0.5
player_scale = 0.5

width = 800
height = 600
viewport_margin = 200

speed = 5


class MyGame(ac.Window):
    def __init__(self):
        super().__init__(width, height, "Wall Example")

        self.wall_pic = "./boxCrate_double.png"
        self.view_left = 0
        self.view_bottom = 0

    def setup(self):
        ac.set_background_color(ac.color.AMAZON)

        self.players = ac.SpriteList()
        self.walls = ac.SpriteList()

        self.score = 0

        self.player = ac.Sprite("character.png", player_scale)
        self.player.center_x = 50
        self.player.center_y = 50
        self.players.append(self.player)

        for x in range(173, 650, 64):
            self.place_box(x, 350)

        self.physics_engine = ac.PhysicsEngineSimple(self.player, self.walls)

    def on_draw(self):
        ac.start_render()
        self.walls.draw()
        self.players.draw()

    def update(self, delta_time: float):
        self.physics_engine.update()

        # manage scrolling
        changed = False

        left_boundary = self.view_left + viewport_margin
        if self.player.left < left_boundary:
            self.view_left = self.player.left - viewport_margin
            changed = True
        right_boundary = self.view_left + width - viewport_margin
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary
            changed = True

        self.view_left = int(self.view_left)
        if changed:
            ac.set_viewport(
                self.view_left,
                self.view_left + width - 1,
                self.view_bottom,
                self.view_bottom + height - 1,
            )

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == ac.key.UP:
            self.player.change_y = speed
        elif symbol == ac.key.DOWN:
            self.player.change_y = -speed
        elif symbol == ac.key.LEFT:
            self.player.change_x = -speed
        elif symbol == ac.key.RIGHT:
            self.player.change_x = speed

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == ac.key.UP or symbol == ac.key.DOWN:
            self.player.change_y = 0
        elif symbol == ac.key.LEFT or symbol == ac.key.RIGHT:
            self.player.change_x = 0

    def place_box(self, x, y):
        wall = ac.Sprite(self.wall_pic, box_scale)
        wall.center_x = x
        wall.center_y = y
        self.walls.append(wall)


def main():
    window = MyGame()
    window.setup()
    ac.run()


if __name__ == "__main__":
    main()
