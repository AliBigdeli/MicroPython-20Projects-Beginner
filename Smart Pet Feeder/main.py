'''
In this code, the PIR sensor is connected to pin GP26, the relay is connected to pin GP16, and the neopixel is connected to pin GP0. The code checks if the pet is nearby using the PIR sensor and dispenses food using the relay if the pet is detected. The code waits for 5 seconds to allow the pet to eat and then stops dispensing food using the relay. The code updates the neopixel to indicate whether food has been dispensed or not, with green indicating that food has been dispensed, red indicating that food has not been dispensed, and blue indicating that the pet is not nearby. The code loops continuously, checking if the pet is nearby every 0.1 seconds.
'''

import machine
import neopixel
import time

# Set up the PIR sensor on pin GP26
pir_pin = machine.Pin(26, machine.Pin.IN)

# Set up the relay on pin GP16
relay_pin = machine.Pin(16, machine.Pin.OUT)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Main loop
while True:
    # Check if the pet is nearby using the PIR sensor
    if pir_pin.value() == 1:
        # Dispense food using the relay
        relay_pin.value(1)
        pixels[0] = (0, 255, 0) # Green for food dispensed

        # Wait for 5 seconds to allow the pet to eat
        time.sleep(5)

        # Stop dispensing food using the relay
        relay_pin.value(0)
        pixels[0] = (255, 0, 0) # Red for food not dispensed
    else:
        pixels[0] = (0, 0, 255) # Blue for pet not nearby

    time.sleep(0.1)