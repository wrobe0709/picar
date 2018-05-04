import speed_sensor

class Train():
    """Train robot to follow route"""

    def __init__(self):
        """Constructor"""
        self.current_direction = ''
        self.current_distance = ''

    def get_current_direction(self):
        """Get current direction from user"""
        self.current_direction = input("Which way? > ")
        self.current_distance = input("How far (cm)? > ")

    def drive(self):
        """Drive"""
        speed_sensor.main(self.current_distance)

    
if __name__ == '__main__':
    train = Train()
    train.get_current_direction()
    train.drive()