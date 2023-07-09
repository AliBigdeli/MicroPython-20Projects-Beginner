
"""
In this code, the soil moisture sensor is connected to pin GP26, the relay is connected to pin GP14,
and the neopixel is connected to pin GP0. The code reads the soil moisture sensor value and compares it
to a threshold value (watering_threshold). If the soil moisture level is below the threshold,
the code turns on the relay to activate the water pump for 5 seconds and turns on the neopixel to
indicate that the plant has been watered. The neopixel is turned off after watering.
The code loops continuously, checking the soil moisture level every second.
"""

import machine
import time
import neopixel

# Set up the soil moisture sensor on pin GP26
sensor_pin = machine.Pin(26, machine.Pin.IN)

# Set up the relay on pin GP14
relay_pin = machine.Pin(14, machine.Pin.OUT)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set the threshold for watering the plant based on soil moisture level
watering_threshold = 500

# Main loop
while True:
    # Read the soil moisture sensor value
    soil_moisture = sensor_pin.read_u16()

    # Turn on the water pump if soil moisture level is below the threshold
    if soil_moisture < watering_threshold:
        relay_pin.value(1)
        pixels[0] = (0, 255, 0)  # Turn on the neopixel to indicate watering
        time.sleep(5)  # Water for 5 seconds
        relay_pin.value(0)
        pixels[0] = (0, 0, 0)  # Turn off the neopixel

    time.sleep(1)
