import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(n):
    print(n)
    number = [int(i) for i in bin(n)[2:]]
    while len(number) != 8:
        number = [0] + number
    return number
t = 6
tp = 1
period = float(input())
# halfperiod = 255 * x
try:
    while True:
        GPIO.output(dac, dec2bin(int(t)))
        
        if t == 255 or t == 0:
            tp *= -1
        sleep(period/255/2)
        t += tp
            
finally:
    GPIO.output(dac, 0)