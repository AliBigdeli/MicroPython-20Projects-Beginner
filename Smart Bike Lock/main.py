'''
In this code, the PIR sensor is connected to pin GP13, the neopixel is connected to pin GP0, and the buzzer is connected to pin GP14. The code checks the PIR sensor for a specified time interval and counts the number of times it detects motion. If the PIR count is above the threshold value, the code sets the neopixel to red to indicate that the alarm is activated and turns on the buzzer to activate the alarm. If the PIR count is below the threshold value, the code sets the neopixel to green to indicate that the alarm is not activated and turns off the buzzer. The code loops continuously, checking the PIR sensor every second and updating the neopixel and buzzer accordingly. Note that you may need to adjust the threshold PIR count and the time interval for checking the PIR sensor to suit your bike lock setup.
'''

import machine
import neopixel
import time

# Set up the PIR sensor on pin GP13
pir_pin = machine.Pin(13, machine.Pin.IN)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set up the buzzer on pin GP14
buzzer_pin = machine.Pin(14, machine.Pin.OUT)

# Set the threshold value for indicating that someone is attempting to unlock the bike
threshold_pir_count = 5

# Set the time interval for checking the PIR sensor
check_interval = 1 # in seconds

# Main loop
while True:
    # Initialize the PIR count to 0
    pir_count = 0

    # Check the PIR sensor for the specified time interval and count the number of times it detects motion
    for i in range(check_interval):
        if pir_pin.value() == 1:
            pir_count += 1
        time.sleep(1)

    # Check if the PIR count is above the threshold value and activate the alarm accordingly
    if pir_count >= threshold_pir_count:
        pixels[0] = (255, 0, 0) # Red for alarm activated
        buzzer_pin.on() # Turn on the buzzer to activate the alarm
    else:
        pixels[0] = (0, 255, 0) # Green for alarm not activated
        buzzer_pin.off() # Turn off the buzzer

    # Wait for 1 second before checking the PIR sensor again
    time.sleep(1)