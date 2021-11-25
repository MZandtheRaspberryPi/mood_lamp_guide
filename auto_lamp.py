#!/usr/bin/env python3
#autoLamp.py, a script that lights the LEDs so that in the morning there is increasingly bright yellow light, then pulsing
#and in the evening increasingly dimmer blue/purple light.

import logging
import datetime
import time
import unicornhat as uh
import snow



LIGHT_YELLOW_3 = [255, 255, 102]
BLUE_VIOLET = [138, 43, 226]


# first wake up time, second wake up time, third wakeup time, fourth wakeup time
# gone time, restart time, first bed time, second bed time, third bed time, offtime
weekdayScheduleHours = [640, 650, 700, 730, 800, 1600, 2100, 2110, 2120, 2130]

weekendScheduleHours = [800, 815, 830, 1000, 2200, 2220, 2230, 2240]

def getClockTime():
    dt = datetime.datetime.now()
    clockTime = dt.strftime('%H%M')
    clockTime = int(clockTime)
    return clockTime

def getDay():
    dt = datetime.datetime.now()
    day = dt.strftime('%A')
    return day

def sleepTillMorn(startTime):
    priorDay = getDay()
    while getClockTime() < startTime or priorDay == getDay():
        time.sleep(10)

def pulse(endTime, r, g, b, maxBrightness=.5, pulseTimeInterval=.01, brightStepInterval=1):
    brightRange = list(range(200, int(maxBrightness*1000), brightStepInterval))
    while getClockTime() < endTime:
        for brightness in brightRange:
            setAllPixels(r, g, b, brightness / 1000)
            time.sleep(pulseTimeInterval)
        brightRange.reverse()
        for brightness in brightRange:
            setAllPixels(r, g, b, brightness / 1000)
            time.sleep(pulseTimeInterval)
        brightRange.reverse()


def setAllPixels(end_time, r, g, b, brightness):
    uh.brightness(brightness)
    for x in range(8):
        for y in range(8):
            uh.set_pixel(x, y, r, g, b)
    uh.show()
    while getClockTime() < end_time:
        time.sleep(3)


def snow_wrapper(end_time, r, g, b, brightness):
    snow.snow(end_time)

def sleep_till_morn_wrapper(end_time, r, g, b, brightness):
    sleepTillMorn(end_time)


weekdaySchedule = {640: {"color": LIGHT_YELLOW_3, "brightness": .2, "function": setAllPixels},
                   650: {"color": LIGHT_YELLOW_3, "brightness": .3, "function": setAllPixels},
                   700: {"color": LIGHT_YELLOW_3, "brightness": .5, "function": pulse},
                   730: {"color": LIGHT_YELLOW_3, "brightness": .5, "function": pulse},
                   800: {"color": LIGHT_YELLOW_3, "brightness": .2, "function": sleep_till_morn_wrapper},
                   1600: {"color": LIGHT_YELLOW_3, "brightness": .2, "function": snow_wrapper},
                   2100: {"color": BLUE_VIOLET, "brightness": .6, "function": pulse},
                   2110: {"color": BLUE_VIOLET, "brightness": .5, "function": pulse},
                   2120: {"color": BLUE_VIOLET, "brightness": .4, "function": pulse},
                   2130: {"color": BLUE_VIOLET, "brightness": .2, "function": sleep_till_morn_wrapper}}

weekendSchedule = {800: {"color": LIGHT_YELLOW_3, "brightness": .2, "function": setAllPixels},
                   815: {"color": LIGHT_YELLOW_3, "brightness": .3, "function": setAllPixels},
                   830: {"color": LIGHT_YELLOW_3, "brightness": .5, "function": pulse},
                   1000: {"color": LIGHT_YELLOW_3, "brightness": .2, "function": snow_wrapper},
                   2200: {"color": BLUE_VIOLET, "brightness": .6, "function": pulse},
                   2220: {"color": BLUE_VIOLET, "brightness": .5, "function": pulse},
                   2230: {"color": BLUE_VIOLET, "brightness": .4, "function": pulse},
                   2240: {"color": BLUE_VIOLET, "brightness": .2, "function": sleep_till_morn_wrapper}}


if __name__ == "__main__":
    # this won't be run when imported
    logging.basicConfig(filename = '/home/mikey/logs/autoLampLog.txt', level=logging.DEBUG,
                        format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.disable(logging.DEBUG)
    logging.info('running lamp...')

    uh.set_layout(uh.PHAT)

    while True:
        clockTime = getClockTime()
        day = getDay()

        settings_for_day = weekendSchedule if day == "Sunday" or day == "Saturday" else weekdaySchedule
        hours_for_day = weekendScheduleHours if day == "Sunday" or day == "Saturday" else weekdayScheduleHours

        current_hour_key = None
        end_time = None
        for i in range(0, len(hours_for_day)):
            hour_min = hours_for_day[i]
            if clockTime >= hour_min:
                continue
            elif not clockTime < hour_min:
                current_hour_key = hours_for_day[i - 1]
                end_time = hours_for_day[i]

        # if we are past the last time, its turn off time
        if current_hour_key is None and day not in ["Sunday", "Friday"]:
            current_hour_key = hours_for_day[-1]
            end_time = hours_for_day[0]
        # monday sleep till weekday wakeup
        elif current_hour_key is None and day == "Sunday":
            current_hour_key = hours_for_day[-1]
            end_time = weekdayScheduleHours[0]
        elif current_hour_key is None and day == "Friday":
            current_hour_key = hours_for_day[-1]
            end_time = weekendScheduleHours[0]

        logging.info("{} and current hour key is {} and end time is {}", day, current_hour_key, end_time)

        current_hour_settings = settings_for_day[current_hour_key]
        r, g, b = current_hour_settings["color"]
        brightness = current_hour_settings["brightness"]
        uh.clear()
        uh.show()
        current_hour_settings["function"](end_time, r, g, b, brightness)

        time.sleep(2)
