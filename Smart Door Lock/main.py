'''
In this code, the PIR sensor is connected to pin GP13, the relay is connected to pin GP14, and the neopixel is connected to pin GP0. The code checks the PIR sensor for a specified time interval and counts the number of times it detects motion. If the PIR count is above the threshold value, the code checks the current state of the lock and unlocks the door if it is locked or locks the door if it is unlocked. The code sets the neopixel to green to indicate that the door is unlocked or to red to indicate that the door is locked, and updates the state of the lock accordingly. The code loops continuously, checking the PIR sensor every second and updating the neopixel and relay accordingly. Note that you may need to adjust the threshold PIR count and the time interval for checking the PIR sensor to suit your door lock setup.
'''

import machine
import neopixel
import time

# Set up the PIR sensor on pin GP13
pir_pin = machine.Pin(13, machine.Pin.IN)

# Set up the relay on pin GP14
relay_pin = machine.Pin(14, machine.Pin.OUT)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set the threshold value for detecting someone approaching the door
threshold_pir_count = 5

# Set the time interval for checking the PIR sensor
check_interval = 1 # in seconds

# Set the initial state of the lock
locked = True

# Set the color of the neopixel to indicate the initial state of the lock
if locked:
    pixels[0] = (255, 0, 0) # Red for locked
else:
    pixels[0] = (0, 255, 0) # Green for unlocked

# Main loop
while True:
    # Initialize the PIR count to 0
    pir_count = 0

    # Check the PIR sensor for the specified time interval and count the number of times it detects motion
    for i in range(check_interval):
        if pir_pin.value() == 1:
            pir_count += 1
        time.sleep(1)

    # Check if the PIR count is above the threshold value and unlock the door accordingly
    if pir_count >= threshold_pir_count:
        if locked:
            pixels[0] = (0, 255, 0) # Green for unlocked
            relay_pin.on() # Unlock the door
            locked = False
        else:
            pixels[0] = (255, 0, 0) # Red for locked
            relay_pin.off() # Lock the door
            locked = True

    # Wait for 1 second before checking the PIR sensor again
    time.sleep(1)