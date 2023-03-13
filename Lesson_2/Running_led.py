import RPi.GPIO as GPIO
import time

LED_PORTS = [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setmode(GPIO.BCM)
for PORT in LED_PORTS:
    GPIO.setup(PORT, GPIO.OUT)

_port_index = 0
full_loops = 0
while full_loops < 3:
    GPIO.output(LED_PORTS[_port_index], 1)
    time.sleep(0.200)
    GPIO.output(LED_PORTS[_port_index], 0)
    full_loops += (_port_index + 1) // 8
    _port_index = (_port_index + 1) % 8 

GPIO.cleanup()