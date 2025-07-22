speed = 0
import time

def ramp_up_motor():
    for speed in range(0, 101, 20):
        print("Motor speed going to:", speed, " rpm")



def ramp_down_motor():
    for speed in range(100, -1, -25):
        print("Motor speed going to:", speed, "rpm")
        time.sleep(1)

for i in range (5):
    ramp_up_motor()
    ramp_down_motor()
    time.sleep(2)
    