'''
In this code, the DHT22 sensor is connected to pin GP14, the neopixel is connected to pin GP0, and the buzzer is connected to pin GP15. The code reads the temperature and humidity values from the DHT22 sensor and maps them to a value between 0 and 255 for the neopixel. The code sets the color of the neopixel based on the temperature and humidity values, with green indicating good levels and red indicating poor levels. If the temperature or humidity levels are poor (i.e., below the threshold values temp_threshold and humidity_threshold), the code turns on the buzzer to indicate that the levels are poor. The code loops continuously, updating the neopixel every second and checking the temperature and humidity levels.
'''

import machine
import neopixel
import dht
import time

# Set up the DHT22 sensor on pin GP14
dht_pin = machine.Pin(14)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set up the buzzer on pin GP15
buzzer_pin = machine.Pin(15, machine.Pin.OUT)

# Set the temperature and humidity thresholds for indicating poor levels
temp_threshold = 25 # in Celsius
humidity_threshold = 60 # in percentage

# Main loop
while True:
    # Read the temperature and humidity values from the DHT22 sensor
    dht_sensor = dht.DHT22(dht_pin)
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

    # Map the temperature and humidity values to a value between 0 and 255 for the neopixel
    temp_neopixel_value = int(machine.map(temperature, 0, 40, 0, 255))
    humidity_neopixel_value = int(machine.map(humidity, 0, 100, 0, 255))

    # Set the color of the neopixel based on the temperature and humidity values
    if temperature < temp_threshold and humidity < humidity_threshold:
        pixels[0] = (0, 255, 0) # Green for good temperature and humidity levels
        buzzer_pin.value(0) # Turn off the buzzer
    else:
        pixels[0] = (255, 0, 0) # Red for poor temperature and humidity levels
        buzzer_pin.value(1) # Turn on the buzzer

    # Update the neopixel
    pixels[0] = (temp_neopixel_value, humidity_neopixel_value, 0)

    time.sleep(1)
    
    