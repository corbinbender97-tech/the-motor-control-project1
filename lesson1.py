speed = 100 
voltage =3.3


motor_name = "ServoA"

is_running = True

print("Motor:", motor_name)
print("speed:", speed)
print("running:", is_running)

if is_running:
    print("The motor is Runninng.")
else:
    print("The motor is Stopped.")

for i in range(5):
    print("Loop number:", i)


def sart_motor():
    print("Motor Started.")