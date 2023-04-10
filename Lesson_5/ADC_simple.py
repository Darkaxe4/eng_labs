import RPi.GPIO as GPIO
import time

DAC_PORTS = [10, 9, 11, 5, 6, 13, 19, 26]
DAC_PORTS.reverse()
COMP_PORT = 4
TROYKA_PORT = 17

REF_VOLTAGE = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC_PORTS, GPIO.OUT)
GPIO.setup(TROYKA_PORT, GPIO.OUT, initial = 0)
GPIO.setup(COMP_PORT, GPIO.IN)


def binarize_out(val: int):
    return tuple(map(lambda x: 1 & int(x), "{0:0>8}".format(bin(val)[2:])))

def get_ADC(bit_depth:int, comp_port:int, dac_ports:list):
    output = 0
    for i in range(len(dac_ports)-1, -1, -1):
        GPIO.output(dac_ports, binarize_out(output + 2 ** i))
        time.sleep(0.01)
        if GPIO.input(comp_port):
            output += 2 ** i
    return output
        


try:
    GPIO.output(TROYKA_PORT, 1)
    while True:
        val = get_ADC(len(DAC_PORTS), COMP_PORT, DAC_PORTS)
        VOLTAGE = REF_VOLTAGE * (val / (2 ** len(DAC_PORTS)))
        print(val, VOLTAGE)

finally:
    GPIO.output(DAC_PORTS, 0)
    GPIO.cleanup()