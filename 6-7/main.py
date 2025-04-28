import RPi.GPIO as GPIO
from time import sleep
import time
import matplotlib.pyplot as plt

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
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

l = []
down = False

time_start = time.time()
try:
    while True:
        a = adc()
        print(a)
        v = a/256*3.3
        print(a, round(v, 3))
        # sleep(0.01)
        s = round(a/256*8) * "1" + (8-round(a/256*8)) * "0"
        s = [int(i) for i in s] 
        
        GPIO.output(leds, s)
        if a >= 207:
            GPIO.output(troyka, 0)
            down = True
        if down and a == 0:
            time_stop = time.time()
            all_time = time_stop - time_start
            print(f"Experiment time: {all_time} s, period: {all_time/len(l)} s, discretisation: {len(l)/all_time} Hz, quantize step:{3.3/256} V")
            data = open("data.txt", "w")
            datatext = ""
            for i in l:
                datatext += str(i) + "\n"
            data.write(datatext)
            data.close()
            settings = open("settings.txt", "w")
            settings.write(f"Discretisation: {len(l)/all_time} Hz\nQuantize step:{3.3/256} V")
            settings.close()

            plt.plot(l)
            plt.show()
            
            exit()
        
        l.append(v)
            
finally:
    GPIO.output(leds, 0)