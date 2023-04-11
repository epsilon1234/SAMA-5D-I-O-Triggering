from mpio import LED
import time
from mpio import GPIO
import mpio

#Press the user push button for LED's to trigger

def main():
    red = LED("red")
    green = LED("green")
    blue = LED("blue")
    pin_out=GPIO(84,GPIO.OUT)
    pin_out.set(False)
    while(True):
        print("Please Press The User Push Button On The Board")
        device_id=("event0")
        button=mpio.Input(device_id)
        (tv_sec, tv_usec, evtype, code, value) = button.read()
        if(value==1):
            print("Button Pressed")
            pin_out.set(True)
            #time.sleep(10)
            for i in range(2):
                red.brightness = 51
                green.brightness = 0
                blue.brightness = 0
                time.sleep(1)

                red.brightness = 253
                green.brightness = 253
                blue.brightness = 0
                time.sleep(1)

                red.brightness = 0
                green.brightness = 0
                blue.brightness = 50
                time.sleep(1)

                red.brightness = 0
                green.brightness = 0
                blue.brightness = 0
                time.sleep(1)
            print("Action Completed")
            pin_out.set(False)
    pin_out.close() # if program exits pin is closed
if __name__ == "__main__":
    main()