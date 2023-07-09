'''
In this code, the soil moisture sensor is connected to pin GP13, the relay is connected to pin GP14, and the neopixel is connected to pin GP0. The code reads the moisture value from the soil moisture sensor and checks if the moisture level is below the threshold value. If the moisture level is below the threshold value, the code activates the relay to activate the water pump and sets the neopixel to blue to indicate that the water pump is activated. If the moisture level is above the threshold value, the code deactivates the relay to deactivate the water pump and sets the neopixel to green to indicate that the water pump is deactivated. The code also checks if it's time to indicate that the water has been changed and sets the neopixel to red accordingly. The code loops continuously, checking the moisture level and updating the relay and neopixel accordingly, and checking the time interval for indicating that the water has been changed. Note that you may need to adjust the threshold moisture value and the time intervals to suit your aquarium setup.
'''

import machine
import neopixel
import time

# Set up the soil moisture sensor on pin GP13
moisture_pin = machine.Pin(13, machine.Pin.IN)

# Set up the relay on pin GP14
relay_pin = machine.Pin(14, machine.Pin.OUT)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set the threshold moisture value for activating the water pump
threshold_moisture = 500

# Set the time interval for checking the moisture level
check_interval = 60  # in seconds

# Set the time interval for indicating that the water has been changed
water_changed_interval = 24 * 60 * 60  # in seconds (1 day)

# Set the initial time for indicating that the water has been changed
water_changed_time = time.time()

# Main loop
while True:
    # Read the moisture value from the soil moisture sensor
    moisture = moisture_pin.read_u16()

    # Check if the moisture level is below the threshold value and activate the relay accordingly
    if moisture < threshold_moisture:
        relay_pin.value(1)  # Turn on the relay to activate the water pump
        pixels[0] = (0, 0, 255)  # Blue for water pump activated
    else:
        # Turn off the relay if the moisture level is above the threshold value
        relay_pin.value(0)
        pixels[0] = (0, 255, 0)  # Green for water pump deactivated

    # Check if it's time to indicate that the water has been changed and set the neopixel to red accordingly
    if time.time() - water_changed_time >= water_changed_interval:
        pixels[0] = (255, 0, 0)  # Red for water changed

        # Update the time for indicating that the water has been changed
        water_changed_time = time.time()

    # Wait for the check interval before checking the moisture level again
    time.sleep(check_interval)
