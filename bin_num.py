import RPi.GPIO as GPIO


DAC_PORTS = [10, 9, 11, 5, 6, 13, 19, 26]
DAC_PORTS.reverse()

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC_PORTS, GPIO.OUT)

num = int(input())
while num < 256:
    out = "{0:0>8}".format(bin(num)[2:])
    print(out)
    for i in range(8):
        GPIO.output(DAC_PORTS[i], 1 & int(out[i]))
    num = int(input())

GPIO.cleanup()