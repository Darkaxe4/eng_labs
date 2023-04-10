import RPi.GPIO as GPIO

IN_PORT_NUMBER = 23
OUT_PORT_NUMBER = 14

GPIO.setmode(GPIO.BCM)


GPIO.setup(OUT_PORT_NUMBER, GPIO.OUT)
GPIO.setup(IN_PORT_NUMBER, GPIO.IN)

command = 0
state = 0
while command != 'exit':
    if (GPIO.input(IN_PORT_NUMBER)):
        state = 1
    else:
        state = 0
    GPIO.output(OUT_PORT_NUMBER, state)
    command = input()

GPIO.cleanup()