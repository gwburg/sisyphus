# stepper motor config
STEPS = ((1,0,0,0),(1,1,0,0),(0,1,0,0),(0,1,1,0),(0,0,1,0),(0,0,1,1),(0,0,0,1),(1,0,0,1))
#STEPS = ((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))
STEPS_PER_REV = 4096
def next_step(current_step, reverse=False):
    if current_step == STEPS[0]: return STEPS[1] if not reverse else STEPS[7]
    elif current_step == STEPS[1]: return STEPS[2] if not reverse else STEPS[0]
    elif current_step == STEPS[2]: return STEPS[3] if not reverse else STEPS[1]
    elif current_step == STEPS[3]: return STEPS[4] if not reverse else STEPS[2]
    elif current_step == STEPS[4]: return STEPS[5] if not reverse else STEPS[3]
    elif current_step == STEPS[5]: return STEPS[6] if not reverse else STEPS[4]
    elif current_step == STEPS[6]: return STEPS[7] if not reverse else STEPS[5]
    elif current_step == STEPS[7]: return STEPS[0] if not reverse else STEPS[6]


#GPIO config
#angular_channels = (4,17,27,22)
angular_channels = (22,27,17,4)
radial_channels = (19,13,6,5)
#radial_channels = (5,6,13,19)
radial_endstop_channel = 26
angle_endstop_channel = 21

# gearing config
PINION_CIRC = 39.861

# speed config
PROC_DELAY = 0.00044
#PROC_DELAY = 0
#ANG_V_MAX = 360/(STEPS_PER_REV*0.001)
#V_MAX = (PINION_CIRC/STEPS_PER_REV)*(1/0.001-1/t_r0)
#t_a = 0.001
#t_r0 = t_a*3 + 0.00044
