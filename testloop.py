import time
import RPi.GPIO as GPIO



motor_pin1 = 17
motor_pin2 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)

T = 60 # T = time motor is running
ST = 60 # ST = time motor is stopped

loop_count =0

def motor_forward(Duration):
    GPIO.output(motor_pin1, GPIO.HIGH)
    GPIO.output(motor_pin2, GPIO.LOW)
    time.sleep(Duration)

def motor_backward(Duration):
    GPIO.output(motor_pin1, GPIO.LOW)
    GPIO.output(motor_pin2, GPIO.HIGH)
    time.sleep(Duration)    

def stop_motor(Duration):
    GPIO.output(motor_pin1, GPIO.LOW)
    GPIO.output(motor_pin2, GPIO.LOW)
    time.sleep(Duration)
   
try:
    while True:
        motor.forward(T)
        stop_motor()
        time.sleep(ST)
        motor.backward(T)
        stop_motor()
        time.sleep(ST)
        loop_count += 1


except KeyboardInterrupt:
    GPIO.cleanup()