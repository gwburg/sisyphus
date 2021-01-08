from movement import move
from config import *
import RPi.GPIO as GPIO
import sys

if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        move(0,10,2)
        for i in range(15):
            move(12,2,1)
            move(12,-2,1)
        GPIO.output(angular_channels+radial_channels,(0,0,0,0,0,0,0,0))
        GPIO.cleanup()
            
    except KeyboardInterrupt:
        GPIO.output(angular_channels+radial_channels,(0,0,0,0,0,0,0,0))
        GPIO.cleanup()
        sys.exit()
