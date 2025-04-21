import RPi.GPIO as GPIO
from time import sleep

def dec2bin(n):
    number = [int(i) for i in bin(n)[2:]]
    while len(number) != 8:
        number = [0] + number
    return number

def adc():
    for i in range(256):
        GPIO.output(dac, dec2bin(i))
        sleep(0.001)
        if GPIO.input(comp) == 1:
            return i
    return 255

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)


try:
    while True:
        a = adc()
        v = a/256*3.3
        print(a, round(v, 3))
        # adc()
        sleep(0.01)
            
finally:
    GPIO.output(dac, 0)
