import RPi.GPIO as GPIO
import time as t

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

def decimal_to_binary(value):
    return [int(element) for element in  bin(value)[2:].zfill(8)]
try:
    T = 0.1
    while(True):
        for i in range(256):
            l = []
            l = decimal_to_binary(i)
            for j in range(8):
                GPIO.output(dac[j], l[j])
            t.sleep(T)
        for i in range(255, -1, -1):
            l = []
            l = decimal_to_binary(i)
            for j in range(8):
                GPIO.output(dac[j], l[j])
            t.sleep(T)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()         
