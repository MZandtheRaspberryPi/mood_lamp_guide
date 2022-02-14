#!/usr/bin/env python

import math
import time
from datetime import datetime
import unicornhat as unicorn


def rainbow(stop_time):
    width,height=unicorn.get_shape()
    i = 0.0
    offset = 30
    while int(datetime.now().strftime("%H%M")) < stop_time:
        i = i + 0.3
        for y in range(height):
            for x in range(width):
                r = 0
                g = 0
                r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
                g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
                b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
                r = max(0, min(255, r + offset))
                g = max(0, min(255, g + offset))
                b = max(0, min(255, b + offset))
                unicorn.set_pixel(x,y,int(r),int(g),int(b))
        unicorn.show()
        time.sleep(0.01)

if __name__ == "__main__":
    rainbow(2359)
