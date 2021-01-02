# mood_lamp_guide
A guide on how to setup a pimoroni mood lamp, including links to various tutorials.   
![](alexa_light_demo.gif)

There are four steps to this. Setup the pi, put in the headers to the pi and the pHAT, and then put together the mood lamp, and then configure the mood lamp to run regularly.

## Equipment Needed
You'll need a mood lamp kit from pimoroni [here](https://shop.pimoroni.com/products/mood-light-pi-zero-w-project-kit).   
You can use solderless headers so you don't have to solder them and you can instead hammer them in. For example these products [here](https://shop.pimoroni.com/products/gpio-hammer-header?variant=35643318026).   
You may also want a power adaptor that will plug into the wall. I like the official power supply in white color as it matches the lamp (ensure its a micro usb port for the pi zero). You can see an example [here](https://shop.pimoroni.com/products/raspberry-pi-universal-power-supply).

## Setting up the Pi
You can follow the guide here [pi_setup_guide](https://github.com/MZandtheRaspberryPi/pi_headless_setup) and do the first two sections including "Preparing the Micro SD Card" and "First SSH connection, changing default user". 

## Putting in the headers to the Pi and pHAT
I'll assume you have solderless headers. To use them, follow the guide and put in the male headers to the pi, and the female headers to the pHAT. [guide here](https://learn.pimoroni.com/tutorial/sandyj/fitting-hammer-headers).

## Putting the Lamp Together
You can follow the [guide here](https://learn.pimoroni.com/tutorial/sandyj/fitting-hammer-headers).

## Get familiar with the pHAT code
I'd recommend going through this tutorial [here](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-unicorn-phat) and running a python console and running the given commands line by line to see how the lamp works and how you can control it with code. From here you should be ready to write your own code! Imagine a light show, a lamp that turns itself on and off at regular times, or some other creative use.

## Scheduling a script to run on startup
You'll need to setup a cron job to run a script of your choosing on startup. You can see the example script I included called auto_lamp.py in this repository, or you could use one of the pimoroni examples in unicornhat/examples folder in your home directory. I particularly like the rainbow.py example!

To use this, navigate to your crontab for the super user:    
```sudo crontab -e```

And add a line at the bottom replacing your user in the home directory.   
```@reboot sudo python3 /home/[your_user]/unicornhat/examples/rainbow.py```

Then when you reboot the pi, it should run this script at startup and you should see your line come in.   
```sudo reboot```
