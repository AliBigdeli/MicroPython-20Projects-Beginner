'''
In this code, the soil moisture sensor is connected to pin GP26, the relay is connected to pin GP14, and the neopixel is connected to pin GP0. The code reads the soil moisture level and checks if it is below the threshold value. If the moisture level is below the threshold value, the code sets the neopixel to blue to indicate that the watering system is activated and activates the relay to activate the watering system. If the moisture level is above the threshold value, the code sets the neopixel to green to indicate that the watering system is not activated and deactivates the relay to deactivate the watering system. The code loops continuously, checking the soil moisture level every 5 seconds and updating the neopixel and relay accordingly. Note that you may need to adjust the threshold moisture level and the time interval for checking the soil moisture level to suit your greenhouse setup.
'''

import machine
import neopixel
import time

# Set up the soil moisture sensor on pin GP26
moisture_pin = machine.Pin(26, machine.Pin.IN)

# Set up the relay on pin GP14
relay_pin = machine.Pin(14, machine.Pin.OUT)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set the threshold value for activating the watering system
threshold_moisture_level = 500

# Set the time interval for checking the soil moisture level
check_interval = 5 # in seconds

# Main loop
while True:
    # Read the soil moisture level
    moisture_level = moisture_pin.read()

    # Check if the moisture level is below the threshold value and activate the watering system accordingly
    if moisture_level < threshold_moisture_level:
        pixels[0] = (0, 0, 255) # Blue for watering system activated
        relay_pin.on() # Activate the watering system
    else:
        pixels[0] = (0, 255, 0) # Green for watering system not activated
        relay_pin.off() # Deactivate the watering system

    # Wait for the specified time interval before checking the soil moisture level again
    time.sleep(check_interval)