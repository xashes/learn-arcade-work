#!/usr/bin/env python3
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Grid Using Sprites"
row_count = 9
column_count = 9
grid_width = SCREEN_WIDTH / column_count
grid_height = SCREEN_HEIGHT / row_count


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.grid_sprite_list = None
        self.grid_sprites = None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        self.grid_sprite_list = arcade.SpriteList()
        self.grid_sprites = []

        for row in range(row_count):
            self.grid_sprites.append([])
            for column in range(column_count):
                x = grid_width * column + grid_width / 2
                y = grid_height * row + grid_height / 2
                color = arcade.color.WHITE
                sprite = arcade.SpriteSolidColor(
                    int(grid_width), int(grid_height), color
                )
                sprite.position = (x, y)
                self.grid_sprites[row].append(sprite)
                self.grid_sprite_list.append(sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.grid_sprite_list.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        row = int(y // grid_height)
        column = int(x // grid_width)

        if row < row_count and column < column_count:
            self.grid_sprites[row][column].color = arcade.color.GREEN

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
