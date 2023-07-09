'''
In this code, the DHT22 sensor is connected to pin GP22, the photocell sensor is connected to pin GP26, and the neopixel is connected to pin GP0. The code reads the temperature and humidity levels from the DHT22 sensor and the light level from the photocell sensor. If the light level, temperature, or humidity is above the threshold value, the code sets the neopixel to red to indicate high energy usage. If the light level, temperature, and humidity are below the threshold value, the code sets the neopixel to green to indicate normal energy usage. The code loops continuously, checking the sensors every 5 seconds and updating the neopixel accordingly. Note that you may need to adjust the threshold light level, temperature, and humidity values and the time interval for checking the sensors to suit your energy monitoring needs
'''

import machine
import neopixel
import time
import dht

# Set up the DHT22 sensor on pin GP22
dht_pin = machine.Pin(22, machine.Pin.IN)

# Set up the photocell sensor on pin GP26
photo_pin = machine.Pin(26, machine.Pin.IN)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set the threshold value for indicating high energy usage
threshold_light_level = 500
threshold_temperature = 25.0
threshold_humidity = 60.0

# Set the time interval for checking the sensors
check_interval = 5  # in seconds

# Main loop
while True:
    # Read the temperature and humidity levels from the DHT22 sensor
    d = dht.DHT22(machine.Pin(22))
    d.measure()
    temperature = d.temperature()
    humidity = d.humidity()

    # Read the light level from the photocell sensor
    light_level = photo_pin.read()

    # Check if the light level, temperature, or humidity is above the threshold value and indicate high energy usage accordingly
    if light_level > threshold_light_level or temperature > threshold_temperature or humidity > threshold_humidity:
        pixels[0] = (255, 0, 0)  # Red for high energy usage
    else:
        pixels[0] = (0, 255, 0)  # Green for normal energy usage

    # Wait for the specified time interval before checking the sensors again
    time.sleep(check_interval)
