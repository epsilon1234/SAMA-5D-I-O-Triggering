from mpio import LED
import time
from mpio import GPIO
import mpio

#Press the user push button for LED's to trigger
# We will be looping the pins PC 20 and PC 
def main():
    #global counter
    red = LED("red")
    green = LED("green")
    blue = LED("blue")
    pin_in=GPIO(83, GPIO.IN)
    pin_out=GPIO(84,GPIO.OUT)
    pin_out.set(False)
    counter=0
    while(True):
        print("Please Press The User Push Button On The Board")
        device_id=("event0")
        button=mpio.Input(device_id)
        (tv_sec, tv_usec, evtype, code, value) = button.read()
        if(value==1):
            count=0
            print("Button Pressed")
            for i in range (10):
                pin_out.set(True)
                pin_out.set(False)
                if(pin_in.get()==False):
                    counter=counter+1 #global counter
                    count=count+1 #current flow counter
                print("Current Flow: ",count)
                
                time.sleep(1)
            print("Total Flow: ",counter)
            print("Action Completed")
            pin_out.set(False)
    pin_out.close() # if program exits pin is closed
    pin_in.close() 
if __name__ == "__main__":
    main()