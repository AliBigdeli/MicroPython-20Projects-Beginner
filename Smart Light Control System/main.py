'''
In this code, the photocell sensor is connected to pin GP26, the relay is connected
to pin GP16, and the neopixel is connected to pin GP0. The code reads the light level
from the photocell sensor and maps it to a value between 0 and 255 for the neopixel. 
The code turns on/off the lights based on the light level, with the light turning on if
the light level is less than the threshold value light_threshold. The code updates the
neopixel to indicate whether the lights are on or off. The code loops continuously, updating
the neopixel every 0.1 seconds and checking the light level.
'''

import machine
import neopixel
import time

# Set up the photocell sensor on pin GP26
photocell_pin = machine.Pin(26, machine.Pin.IN)

# Set up the relay on pin GP16
relay_pin = machine.Pin(16, machine.Pin.OUT)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set the light threshold for turning on/off the lights
light_threshold = 500 # in ADC units

# Main loop
while True:
    # Read the light level from the photocell sensor
    light_level = photocell_pin.read_u16()

    # Map the light level to a value between 0 and 255 for the neopixel
    neopixel_value = int(machine.map(light_level, 0, 65535, 0, 255))

    # Turn on/off the lights based on the light level
    if light_level < light_threshold:
        relay_pin.value(1) # Turn on the lights
        pixels[0] = (0, 255, 0) # Green for lights on
    else:
        relay_pin.value(0) # Turn off the lights
        pixels[0] = (255, 0, 0) # Red for lights off

    # Update the neopixel
    pixels[0] = (neopixel_value, 0, 0)

    time.sleep(0.1)