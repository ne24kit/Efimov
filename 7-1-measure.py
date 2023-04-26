import RPi.GPIO as GPIO

import time

import matplotlib.pyplot as plt


dac = [26, 19, 13, 6, 5, 11, 9, 10]

led = [21, 20, 16, 12, 7, 8, 25, 24]

comp = 4

troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(led, GPIO.OUT)

GPIO.setup(comp, GPIO.IN)

#GPIO.output(dac, 0)
#GPIO.output(led, 0)
#GPIO.cleanup()

def decimal_to_binary(value):
    return [int(element) for element in  bin(value)[2:].zfill(8)]

def adc():
    count = 0
    for value in range(7, -1, -1):
        count += 2**value
        signal = decimal_to_binary(count)
        GPIO.output(dac, signal)
        time.sleep(0.01)
        compval = GPIO.input(comp)
        if compval == 0:
            count -= 2**value
    return count 


def leds_on(value):
    c = 0
    for i in range(8):
        if (i/8)*256 <= value:
            c += 2**i
    GPIO.output(led, decimal_to_binary(c))
  
try:
    res = []
    time_begin = time.time()
    point = 0
    count = 0

    #зарядка
    GPIO.output(troyka, 0)
    time.sleep(5)
    GPIO.output(troyka, 1)

    while point < 40:
        point = adc()
        print(point)
        res.append(point*3.3/256)
        print("{:.3f}".format(point*3.3/256))
        count += 1
        leds_on(point)

    #разрядка
    GPIO.output(troyka, 0)

    while point > 10:
        point = adc()
        res.append(point*3.3/256)
        print("{:.3f} V".format(point*3.3/256))
        count += 1
        leds_on(point)
    
    time_end = time.time()
    
    total_time =  time_end - time_begin
    print("{:.3f} c".format(total_time))
    plt.title("График зависимости U от t") # заголовок
    plt.xlabel("t") # ось абсцисс
    plt.ylabel("U") # ось ординат
    plt.grid()      # включение отображение сетки
    #time_ar = [i for i in range(int(total_time)) ]
    #plt.plot(res, "r--")  # построение графика
    plt.plot(res)
    plt.show()

    with open('data.txt', 'w') as f:
        for i in res:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1/total_time/count))
        f.write('\n')
        f.write(str(3.3/256))

except KeyboardInterrupt:
    print('KeyboardInterrupt')

finally:
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()    