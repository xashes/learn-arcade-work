"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

character_scaling = 1
tile_scaling = 0.5
coin_scaling = 0.5
PLAYER_MOVEMENT_SPEED = 5
gravity = 1
jump_speed = 20


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)

        self.player_sprite = arcade.Sprite(
            "images/player_1/player_stand.png", character_scaling
        )
        self.player_sprite.left = 64
        self.player_sprite.bottom = 64

        self.player_list.append(self.player_sprite)

        # create the ground
        positions = ((x, 32) for x in range(0, self.width + 200, 64))
        for posn in positions:
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", tile_scaling)
            wall.position = posn
            self.wall_list.append(wall)

        coordinate_list = ((x, 96) for x in (256, 512, 768))
        for coor in coordinate_list:
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", tile_scaling
            )
            wall.position = coor
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.wall_list, gravity
        )

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = jump_speed
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # Code to draw the screen goes here
        self.player_list.draw()
        self.wall_list.draw()
        self.coin_list.draw()

    def on_update(self, delta_time: float):
        self.physics_engine.update()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
