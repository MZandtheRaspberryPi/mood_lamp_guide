#!/usr/bin/env python3
#autoLamp.py, a script that lights the LEDs so that in the morning there is increasingly bright yellow light, then pulsing
#and in the evening increasingly dimmer blue/purple light.

import logging
import datetime
import time
import unicornhat as uh
import rainbow

def sleepTillMorn(startTime):
    while True:
        dt = datetime.datetime.now()
        clockTime = dt.strftime('%H%M')
        clockTime = int(clockTime)
        if clockTime >=startTime:
            break
        time.sleep(10)

def pulse(startTime,endTime,r,g,b,maxBrightness=.5,pulseTimeInterval=.01,brightStepInterval=1):
    brightRange = list(range(200,int(maxBrightness*1000),brightStepInterval))
    while True:
        dt = datetime.datetime.now()
        clockTime = dt.strftime('%H%M')
        clockTime = int(clockTime)
        logging.info(clockTime)
        if clockTime >= startTime and clockTime < endTime:
            for brightness in brightRange:
                setAllPixels(r,g,b,brightness/1000)
                time.sleep(pulseTimeInterval)
            brightRange.reverse()
            for brightness in brightRange:
                setAllPixels(r,g,b,brightness/1000)
                time.sleep(pulseTimeInterval)
            brightRange.reverse()
        else:
            break

def setAllPixels(r,g,b,brightness):
    uh.brightness(brightness)
    for x in range(8):
        for y in range(8):
            uh.set_pixel(x,y,r,g,b)
    uh.show()

weekdaySchedule = {'firstWakeUpTime':620,
'secondWakeUpTime':640,
'thirdWakeUpTime':645,
'fourthWakeUpTime':7,
'goneTime':800,
'restartTime':1600,
'firstBedTime':2000,
'secondBedTime':2015,
'thirdBedTime':2030,
'offTime':2045}

weekendSchedule = {'firstWakeUpTime':800,
'secondWakeUpTime':815,
'thirdWakeUpTime':830,
'fourthWakeUpTime':1000,
'firstBedTime':2300,
'secondBedTime':2315,
'thirdBedTime':2330,
'offTime':2345}

