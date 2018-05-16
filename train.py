import math
import signal
import time
import speed_sensor
from speed_sensor import SpeedSensor

class Train():
    """Train robot to follow route"""

    def __init__(self):
        """Constructor"""
        self.current_direction = ''
        self.current_distance = ''
        self.speed_sensor = SpeedSensor()
        self.speed_sensor.set_in_pin(22)
        self.speed_sensor.set_pulse(0)
        self.speed_sensor.set_radius(3.175)
        self.speed_sensor.set_circumference((2 * math.pi) * self.speed_sensor.radius)
        self.speed_sensor.speed_init()
        self.speed_sensor.init_interrupt()
        signal.signal(signal.SIGINT, self.speed_sensor.signal_handler)
        time.sleep(2)

    def get_current_direction(self):
        """Get current direction from user"""
        self.current_direction = input("Which way? > ")
        if self.current_direction == 'forward' or self.current_direction == 'reverse':
            self.current_distance = input("How far (cm)? > ")

    def drive(self):
        """Drive"""
        speed_sensor.straight(self.speed_sensor, self.current_direction, self.current_distance)

if __name__ == '__main__':
    train = Train()
    training = True
    while training:
        train.get_current_direction()
        train.speed_sensor.set_pulse(0)
        if train.current_direction == 'forward':
            speed_sensor.forward(train.speed_sensor, train.current_distance)
        elif train.current_direction == 'reverse':
            speed_sensor.reverse(train.speed_sensor, train.current_distance)
        elif train.current_direction == 'left':
            speed_sensor.left()
        elif train.current_direction == 'right':
            speed_sensor.right()
        elif train.current_direction == 'quit':
            speed_sensor.cleanup()
            training = False