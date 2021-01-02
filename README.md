# mood_lamp_guide
A guide on how to setup a pimoroni mood lamp, including links to various pieces

There are four steps to this. Setup the pi, put in the headers to the pi and the pHAT, and then put together the mood lamp, and then configure the mood lamp to run regularly.

## Setting up the Pi
You can follow the guide here [pi_setup_guide](https://github.com/MZandtheRaspberryPi/pi_headless_setup) and do the first two sections including "Preparing the Micro SD Card" and "First SSH connection, changing default user". 

## Putting in the headers to the Pi and pHAT
I'll assume you have solderless headers. To use them, follow the guide and put in the male headers to the pi, and the female headers to the pHAT. [guide here](https://learn.pimoroni.com/tutorial/sandyj/fitting-hammer-headers).

## Putting the Lamp Together
You can follow the [guide here](https://learn.pimoroni.com/tutorial/sandyj/fitting-hammer-headers).

## Scheduling a script to run regularly
You'll need to setup a cron job to run a script of your choosing on startup.
