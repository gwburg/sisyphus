from movement import move, home
from config import *
import RPi.GPIO as GPIO
import sys
from itertools import islice

if __name__ == '__main__':
    try:
#        home()
        v = 10
        with open('test.txt') as points:
            (th0,r0) = points.readline().split('\t')
            th0 = float(th0)
            r0 = float(r0)
            move(th0,r0,v)

            for point in points:
                (th1,r1) = point.split('\t')
                th1 = float(th1)
                r1 = float(r1)

                d_th = th1-th0
                d_r = r1-r0
                move(d_th,d_r,v,ang0=th0,rad0=r0)
                th0 = th1
                r0 = r1

        GPIO.output(angular_channels+radial_channels,(0,0,0,0,0,0,0,0))
        GPIO.cleanup()
            
    except KeyboardInterrupt:
        GPIO.output(angular_channels+radial_channels,(0,0,0,0,0,0,0,0))
        GPIO.cleanup()
        sys.exit()


