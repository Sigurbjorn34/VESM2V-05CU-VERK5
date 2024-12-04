import machine
import neopixel
import time

# Configuration
LED_PINS = [11, 12]  # GPIO pins for the two LED strips
NUM_LEDS = 8  # Number of LEDs in each strip

# Initialize the NeoPixel objects
strips = [neopixel.NeoPixel(machine.Pin(pin), NUM_LEDS) for pin in LED_PINS]

def set_color_all(color):
    """Set all LEDs on all strips to a specific color."""
    for strip in strips:
        for i in range(NUM_LEDS):
            strip[i] = color
        strip.write()

def color_chase_all(color, delay):
    """Chase a color across all strips."""
    for i in range(NUM_LEDS):
        for strip in strips:
            strip[i] = color
            strip.write()
        time.sleep(delay)
        for strip in strips:
            strip[i] = (0, 0, 0)  # Turn off the LED
            strip.write()

# Example usage
try:
    while True:
        # Set all LEDs to red
        set_color_all((255, 0, 50))  # Red
        time.sleep(1)

        # Set all LEDs to green
        set_color_all((127, 0, 25))  # Green
        time.sleep(1)

        # Chase blue across the LEDs
        color_chase_all((255, 0, 100), 0.1)  # Blue chase
        time.sleep(1)

except KeyboardInterrupt:
    # Turn off all LEDs on exit
    set_color_all((0, 0, 0))

