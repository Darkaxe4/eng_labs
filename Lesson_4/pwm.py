import RPi.GPIO as GPIO

PWM_PORT = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PORT, GPIO.OUT)

try:
    p = GPIO.PWM(PWM_PORT, 1000)
    p.start(0)
    inp = input()
    while inp != "q":
        if any(map(str.isalpha, inp)):
            print("ERR:\tNAN")
        elif ("." in inp):
            print("ERR:\tnon-integer value")
        elif(int(inp) < 0):
            print("ERR:\tnegative value")
        else:
            inp = int(inp)
            p.ChangeDutyCycle(inp)
        inp = input()


finally:

    GPIO.output(PWM_PORT, 0)
    GPIO.cleanup()