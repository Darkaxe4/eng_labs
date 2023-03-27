import RPi.GPIO as GPIO


DAC_MAX_U = 3.3
DAC_BIT_DEPTH = 8
DAC_PORTS = [10, 9, 11, 5, 6, 13, 19, 26]
DAC_PORTS.reverse()

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC_PORTS, GPIO.OUT)

try:
    inp = input()
    while inp != "q":
        if any(map(str.isalpha, inp)):
            print("ERR:\tNAN")
        elif ("." in inp):
            print("ERR:\tnon-integer value")
        elif(int(inp) < 0):
            print("ERR:\tnegative value")
        elif(int(inp) > (2 ** DAC_BIT_DEPTH - 1)):
            print("ERR:\tvalue > 255")
        else:
            inp = int(inp)
            GPIO.output(DAC_PORTS, tuple(map(lambda x: 1 & int(x), "{0:0>8}".format(bin(inp)[2:]))))
            print("OUT_VOLTAGE:\t{:.4f}".format(inp / (2 ** DAC_BIT_DEPTH - 1) * DAC_MAX_U))
        inp = input()

finally:
    GPIO.output(DAC_PORTS, 0)
    GPIO.cleanup()