import time
def battery_level():
    for level in range (100, -1, -10):
        print("Current BatteryLevel:", level, "%")
        time.sleep(1)


        if level > 50:
            print("battery Good")
 
        elif level > 20:
            print("battery low")
        
        else:

            print("battery Dead")
    
battery_level()