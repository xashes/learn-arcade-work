#!/usr/bin/env python3

import random
import arcade as ac

sprite_scaling_player = 0.5
sprite_scaling_coin = 0.2
coin_count = 50

screen_width = 800
screen_height = 600


class MyGame(ac.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, "Sprite Example")

        self.players = None
        self.coins = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        ac.set_background_color(ac.color.AMAZON)

    def setup(self):
        self.players = ac.SpriteList()
        self.coins = ac.SpriteList()

        self.score = 0

        self.player_sprite = ac.Sprite("./character.png", sprite_scaling_player)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.players.append(self.player_sprite)

        for i in range(coin_count):
            coin = Coin("coin_01.png", sprite_scaling_coin)
            coin.center_x = random.randrange(screen_width)
            coin.center_y = random.randrange(screen_height)
            self.coins.append(coin)

    def on_draw(self):
        ac.start_render()

        self.coins.draw()
        self.players.draw()

        score = f"Score: {self.score}"
        ac.draw_text(score, 10, 20, ac.color.WHITE, 14)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time: float):
        self.coins.update()

        coins_hit = ac.check_for_collision_with_list(self.player_sprite, self.coins)

        for coin in coins_hit:
            coin.remove_from_sprite_lists()
            self.score += 1


class Coin(ac.Sprite):
    def update(self):
        self.center_y -= 1

        if self.center_y < -20:
            self.center_y = random.randrange(screen_height + 20, screen_height + 100)
            self.center_x = random.randrange(0, screen_width)


def main():
    window = MyGame()
    window.setup()
    ac.run()


if __name__ == "__main__":
    main()
