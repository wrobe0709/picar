import RPi.GPIO as gpio
import time
from sensor import sensor_distance, sensor_init, sensor_settle


def init():
    """Initialize car for driving"""
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)


def avoid_right():
    """Avoid to the right"""
    time.sleep(1)
    for turn in range(0, 2):
        right()
    time.sleep(1)
    forward(1)
    time.sleep(1)
    for turn in range(0, 2):
        left()
    time.sleep(1)
    forward(1)
    time.sleep(1)
    for turn in range(0, 2):
        left()
    time.sleep(1)
    forward(1)
    time.sleep(1)
    for turn in range(0, 2):
        right()
    return


def forward(seconds):
    """Drive car forward"""
    drive_time = 0
    init()
    gpio.output(11, gpio.HIGH)
    gpio.output(15, gpio.HIGH)
    while drive_time < seconds:
        sensor_init()
        distance = sensor_distance()
        init()
        if distance < 20:
            gpio.output(11, gpio.LOW)
            gpio.output(15, gpio.LOW)
            avoid_right()
            break
        else:
            drive_time += .25
            time.sleep(.25)
    gpio.output(11, gpio.LOW)
    gpio.output(15, gpio.LOW)


def reverse(seconds):
    """Drive car in reverse"""
    gpio.output(7, gpio.HIGH)
    gpio.output(13, gpio.HIGH)
    time.sleep(seconds)
    gpio.output(7, gpio.LOW)
    gpio.output(13, gpio.LOW)


def right():
    """Drive car right"""
    gpio.output(7, gpio.HIGH)
    gpio.output(15, gpio.HIGH)
    time.sleep(.15)
    gpio.output(7, gpio.LOW)
    gpio.output(15, gpio.LOW)


def left():
    """Drive car left"""
    gpio.output(11, gpio.HIGH)
    gpio.output(13, gpio.HIGH)
    time.sleep(.15)
    gpio.output(11, gpio.LOW)
    gpio.output(13, gpio.LOW)


def drive():
    """Handle user input for driving"""
    driving = True
    while driving:
        direction = input("Which way? > ")
        if direction == "forward":
            seconds = input("For how long? > ")
            forward(int(seconds))
        elif direction == "reverse":
            seconds = input("For how long? > ")
            reverse(int(seconds))
        elif direction == "left":
            left()
        elif direction == "right":
            right()
        elif direction == "quit":
            driving = False


def main():
    """Main interface"""
    init()
    sensor_init()
    sensor_settle()
    drive()
    gpio.cleanup()


if __name__ == '__main__':
    main()