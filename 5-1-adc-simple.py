import RPi.GPIO as GPIO

import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4

troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

GPIO.setup(comp, GPIO.IN)

def decimal_to_binary(value):
    return [int(element) for element in  bin(value)[2:].zfill(8)]

def adc():
    for value in range(256):
        signal = decimal_to_binary(value)
        GPIO.output(dac, signal)
        time.sleep(0.001)
        compval = GPIO.input(comp)
        if compval == 0:
            return value

try:
    while(True):
        value = adc()
        volt = (value*3.3)/256
        print("{:.3f} V".format(volt))

except KeyboardInterrupt:
    print('KeyboardInterrupt')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)    
