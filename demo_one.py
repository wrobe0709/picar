import RPi.GPIO as gpio
import time


def main():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

    gpio.output(15, gpio.HIGH)
    time.sleep(2)
    gpio.output(15, gpio.LOW)

    gpio.output(13, gpio.HIGH)
    time.sleep(2)
    gpio.output(13, gpio.LOW)


if __name__ == '__main__':
    main()
    gpio.cleanup()
