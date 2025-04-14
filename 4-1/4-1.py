import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def binary(n):
    number = [int(i) for i in bin(n)[2:]]
    while len(number) != 8:
        number = [0] + number
    return number

try:
    while True:
        number = input()
        if number == "q":
            exit()
        elif "." in number:
            print("Is a float")
        elif "-" in number:
            print("Negative number")
        else:
            try: 
                number = int(number)
                if number > 255:
                    print("More than 255")
                else:
                    GPIO.output(dac, binary(number))
                    # print(binary(number))
                    print(number/255*3.3+0.03)
            except:
                print("Not a number") 
            
finally:
    GPIO.output(dac, 0)