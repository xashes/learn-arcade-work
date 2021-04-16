#!/usr/bin/env python3

import arcade as ac

ac.open_window(600, 600, "Drawing Example")

ac.set_background_color(ac.csscolor.SKY_BLUE)

ac.start_render()

ac.draw_lrtb_rectangle_filled(0, 599, 300, 0, ac.csscolor.GREEN)
ac.draw_rectangle_filled(100, 320, 20, 60, ac.csscolor.SIENNA)
ac.draw_circle_filled(100, 350, 30, ac.csscolor.DARK_GREEN)

ac.finish_render()

ac.run()
