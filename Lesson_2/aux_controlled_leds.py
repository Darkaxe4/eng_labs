import RPi.GPIO as GPIO


AUX_PORTS = [2, 3, 14, 15, 18, 27, 23, 22] #some input ports
LED_PORTS = [24, 25, 8, 7, 12, 16, 20, 21] #some output ports

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PORTS, GPIO.OUT)
GPIO.setup(AUX_PORTS, GPIO.IN)

cmd = input()

while cmd != "exit":
    for i in range(len(AUX_PORTS)):
       GPIO.output(LED_PORTS[i], GPIO.input(AUX_PORTS[i]))
    cmd = input()

GPIO.cleanup()
