'''
In this code, the ultrasonic sensor is connected to pins GP14 (trigger) and GP15 (echo),
the relay is connected to pin GP16, and the neopixel is connected to pin GP0.
The code calculates the distance from the ultrasonic sensor using the measure_distance()
function. If a car is approaching the garage door (i.e., the distance is less than the threshold
value distance_threshold), the code turns on the relay to open the door for 5 seconds and turns on
the neopixel to indicate that the door is open. The code loops continuously, measuring the distance every 0.1 seconds.
'''

import machine
import neopixel
import time

# Set up the ultrasonic sensor on pins GP14 (trigger) and GP15 (echo)
trigger_pin = machine.Pin(14, machine.Pin.OUT)
echo_pin = machine.Pin(15, machine.Pin.IN)

# Set up the relay on pin GP16
relay_pin = machine.Pin(16, machine.Pin.OUT)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set the distance threshold for opening the garage door
distance_threshold = 20  # in centimeters

# Function to calculate distance from the ultrasonic sensor


def measure_distance():
    # Send a 10 microsecond pulse to the trigger pin
    trigger_pin.value(1)
    time.sleep_us(10)
    trigger_pin.value(0)

    # Measure the pulse duration on the echo pin
    pulse_duration = machine.time_pulse_us(echo_pin, 1, 10000)

    # Calculate the distance in centimeters
    distance = pulse_duration / 58.0

    return distance


# Main loop
while True:
    # Measure the distance from the ultrasonic sensor
    distance = measure_distance()

    # Open the garage door if a car is approaching
    if distance < distance_threshold:
        relay_pin.value(1)
        # Turn on the neopixel to indicate the door is open
        pixels[0] = (0, 255, 0)
        time.sleep(5)  # Keep the door open for 5 seconds
        relay_pin.value(0)
        pixels[0] = (0, 0, 0)  # Turn off the neopixel

    time.sleep(0.1)


