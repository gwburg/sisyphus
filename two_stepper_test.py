from movement import move
from config import *
import RPi.GPIO as GPIO
import sys

if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        if len(sys.argv) != 4:
            pass
        else:
            angle = int(sys.argv[1]) #deg
            radial_dist = int(sys.argv[2]) #mm
            velocity = int(sys.argv[3]) #mm/s
            move(angle,radial_dist,velocity)
            GPIO.output(angular_channels+radial_channels,(0,0,0,0,0,0,0,0))
            GPIO.cleanup()
            
    except KeyboardInterrupt:
        GPIO.output(angular_channels+radial_channels,(0,0,0,0,0,0,0,0))
        GPIO.cleanup()
        sys.exit()
