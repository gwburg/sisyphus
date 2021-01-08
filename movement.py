from config import *
import RPi.GPIO as GPIO
import time
import math
import threading

ang_curr = 0
rad_curr = 0
ang_curr_step = STEPS[0]
rad_curr_step = STEPS[0]

initialized = False
def init(func):
    def init_wrapper(*args,**kwargs):
        global initialized
        if not initialized:
            GPIO.setmode(GPIO.BCM)
            for pin in angular_channels + radial_channels:
                GPIO.setup(pin,GPIO.OUT)
            GPIO.setup(radial_endstop_channel,GPIO.IN)
            GPIO.setup(angle_endstop_channel,GPIO.IN)
            initialized = True
        func(*args,**kwargs)
    return init_wrapper


#ang: total angle moved -> deg, 
#rad_dist: total radial distance moved -> mm
#vel: total velocity of move -> mm/s
#ang0: initial angle
#r0: initial radius
def move(ang,rad_dist,vel,homing=False,ang0=0,rad0=0):
    global ang_curr
    global rad_curr
    if ang == 0 and rad_dist ==0:
        return
    vel = abs(vel)
    ang_curr = ang0
    rad_curr = rad0
    
    num_ang_steps = int((ang/360)*STEPS_PER_REV*3)
    num_rad_steps = int((STEPS_PER_REV*rad_dist)/PINION_CIRC-num_ang_steps/3)
    
    t_move = math.sqrt((((2*3.1416*ang)/360)*(rad_curr+rad_dist/2))**2 + rad_dist**2)/vel
    if t_move/max(abs(num_ang_steps),abs(num_rad_steps)) < 0.001:
        t_move = max(abs(num_ang_steps),abs(num_rad_steps))*0.001
    ang_step_delay = t_move/abs(num_ang_steps) if num_ang_steps != 0 else 0.001
    rad_step_delay = t_move/abs(num_rad_steps) + PROC_DELAY if num_rad_steps != 0 else 0.001
    
    radial_thread = threading.Thread(target=radial_move, args=(num_rad_steps,rad_step_delay,homing)) 
    radial_thread.start()
    angular_move(num_ang_steps,ang_step_delay,homing)
    radial_thread.join()


@init
def radial_move(num_steps,t_step,homing=False):
    global rad_curr_step
    reverse = False if num_steps >= 0 else True
    if reverse: 
        num_steps = abs(num_steps)
    
    for i in range(num_steps):
        rad_curr_step = next_step(rad_curr_step, reverse)
        GPIO.output(radial_channels, rad_curr_step)
        time.sleep(t_step)
        if homing and GPIO.input(radial_endstop_channel):
            break


@init
def angular_move(num_steps,t_step,homing=False):
    global ang_curr_step
    reverse = False if num_steps >= 0 else True
    if reverse: 
        num_steps = abs(num_steps)

    for i in range(num_steps):
        ang_curr_step = next_step(ang_curr_step, reverse)
        GPIO.output(angular_channels, ang_curr_step)
        time.sleep(t_step)
        if homing and GPIO.input(angle_endstop_channel):
            break

def home():
    global ang_curr
    global rad_curr
    move(360,0,100,homing=True)
    move(0,-100,100,homing=True)
    ang_curr = 0
    rad_curr = 0

