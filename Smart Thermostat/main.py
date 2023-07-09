'''
In this code, the DHT22 sensor is connected to pin GP13, the relay is connected to pin GP14, and the neopixel is connected to pin GP0. The code reads the temperature and humidity values from the DHT22 sensor and checks if the temperature is below or above the target temperature. If the temperature is below the target temperature, the code activates the relay to activate the heating system and sets the neopixel to red to indicate that the heating system is activated. If the temperature is above the target temperature, the code deactivates the relay to deactivate the heating system and sets the neopixel to blue to indicate that the cooling system is activated. If the temperature is at the target temperature, the code deactivates the relay and sets the neopixel to green to indicate that the temperature is at the target value. The code loops continuously, checking the temperature and humidity values every 2 seconds and updating the relay and neopixel accordingly. Note that you may need to adjust the target temperature and humidity values to suit your preferences.
'''

import dht
import machine
import neopixel
import time

# Set up the DHT22 sensor on pin GP13
dht_pin = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
dht_sensor = dht.DHT22(dht_pin)

# Set up the relay on pin GP14
relay_pin = machine.Pin(14, machine.Pin.OUT)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set the target temperature and humidity values
target_temperature = 25  # in degrees Celsius
target_humidity = 50  # in percentage

# Main loop
while True:
    # Read the temperature and humidity values from the DHT22 sensor
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

    # Check if the temperature is below or above the target temperature and activate the relay accordingly
    if temperature < target_temperature:
        relay_pin.value(1)  # Turn on the relay to activate the heating system
        pixels[0] = (255, 0, 0)  # Red for heating system activated
    elif temperature > target_temperature:
        # Turn off the relay to deactivate the heating system
        relay_pin.value(0)
        pixels[0] = (0, 0, 255)  # Blue for cooling system activated
    else:
        # Turn off the relay if the temperature is at the target temperature
        relay_pin.value(0)
        pixels[0] = (0, 255, 0)  # Green for temperature at target value

    # Wait for 2 seconds before checking the temperature and humidity values again
    time.sleep(2)
