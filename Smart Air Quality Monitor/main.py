'''
Smart Air Quality Monitor: Use a gas detection sensor to measure air quality,
use a neopixel to indicate the air quality level, and send alerts to you
when air quality is poor.
'''
import machine
import neopixel
import time

# Set up the gas detection sensor on pin GP26
gas_pin = machine.Pin(26, machine.Pin.IN)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set up the buzzer on pin GP15
buzzer_pin = machine.Pin(15, machine.Pin.OUT)

# Set the gas threshold for indicating poor air quality
gas_threshold = 500  # in ppm

# Main loop
while True:
    # Read the gas sensor value
    gas_value = gas_pin.read_u16()

    # Map the gas value to a value between 0 and 255 for the neopixel
    neopixel_value = int(machine.map(gas_value, 0, 65535, 0, 255))

    # Set the color of the neopixel based on the gas value
    if gas_value < gas_threshold:
        pixels[0] = (0, 255, 0)  # Green for good air quality
        buzzer_pin.value(0)  # Turn off the buzzer
    else:
        pixels[0] = (255, 0, 0)  # Red for poor air quality
        buzzer_pin.value(1)  # Turn on the buzzer

    # Update the neopixel
    pixels[0] = (neopixel_value, 0, 0)

    time.sleep(0.1)

'''
In this code, the gas detection sensor is connected to pin GP26, the neopixel is connected
to pin GP0, and the buzzer is connected to pin GP15. The code reads the gas sensor value and 
maps it to a value between 0 and 255 for the neopixel. The code sets the color of the neopixel
based on the gas value, with green indicating good air quality and red indicating poor air quality.
If the air quality is poor (i.e., the gas value is greater than the threshold value gas_threshold),
the code turns on the buzzer to indicate that the air quality is poor. The code loops continuously,
updating the neopixel every 0.1 seconds and checking the gas value.
'''
