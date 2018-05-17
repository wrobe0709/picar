import json
import math
import signal
import time
from SpeedSensor import SpeedSensor

class Train():
    """Train robot to follow route"""

    def __init__(self):
        """Constructor"""
        self.current_direction = ''
        self.current_distance = ''
        self.path = []
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
            self.path.append({
                'direction': self.current_direction,
                'distance': self.current_distance
            })
        else:
            self.path.append({
                'direction': self.current_direction
            })

    def save_path_to_json(self):
        """Save path to JSON"""
        json_obj = {
            'path': self.path
        }
        with open('path.json', 'w+') as outfile:
            json.dump(json_obj, outfile)
