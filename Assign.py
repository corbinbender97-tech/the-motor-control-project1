import time
from gpiozero import Motor, DigitalInputDevice, Button

motor = Motor(up=17, down=18,)
light_sensor =DigitalInputDevice(22)
limit_switch = Button(23)

def motor_start():
    motor.up()

def motor_stop():
    motor.down()

while true:
    if light_sensor.is_active:
        print("Light sensor is active")
        if not limit_switch.is_pressed:
            motor_start()
            print("motor started")
        else:
            print("Limit switch is pressed Motor down")
            motor_down()
    else:
        print("Light sensor is not active, waiting...")
        time.sleep(1)