if __name__ == "__main__":
    # this won't be run when imported
    logging.basicConfig(filename = '/home/mikey/logs/autoLampLog.txt',level=logging.DEBUG,
         format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.disable(logging.DEBUG)
    print('running lamp...')

    uh.set_layout(uh.PHAT)

    while True:
        dt = datetime.datetime.now()
        day = dt.strftime('%A')
        clockTime =  dt.strftime('%H%M')
        clockTime = int(clockTime)
        lightYellow3 = [255,255,102]
        blueViolet = [138,43,226]
        #Weekend Section
        if day in ['Saturday','Sunday']:
            #logging.info("It's a weekend!")
            if clockTime >= weekendSchedule['firstWakeUpTime'] and  clockTime <  weekendSchedule['secondWakeUpTime']:
                r,g,b = lightYellow3[0],lightYellow3[1],lightYellow3[2]
                setAllPixels(r,g,b,brightness=.2)
            elif clockTime >= weekendSchedule['secondWakeUpTime'] and clockTime < weekendSchedule['thirdWakeUpTime']:
                r,g,b = lightYellow3[0],lightYellow3[1],lightYellow3[2]
                setAllPixels(r,g,b,brightness=.3)
            elif clockTime >= weekendSchedule['thirdWakeUpTime'] and clockTime < weekendSchedule['fourthWakeUpTime']:
                r,g,b = lightYellow3[0],lightYellow3[1],lightYellow3[2]
                pulse(weekendSchedule['thirdWakeUpTime'],weekendSchedule['fourthWakeUpTime'],r,g,b)
            elif day == 'Saturday' and clockTime >= weekendSchedule['fourthWakeUpTime'] and clockTime < weekendSchedule['firstBedTime']:
                rainbow.rainbow(weekendSchedule['firstBedTime'])
            elif day == 'Saturday' and clockTime >= weekendSchedule['firstBedTime'] and clockTime < weekendSchedule['secondBedTime']:
                r,g,b = blueViolet[0],blueViolet[1],blueViolet[2]
                pulse(weekendSchedule['firstBedTime'], weekendSchedule['secondBedTime'], r,g,b,maxBrightness = .6)
            elif day == 'Saturday' and  clockTime >= weekendSchedule['secondBedTime'] and clockTime < weekendSchedule['thirdBedTime']:
                r,g,b = blueViolet[0],blueViolet[1],blueViolet[2]
                pulse(weekendSchedule['firstBedTime'],weekendSchedule['secondBedTime'],r,g,b,maxBrightness = .4)
            elif day == 'Saturday' and  clockTime >= weekendSchedule['thirdBedTime'] and clockTime < weekendSchedule['offTime']:
                r,g,b = blueViolet[0],blueViolet[1],blueViolet[2]
                setAllPixels(r,g,b,brightness = .2)
            elif day == 'Sunday' and clockTime >= weekendSchedule['fourthWakeUpTime'] and clockTime < weekdaySchedule['firstBedTime']:
                rainbow.rainbow(weekdaySchedule['firstBedTime'])
            elif day == 'Sunday' and clockTime >= weekdaySchedule['firstBedTime'] and clockTime < weekdaySchedule['secondBedTime']:
                r,g,b = blueViolet[0],blueViolet[1],blueViolet[2]
                pulse(weekdaySchedule['firstBedTime'], weekdaySchedule['secondBedTime'], r,g,b,maxBrightness = .5)
            elif day == 'Sunday' and clockTime >= weekdaySchedule['secondBedTime'] and clockTime < weekdaySchedule['thirdBedTime']:
                r,g,b = blueViolet[0],blueViolet[1],blueViolet[2]
                pulse(weekdaySchedule['secondBedTime'],weekdaySchedule['thirdBedTime'],r,g,b,maxBrightness = .4)
            elif day == 'Sunday' and clockTime >= weekdaySchedule['thirdBedTime'] and clockTime < weekdaySchedule['offTime']:
                r,g,b = blueViolet[0],blueViolet[1],blueViolet[2]
                setAllPixels(r,g,b,brightness = .2)
            elif day == 'Saturday' and clockTime >= weekendSchedule['offTime']:
                uh.clear()
                uh.show()
                logging.info("Sleeping till "+str(weekendSchedule['firstWakeUpTime']))
                sleepTillMorn(weekendSchedule['firstWakeUpTime'])
            elif day == 'Sunday' and clockTime >= weekdaySchedule['offTime']:
                uh.clear()
                uh.show()
                logging.info("Sleeping till "+str(weekdaySchedule['firstWakeUpTime']))
                sleepTillMorn(weekdaySchedule['firstWakeUpTime'])
        #Weekday Section
        else:
            #logging.info("It's a weekday")
            if clockTime >= weekdaySchedule['firstWakeUpTime'] and  clockTime <  weekdaySchedule['secondWakeUpTime']:
                r,g,b = lightYellow3[0],lightYellow3[1],lightYellow3[2]
                setAllPixels(r,g,b,brightness=.2)
            elif clockTime >= weekdaySchedule['secondWakeUpTime'] and clockTime < weekdaySchedule['thirdWakeUpTime']:
                r,g,b = lightYellow3[0],lightYellow3[1],lightYellow3[2]
                setAllPixels(r,g,b,brightness=.3)
            elif clockTime >= weekdaySchedule['thirdWakeUpTime'] and clockTime < weekdaySchedule['fourthWakeUpTime']:
                r,g,b = lightYellow3[0],lightYellow3[1],lightYellow3[2]
                pulse(weekdaySchedule['thirdWakeUpTime'],weekdaySchedule['fourthWakeUpTime'],r,g,b)
            elif clockTime >= weekdaySchedule['fourthWakeUpTime'] and clockTime < weekdaySchedule['goneTime']:
                r,g,b = lightYellow3[0],lightYellow3[1],lightYellow3[2]
                pulse(weekdaySchedule['fourthWakeUpTime'],weekdaySchedule['fourthWakeUpTime'],r,g,b)
            elif clockTime >= weekdaySchedule['goneTime'] and clockTime < weekdaySchedule['restartTime']:
                uh.clear()
                uh.show()
                sleepTillMorn(weekdaySchedule['restartTime'])
            elif clockTime >= weekdaySchedule['restartTime'] and clockTime < weekdaySchedule['firstBedTime']:
                r,g,b = blueViolet[0],blueViolet[1],blueViolet[2]
                pulse(weekdaySchedule['fourthWakeUpTime'],weekdaySchedule['firstBedTime'],r,g,b,maxBrightness=.6)
            elif clockTime >= weekdaySchedule['firstBedTime'] and clockTime < weekdaySchedule['secondBedTime']:
                r,g,b = blueViolet[0],blueViolet[1],blueViolet[2]
                pulse(weekdaySchedule['firstBedTime'], weekdaySchedule['secondBedTime'], r,g,b,maxBrightness = .5)
            elif clockTime >= weekdaySchedule['secondBedTime'] and clockTime < weekdaySchedule['thirdBedTime']:
                r,g,b = blueViolet[0],blueViolet[1],blueViolet[2]
                pulse(weekdaySchedule['firstBedTime'],weekdaySchedule['secondBedTime'],r,g,b,maxBrightness = .4)
            elif clockTime >= weekdaySchedule['thirdBedTime'] and clockTime < weekdaySchedule['offTime'] and not day == 'Friday':
                r,g,b = blueViolet[0],blueViolet[1],blueViolet[2]
                setAllPixels(r,g,b,brightness = .2)
            elif clockTime >= weekdaySchedule['offTime'] and not day == 'Friday':
                uh.clear()
                uh.show()
                logging.info("Sleeping till "+str(weekdaySchedule['firstWakeUpTime']))
                sleepTillMorn(weekdaySchedule['firstWakeUpTime'])
            elif day == 'Friday' and clockTime >= weekdaySchedule['offTime'] and clockTime < weekendSchedule['offTime']:
                r,g,b = blueViolet[0],blueViolet[1],blueViolet[2]
                pulse(weekdaySchedule['offtime'],weekendSchedulej['offTime'],r,g,b,maxBrightness = .4)
            elif day == 'Friday' and clockTime >= weekendSchedule['offTime']:
                uh.clear()
                uh.show()
                logging.info("Sleeping till "+str(weekendSchedule['firstWakeUpTime']))
                sleepTillMorn(weekendSchedule['firstWakeUpTime'])
        time.sleep(10)
