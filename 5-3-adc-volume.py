import RPi.GPIO as GPIO

import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

led = [21, 20, 16, 12, 7, 8, 25, 24]

comp = 4

troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

GPIO.setup(led, GPIO.OUT)

GPIO.setup(comp, GPIO.IN)


def decimal_to_binary(value):
    return [int(element) for element in  bin(value)[2:].zfill(8)]

def adc():
    count = 0
    for value in range(7, -1, -1):
        count += 2**value
        signal = decimal_to_binary(count)
        GPIO.output(dac, signal)
        time.sleep(0.001)
        compval = GPIO.input(comp)
        if compval == 0:
            count -= 2**value
    return count 

def leds_on(value):
    for i in range (8):
        GPIO.output(led[i], decimal_to_binary(value)[i])

def leds_on_2(value):
    c = 0
    for i in range(8):
        if (i/8)*64 <= value:
            c += 2**i

    GPIO.output(led, decimal_to_binary(c))
    
try:
    while(True):
        value = adc()
        #leds_on(value)
        leds_on_2(value)

        volt = (value*3.3)/256
        print("{:.3f} V".format(volt))

except KeyboardInterrupt:
    print('KeyboardInterrupt')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)    
