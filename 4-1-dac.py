import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

def decimal_to_binary(value):
    return [int(element) for element in  bin(value)[2:].zfill(8)]

try:
    while(True):
        print('Enter number in range 0 ... 255')
        c = input()
        if c == 'q':
            exit(0)
        b = int(c)        
        if (int(b) == b and 0 <= b and b <= 255):
            l = []
            l = decimal_to_binary(b)
            for i in range (8):
                GPIO.output(dac[i], l[i])
            print("{:.4f} V".format(b*3.3/256))
except ValueError:
    print('Eneter number 0 ... 255')
except ZeroDivisionError:  
    print("Деление на ноль!!! ZeroDivisionError." )
except KeyboardInterrupt:
    print('KeyboardInterrupt')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()    
