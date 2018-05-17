import json, math, signal, sys, time
from SpeedSensor import SpeedSensor

def main():
    """Main interface"""
    path_file = sys.argv[1]
    path = read_json(path_file)['path']
    speed_sensor = init_speed_sensor()

    for action in path:
        print(action)
        speed_sensor.set_pulse(0)
        if action['direction'] == 'forward':
            speed_sensor.forward(action['distance'])
        elif action['direction'] == 'reverse':
            speed_sensor.reverse(action['distance'])
        elif action['direction'] == 'left':
            speed_sensor.left()
        elif action['direction'] == 'right':
            speed_sensor.right()
        elif action['direction'] == 'quit':
            speed_sensor.cleanup()
        time.sleep(1)

def init_speed_sensor():
    speed_sensor = SpeedSensor()
    speed_sensor.set_in_pin(22)
    speed_sensor.set_pulse(0)
    speed_sensor.set_radius(3.175)
    speed_sensor.set_circumference((2 * math.pi) * speed_sensor.radius)
    speed_sensor.speed_init()
    speed_sensor.init_interrupt()
    signal.signal(signal.SIGINT, speed_sensor.signal_handler)
    time.sleep(2)
    return speed_sensor

def read_json(filename):
    with open(filename) as map_file:
        data = json.load(map_file)
    return data

if __name__ == '__main__':
    main()
