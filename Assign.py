import time
from gpiozero import Motor, DigitalInputDevice, Button

motor = Motor(forward=17, backward=18,)
light_sensor =DigitalInputDevice(22)
limit_switch = Button(23)

def motor_start():
    motor.forward()

def motor_stop():
    motor.backward()

while True:
    loop_count += 1
    print(f"Loop coiunt: {loop_count}")
    if light_sensor.is_active:
        print("Light sensor is active")
        if not limit_switch.is_pressed:
            motor_start()
            print("motor started")
        else:
            print("Limit switch is pressed Motor down")
            motor_stop()
    else:
        print("Light sensor is not active, waiting...")
        time.sleep(1)



