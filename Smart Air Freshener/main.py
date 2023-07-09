'''
In this code, the gas detection sensor is connected to pin GP26, the relay is connected to pin GP14, and the neopixel is connected to pin GP0. The code reads the gas level and checks if it is above the threshold value. If the gas level is above the threshold value, the code sets the neopixel to blue to indicate that the air freshener is activated and activates the relay to activate the air freshener. If the gas level is below the threshold value, the code sets the neopixel to green to indicate that the air freshener is not activated and deactivates the relay to deactivate the air freshener. The code loops continuously, checking the gas level every 5 seconds and updating the neopixel and relay accordingly. Note that you may need to adjust the threshold gas level and the time interval for checking the gas level to suit your air freshener setup.
'''

import machine
import neopixel
import time

# Set up the gas detection sensor on pin GP26
gas_pin = machine.Pin(26, machine.Pin.IN)

# Set up the relay on pin GP14
relay_pin = machine.Pin(14, machine.Pin.OUT)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set the threshold value for activating the air freshener
threshold_gas_level = 500

# Set the time interval for checking the gas level
check_interval = 5 # in seconds

# Main loop
while True:
    # Read the gas level
    gas_level = gas_pin.read()

    # Check if the gas level is above the threshold value and activate the air freshener accordingly
    if gas_level > threshold_gas_level:
        pixels[0] = (0, 0, 255) # Blue for air freshener activated
        relay_pin.on() # Activate the air freshener
    else:
        pixels[0] = (0, 255, 0) # Green for air freshener not activated
        relay_pin.off() # Deactivate the air freshener

    # Wait for the specified time interval before checking the gas level again
    time.sleep(check_interval)