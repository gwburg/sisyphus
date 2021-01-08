from movement import home
from config import *
import RPi.GPIO as GPIO
import sys

if __name__ == '__main__':
    try:
        home()
        GPIO.output(angular_channels+radial_channels,(0,0,0,0,0,0,0,0))
        GPIO.cleanup()
            
    except KeyboardInterrupt:
        GPIO.output(angular_channels+radial_channels,(0,0,0,0,0,0,0,0))
        GPIO.cleanup()
        sys.exit()
