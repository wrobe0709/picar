import RPi.GPIO as GPIO
import time

TRIG = 16
ECHO = 18


def sensor_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)


def sensor_settle():
    GPIO.output(TRIG, False)
    time.sleep(2)


def sensor_distance():
    sensor_init()
    pulse_end = 0
    pulse_start = 0

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    
    distance = round(distance, 2)
    GPIO.cleanup()
    return distance
