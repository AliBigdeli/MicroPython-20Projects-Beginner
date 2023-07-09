'''
In this code, the gas detection sensor is connected to pin GP26, the buzzer is connected to pin GP15, and the neopixel is connected to pin GP0. The code checks if smoke is detected using the gas detection sensor and updates the neopixel to indicate whether the alarm has been activated or not, with red indicating that the alarm has been activated. If smoke is detected, the code sounds the buzzer for 5 seconds. The code loops continuously, checking if smoke is detected every 0.1 seconds.
'''

import machine
import neopixel
import time

# Set up the gas detection sensor on pin GP26
gas_sensor_pin = machine.Pin(26, machine.Pin.IN)

# Set up the buzzer on pin GP15
buzzer_pin = machine.Pin(15, machine.Pin.OUT)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Main loop
while True:
    # Check if smoke is detected using the gas detection sensor
    if gas_sensor_pin.value() == 0:
        pixels[0] = (255, 0, 0) # Red for alarm activated
        buzzer_pin.value(1) # Turn on the buzzer

        # Wait for 5 seconds to sound the alarm
        time.sleep(5)

        buzzer_pin.value(0) # Turn off the buzzer
        pixels[0] = (0, 0, 0) # Turn off the neopixel
    else:
        pixels[0] = (0, 0, 0) # Turn off the neopixel

    time.sleep(0.1)