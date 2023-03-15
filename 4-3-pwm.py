import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)

def decimal_to_binary(value):
    return [int(element) for element in  bin(value)[2:].zfill(8)]

p = GPIO.PWM(2, 1000)
duty_cycle = 0
p.start(duty_cycle)
try:
    while(True):
        print('Enter duty cycle:')
        duty_cycle = int(input())
        p.ChangeDutyCycle(duty_cycle)  

finally:
    p.stop()
    GPIO.output(2, 0)
    GPIO.cleanup() 
