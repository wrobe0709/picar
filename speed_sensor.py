import RPi.GPIO as GPIO
import signal
import time
import math

class SpeedSensor():
    def __init__(self):
        self.in_pin = ''
        self.pulse = ''
        self.start_timer = ''
        self.elapse = ''
        self.rpm = ''
        self.dist_km = ''
        self.dist_m = ''
        self.dist_meas = ''
        self.km_per_sec = ''
        self.km_per_hour = ''
        self.m_per_sec = ''
        self.rotations = ''
        self.radius = ''
        self.interrupt = False

    def set_rpm(self, rpm):
        """Set rpm"""
        self.rpm = rpm

    def set_dist_km(self, dist_km):
        """Set distance in km"""
        self.dist_km = dist_km

    def set_dist_m(self, dist_m):
        """Set distance in km"""
        self.dist_m = dist_m

    def set_dist_meas(self, dist_meas):
        """Set distance measured"""
        self.dist_meas = dist_meas

    def set_km_per_sec(self, km_per_sec):
        """Set km per second"""
        self.km_per_sec = km_per_sec

    def set_km_per_hour(self, km_per_hour):
        """Set km per hour"""
        self.km_per_hour = km_per_hour

    def set_m_per_sec(self, m_per_sec):
        """Set km per second"""
        self.m_per_sec = m_per_sec

    def set_in_pin(self, in_pin):
        """Set in pin"""
        self.in_pin = in_pin

    def set_pulse(self, pulse):
        """Set pulse"""
        self.pulse = pulse

    def set_start_timer(self):
        """Set start timer"""
        self.start_timer = time.time()

    def set_elapse(self, elapse):
        """Set elapse"""
        self.elapse = elapse

    def set_rotations(self, rotations):
        """Set rotations"""
        self.rotations = rotations

    def set_radius(self, radius):
        """Set radius"""
        self.radius = radius

    def set_circumference(self, circumference):
        """Set circumference"""
        self.circumference = circumference  

    def speed_init(self):
        """Initialize GPIO"""
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.in_pin, GPIO.IN)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)

    def init_interrupt(self):
        """Initialize interrupt"""
        GPIO.add_event_detect(self.in_pin, GPIO.RISING, callback=self.calculate_elapse, bouncetime=20)

    def calculate_elapse(self, channel):
        self.pulse += 1

    def calculate_speed(self):
        """Calculate speed"""
        if self.pulse > 0:
            print(self.pulse)

    def signal_handler(self, signal, frame):
        """Handle signals"""
        self.interrupt = True

def forward(speed_sensor, distance_cm):
    """Drive car forward"""
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(7, GPIO.HIGH)

    while speed_sensor.pulse / float(20) * speed_sensor.circumference < float(distance_cm):
        if speed_sensor.interrupt:
            break
        time.sleep(.1)
    
    GPIO.output(15, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)

def reverse(speed_sensor, distance_cm):
    """Drive car in reverse"""
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)

    while speed_sensor.pulse / float(20) * speed_sensor.circumference < float(distance_cm):
        if speed_sensor.interrupt:
            break
        time.sleep(.1)
    
    GPIO.output(13, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)

def left():
    """Drive car left"""
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(.15)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)

def right():
    """Drive car right"""
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(.15)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)

def init():
    """Initialize car for driving"""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

def cleanup():
    """Clean up"""
    GPIO.cleanup()

