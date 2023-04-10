import RPi.GPIO as GPIO

CLEAN_PORT = list(range(28))

GPIO.setmode(GPIO.BCM)
GPIO.setup(CLEAN_PORT, GPIO.OUT)
GPIO.cleanup()