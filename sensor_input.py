#a##Only the first 2 printing

from mpio import GPIO
import sys
import time
import mpio
import threading
import queue

i = 1
average = []
average.append(0)
count = 0
window_size = 10

def analog_value():
    adc = mpio.ADC(0)
    while True:
        value = adc.value(7) #mikrobus pd26 pin 122
        return value

def push_button():
    device_id = "event0"
    button = mpio.Input(device_id)
    state = 0
    while True:
        (tv_sec, tv_usec, evtype, code, digital_value) = button.read()
        if digital_value == 1:
            state = 1 - state
        time.sleep(0.1)  # wait for 100ms to avoid bouncing
        return state
    

def moving_average():
    global i, arr
    #amSwitch = push_button()
    #purgeSwitch = 0
    arr = []
    #while amSwitch == 1 and purgeSwitch == 0:
    while(True):
        arr.append(analog_value())
        if len(arr) > window_size:
            arr.pop(0)
            #print("Removing")
        if len(arr) >= window_size:
            window = arr[-window_size:]
            window_average = round(sum(window) / window_size, 2)
            #print("Averaging")
            return window_average
        time.sleep(0.05)
    return 0

def main():
    while True:
        print("The analog value is ", analog_value())
        #print("The button value is ", push_button())
        print("The averaged value is ", moving_average())

if __name__ == "__main__":
    t = threading.Thread(target=moving_average)
    #t.daemon = True
    t.start()
    t.join()
    main()
