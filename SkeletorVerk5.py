from machine import Pin, PWM
import math
import time
import random

# Servo class definition (from provided code)
class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.pwm = PWM(pin, freq=freq, duty=0)

    def write_us(self, us):
        if us == 0:
            self.pwm.duty(0)
            return
        us = min(self.max_us, max(self.min_us, us))
        duty = us * 1024 * self.freq // 1000000
        self.pwm.duty(duty)

    def write_angle(self, degrees=None, radians=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)

# Initialize servos for the motors on specific pins
neck1 = Servo(Pin(11))
neck2 = Servo(Pin(13))
jaw = Servo(Pin(12))
lefthand = Servo(Pin(14))
righthand = Servo(Pin(10))

def random_slow_movements():
    while True:
        # Generate random angles for all motors
 #       angle1 = random.randint(0, 180)  # Neck motor 1 angle
 #       angle2 = random.randint(0, 180)  # Neck motor 2 angle
        angle3 = random.randint(0, 180)  # Jaw motor angle
        angle4 = random.randint(0, 180)  # Left hand motor angle
        angle5 = random.randint(0, 180)  # Right hand motor angle

        duration = random.uniform(1, 3)  # Random duration in seconds

        # Move motors to random angles
       # neck1.write_angle(angle1)
        #neck2.write_angle(angle2)
        jaw.write_angle(angle3)
        lefthand.write_angle(angle4)
        righthand.write_angle(angle5)

        #print(f"neck1 -> Angle: {angle1}, neck2 -> Angle: {angle2}, jaw -> Angle: {angle3}, lefthand -> Angle: {angle4}, righthand -> Angle: {angle5}")

        # Wait for the duration
        time.sleep(duration)

        # Optionally stop motors for a moment
        neck1.write_us(0)  # Disable neck motor 1
        neck2.write_us(0)  # Disable neck motor 2
        jaw.write_us(0)    # Disable jaw motor
        lefthand.write_us(0)  # Disable left hand motor
        righthand.write_us(0)  # Disable right hand motor

        time.sleep(0.5)

# Run the random movement function
try:
    random_slow_movements()
except KeyboardInterrupt:
    print("Stopping all motors...")
    #neck1.write_us(0)
    #neck2.write_us(0)
    jaw.write_us(0)
    lefthand.write_us(0)
    righthand.write_us(0)


# Define pins for the Green LEDs
led1_green = Pin(5, Pin.OUT)  # Green for LED 1
led2_green = Pin(2, Pin.OUT)  # Green for LED 2

# Turn on green LEDs (common cathode: LOW = ON)
led1_green.value(1)  # LED 1 Green ON
led2_green.value(1)  # LED 2 Green ON
