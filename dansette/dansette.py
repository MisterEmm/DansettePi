from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from ST7789 import ST7789
from subprocess import Popen
import os
import signal
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def increase_volume():
    change_volume('+')
    print("Volume Up")

def decrease_volume():
    change_volume('-')
    print("Volume Down")

def change_volume(ch_sign):
    Popen(['amixer', 'set', 'Master', 'unmute'])
    Popen(['amixer', 'set', 'Master', '5%{}'.format(ch_sign)])

def mute_volume():
    Popen(['amixer', 'set', 'Master', 'mute'])

#Set up screen
SPI_SPEED_MHZ = 80
screen = ST7789(
    rotation=90,  # Needed to display the right way up on Pirate Audio
    port=0,       # SPI port
    cs=1,         # SPI port Chip-select channel
    dc=9,         # BCM pin used for data/command
    backlight=13,
    spi_speed_hz=SPI_SPEED_MHZ * 1000 * 1000
)
# screen size details
width = screen.width
height = screen.height

i=1

screen.display(Image.open("/home/pi/dansette/icons/%s.jpg" % i))
os.system('cvlc /home/pi/dansette/stations/%s.m3u &' % i) 

while True:
    if (GPIO.input(6) ==0):
        i += 1
        if i > 8:
            i = 1
        else:
            i = i
        print ("Station %s" % i)
        screen.display(Image.open("/home/pi/dansette/icons/%s.jpg" % i))
        os.system('cvlc /home/pi/dansette/stations/%s.m3u &' % i)        
        sleep(.2)

    elif ( GPIO.input(14) ==0):
        i -= 1
        if i < 1:
            i = 8
        else:
            i = i
        print ("Station %s" % i)
        screen.display(Image.open("/home/pi/dansette/icons/%s.jpg" % i))
        os.system('cvlc /home/pi/dansette/stations/%s.m3u &' % i)        
        sleep(.2)

    elif ( GPIO.input(24) ==0):
        print ("Volume Up")
        increase_volume()
        sleep(.2)
        
    elif ( GPIO.input(20) ==0):
        print ("Volume Down")
        decrease_volume()
        sleep(.2)
    else:
        sleep(.2)
