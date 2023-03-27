import RPi.GPIO as GPIO
import time


def triangulate(time, period, amp):
    n = time / period
    flt = n - int(n)
    if flt > 0.5:
        return (1-flt) * amp
    else:
        return flt * amp

def to_bits(signal, amplitude, bit_depth): 
    return round(signal / amplitude * (2 ** bit_depth))

DAC_MAX_U = 3.3
DAC_BIT_DEPTH = 8
DAC_PORTS = [10, 9, 11, 5, 6, 13, 19, 26]
DAC_PORTS.reverse()

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC_PORTS, GPIO.OUT)

try:
    T = float(input())
    begin = time.time()
    while True:
        cur = time.time() - begin
        f = triangulate(cur, T, DAC_MAX_U)
        val = to_bits(f, DAC_MAX_U, DAC_BIT_DEPTH)
        GPIO.output(DAC_PORTS, tuple(map(lambda x: 1 & int(x), "{0:0>8}".format(bin(val)[2:]))))


finally:
    GPIO.output(DAC_PORTS, 0)
    GPIO.cleanup()