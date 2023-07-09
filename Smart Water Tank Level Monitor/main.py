'''
In this code, the PIR sensor is connected to pin GP26, the neopixel is connected to pin GP0, and the buzzer is connected to pin GP15. The code checks if someone is at the door using the PIR sensor and updates the neopixel to indicate whether the doorbell has been activated or not, with red indicating that the doorbell has been activated. If someone is at the door, the code sounds the buzzer for 1 second. The code loops continuously, checking if someone is at the door every 0.1 seconds.
'''

import machine
import neopixel
import time

# Set up the PIR sensor on pin GP26
pir_pin = machine.Pin(26, machine.Pin.IN)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set up the buzzer on pin GP15
buzzer_pin = machine.Pin(15, machine.Pin.OUT)

# Main loop
while True:
    # Check if someone is at the door using the PIR sensor
    if pir_pin.value() == 1:
        pixels[0] = (255, 0, 0) # Red for doorbell activated
        buzzer_pin.value(1) # Turn on the buzzer

        # Wait for 1 second to sound the buzzer
        time.sleep(1)

        buzzer_pin.value(0) # Turn off the buzzer
        pixels[0] = (0, 0, 0) # Turn off the neopixel
    else:
        pixels[0] = (0, 0, 0) # Turn off the neopixel

    time.sleep(0.1)