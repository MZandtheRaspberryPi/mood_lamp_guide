import unicornhat as unicorn
import time
import numpy as np
import random
from auto_lamp import pulse, getClockTime

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)

unicorn.brightness(0.5)
width,height=unicorn.get_shape()
unicorn.clear()
unicorn.show()

DARK_BLUE = [2, 55, 171]
DEEP_GREEN =  [52, 235, 134]
PURE_WHITE = [255, 255, 255]
BLUE_GREEN = [7, 173, 157]
"""
for i in range(width):
    for j in range(height):
        if i % 2 == 0:
            color = DARK_BLUE
        else:
            color = DEEP_GREEN
        unicorn.set_pixel(i, j, color[0], color[1], color[2])
"""

# start with 5, 0
# 5, 1, .2, DEEP_GREEN
# 4, 2, .3
# 3, 1, .4

green_path = [
              [[5, 1, .3, DEEP_GREEN]],
              [[4, 2, .4, DEEP_GREEN]],
              [[3, 1, .5, DEEP_GREEN]],
              [[2, 1, .5, DEEP_GREEN]],
              [[1, 1, .4, DEEP_GREEN]],
              [[1, 2, .3, DEEP_GREEN]], #[0, 3, .25, DARK_BLUE]],
              [[1, 3, .25, DEEP_GREEN], [0, 2, .25, DARK_BLUE]],
              [[1, 2, .25, DARK_BLUE]],
              [[1, 1, .3, DARK_BLUE]],
              [[2, 1, .4, DARK_BLUE]],
              [[3, 1, .5, DARK_BLUE]],
              [[4, 1, .5, DARK_BLUE]],
              [[5, 0, .5, DARK_BLUE]],
              [[6, 0, .4, DARK_BLUE]],
              [[7, 0, .3, DARK_BLUE]],
             ]

def move_pixel(pixel_path, delay):
    for path_group in pixel_path:
        for path in path_group:
            brightness = path[2]
            color = path[3]
            x, y = path[0], path[1]
            unicorn.brightness(brightness)
            unicorn.set_pixel(x, y, color[0], color[1], color[2])
        unicorn.show()
        time.sleep(delay)
        unicorn.clear() 


def blink_pixel(x, y, starting_brightness, ending_brightness, num_brightness_steps, delay, color):
    for brightness in np.linspace(starting_brightness, ending_brightness, num_brightness_steps):
        unicorn.brightness(brightness)
        unicorn.set_pixel(x, y, color[0], color[1], color[2])
        unicorn.show()
        time.sleep(delay)
    unicorn.clear()
    unicorn.show()

move_pixel(green_path, .2)
blink_pixel(7, 0, .25, .7, 20, .05, PURE_WHITE)

pulse(getClockTime() + 1, BLUE_GREEN[0], BLUE_GREEN[1], BLUE_GREEN[2], .3, .5, .01, 1)

"""
color = BLUE_GREEN
for i in range(width):
    for j in range(height):
        unicorn.set_pixel(i, j, color[0], color[1], color[2])
unicorn.show()
time.sleep(5) 
"""
"""
for i in range(width):
    for j in range(height):
        if j % 3 == 0:
            color = DEEP_GREEN
        elif j % 3 == 1:
            color = PURE_WHITE
        elif j % 3 == 2:
            color = DARK_BLUE
        unicorn.set_pixel(i, j, color[0], color[1], color[2])
unicorn.show()
time.sleep(5)
"""
"""
for i in range(5):
    x = random.randint(0, 8)
    y = random.randint(0, 4)
    blink_pixel(x, y, .25, .7, 20, .05, PURE_WHITE)
"""

# input()
