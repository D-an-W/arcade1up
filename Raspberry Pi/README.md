# Arcade 1Up scripts

Here I provide a Python script to use the Power button of the Arcade 1Up with a Raspberry Pi 5 assuming you have done similar mods to ETA Prime like so... https://www.youtube.com/watch?v=09DQCOr6zQM

This script runs in the background monitoring the toggle switch & then takes appropriate action accordingly.

### Power switch
Connect the black wire to Pin 5 (GPIO3) & the red wire to Pin 6 (Ground) of the GPIO header.

## Install

I created a directory called arcade1up under my home folder.
These instructions will do the same.
Hit F4 to exit out of RetroPie / Emulation Station to the terminal.

Type:

git clone https://github.com/D-an-W/arcade1up.git

#### Note: If you don't have git, you can download by typing sudo apt install git

Once complete you will have a directory under your home directory (/home/pi) called arcade1up.
Next we edit your rc.local file like so...type:

sudo nano /etc/rc.local

In nano scroll down to after fi line but before exit 0 & add the lines as so...

(sudo python /home/pi/arcade1up/Raspberry\ Pi/shutdown.py) &

Save the file (CTRL x, then y, then enter)

Reboot & profit! (sudo reboot)

### Special notes

The power switch will only power down the Raspberry Pi & not the monitor or speakers. You still need to physically power off at the wall. I haven't done anything with something like an IoT relay yet.

If you power off at the wall please ensure before you start the Pi to toggle the switch back to on.
