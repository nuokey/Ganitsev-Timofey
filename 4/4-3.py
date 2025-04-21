import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

p1 = GPIO.PWM(11, 60)
p1.start(10)

p2 = GPIO.PWM(24, 100)
p2.start(10)


def dec2bin(n):
    print(n)
    number = [int(i) for i in bin(n)[2:]]
    while len(number) != 8:
        number = [0] + number
    return number

try:
    while True:
        k = float(input())
        p1.ChangeDutyCycle(k)
        p2.ChangeDutyCycle(k)
            
finally:
    GPIO.output(dac, 0)