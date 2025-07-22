import time

def ramp_up_motor(target_speed):
    for speed in range(0, target_speed +1, step):
        print("Ramping Up", speed, "RPM")
        time.sleep(1)

def ramp_down_motor(start_speed):
    for speed in range(start_speed, -1, -step ):
        print("Ramping Down",speed, "RPM")
        time.sleep(step_time)


speed = int(input("Enter MOotr speed (0-100):"))
print("Speed set to,", speed, "RPM")

battery_level = int(input("Battery level set to _ %(0-100):"))
print("Battery Level set to,", battery_level,"%")

step = int(input("RPM accerlation or Decleration :"))
print("Step set to,", step, "RPM")

if battery_level > 50:
    print("Battery level good..... Ramping Up motor...")
    ramp_up_motor(speed)
    ramp_down_motor(speed)
elif battery_level > 20:
    print("Battery Level poor... Ramping down motor... cannot run at full speed" )

    ramp_up_motor(40)
    ramp_down_motor(40)

else:
    print(" Motor will not run")

if step <5:
    print("Acleration is increased")
    step_time = 0.2
else:
    print("Acclerlation is Normal")
    step_time = 1

