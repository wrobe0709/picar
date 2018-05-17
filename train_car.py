from Train import Train

def main():
    """Main interface"""
    train = Train()
    training = True
    while training:
        train.get_current_direction()
        train.speed_sensor.set_pulse(0)
        if train.current_direction == 'forward':
            train.speed_sensor.forward(train.current_distance)
        elif train.current_direction == 'reverse':
            train.speed_sensor.reverse(train.current_distance)
        elif train.current_direction == 'left':
            train.speed_sensor.left()
        elif train.current_direction == 'right':
            train.speed_sensor.right()
        elif train.current_direction == 'quit':
            train.speed_sensor.cleanup()
            training = False
    train.save_path_to_json()

if __name__ == '__main__':
    main()