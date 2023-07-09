'''
In this code, the PIR sensor is connected to pin GP20, the buzzer is connected to pin GP15,
and the neopixel is connected to pin GP0. The code checks for motion using the PIR sensor.
If motion is detected, the code turns on the buzzer to activate the alarm and turns on the
neopixel to indicate that the alarm is activated. The code waits for 5 seconds and then 
turns off the buzzer and neopixel. The code loops continuously, checking for motion every 0.1 seconds.
'''

import machine
import neopixel
import time

# Set up the PIR sensor on pin GP20
pir_pin = machine.Pin(20, machine.Pin.IN)

# Set up the buzzer on pin GP15
buzzer_pin = machine.Pin(15, machine.Pin.OUT)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Main loop
while True:
    # Check for motion using the PIR sensor
    if pir_pin.value() == 1:
        # Turn on the buzzer to activate the alarm
        buzzer_pin.value(1)

        # Turn on the neopixel to indicate the alarm is activated
        pixels[0] = (255, 0, 0)

        # Wait for 5 seconds
        time.sleep(5)

        # Turn off the buzzer and neopixel
        buzzer_pin.value(0)
        pixels[0] = (0, 0, 0)

    time.sleep(0.1)

