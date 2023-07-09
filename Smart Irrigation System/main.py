'''
In this code, the soil moisture sensor is connected to analog pin GP26, the relay is connected to pin GP16, and the neopixel is connected to pin GP0. The code reads the soil moisture value from the sensor and maps it to a value between 0 and 255 for the neopixel. The code sets the color of the neopixel based on the soil moisture value, with green indicating good levels and red indicating low levels. If the soil moisture level is low (i.e., below the threshold value soil_moisture_threshold), the code turns on the relay to activate the irrigation system. The code loops continuously, updating the neopixel every second and checking the soil moisture level.
'''


import machine
import neopixel
import time

# Set up the soil moisture sensor on analog pin GP26
soil_moisture_pin = machine.ADC(26)

# Set up the relay on pin GP16
relay_pin = machine.Pin(16, machine.Pin.OUT)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set the soil moisture threshold for activating the irrigation system
soil_moisture_threshold = 500  # adjust this value to suit your needs

# Main loop
while True:
    # Read the soil moisture value from the sensor
    soil_moisture_value = soil_moisture_pin.read_u16()

    # Map the soil moisture value to a value between 0 and 255 for the neopixel
    neopixel_value = int(machine.map(soil_moisture_value, 0, 65535, 0, 255))

    # Set the color of the neopixel based on the soil moisture value
    if soil_moisture_value < soil_moisture_threshold:
        pixels[0] = (0, 255, 0)  # Green for good soil moisture levels
        relay_pin.value(0)  # Turn off the relay
    else:
        pixels[0] = (255, 0, 0)  # Red for low soil moisture levels
        relay_pin.value(1)  # Turn on the relay

    # Update the neopixel
    pixels[0] = (neopixel_value, 0, 0)

    time.sleep(1)
