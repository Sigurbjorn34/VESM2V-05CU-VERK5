from machine import Pin

# Define pins for the Green LEDs
led1_green = Pin(5, Pin.OUT)  # Green for LED 1
led2_green = Pin(2, Pin.OUT)  # Green for LED 2

# Turn on green LEDs (common cathode: LOW = ON)
led1_green.value(1)  # LED 1 Green ON
led2_green.value(1)  # LED 2 Green ON

