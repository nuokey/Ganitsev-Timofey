import RPi.GPIO as GPIO
from time import sleep

def dec2bin(n):
    number = [int(i) for i in bin(n)[2:]]
    while len(number) != 8:
        number = [0] + number
    return number

def adc():
    s = ""
    r = "00000000"
    for i in range(8):
        GPIO.output(dac, dec2bin(2**(7-i)+int(r, 2)))
        sleep(0.001)
        if GPIO.input(comp) == 1:
            s += "0"
        else:
            s += "1"
            r = s
            while len(r) != 8:
                r += "0"
                # print(i, 2**i+int(r, 2), r, s)
            # print(r)
    
    # print(s)
    return(int(s, 2))

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
        print(a)
        v = a/256*3.3
        print(a, round(v, 3))
        sleep(0.01)
            
finally:
    GPIO.output(dac, 0)
