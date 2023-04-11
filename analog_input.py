import mpio
import sys
import time

adc = mpio.ADC(0)
value = None
while True:
    current = adc.value(7) #mikrobus pd26 pin 122


    if value != current:
        sys.stdout.write("\r Channel 0: {0} ".format((current)))
        sys.stdout.flush()
        #print("\rADC value:",(current1*0.402832031)/1000)
        #print(" Analog pin 10: ",(current*0.402832031)/1000)
        value = current
        time.sleep(0.5)