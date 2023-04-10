import RPi.GPIO as GPIO
import time

PORT_NUMBER = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(PORT_NUMBER, GPIO.OUT)


while True:
    GPIO.output(PORT_NUMBER, 1)
    time.sleep(0.500)
    GPIO.output(PORT_NUMBER, 0)
    time.sleep(0.500)

GPIO.cleanup()
