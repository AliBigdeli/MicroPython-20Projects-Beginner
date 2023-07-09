'''
In this updated code, the ultrasonic sensor is connected to pins GP16 (trigger) and GP17 (echo), and the neopixel is connected to pin GP0. The code triggers the ultrasonic sensor to send out a pulse and calculates the distance based on the time it took for the echo to return. The code maps the distance value to a value between 0 and 255 for the neopixel and sets the color of the neopixel based on the distance value, with red indicating that the parking spot is occupied and green indicating that the parking spot is available. The code loops continuously, updating the neopixel every 0.1 seconds and checking the distance value to detect the presence of a car. You can place the neopixel in a visible location near the parking spot to indicate whether it is occupied or not.
'''

import machine
import neopixel
import utime

# Set up the ultrasonic sensor on pins GP16 (trigger) and GP17 (echo)
trigger_pin = machine.Pin(16, machine.Pin.OUT)
echo_pin = machine.Pin(17, machine.Pin.IN)

# Set up the neopixel on pin GP0
neopixel_pin = machine.Pin(0)
num_pixels = 1
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels)

# Set the minimum and maximum distance values for detecting a car
min_distance = 5  # in centimeters
max_distance = 50  # in centimeters

# Main loop
while True:
    # Trigger the ultrasonic sensor to send out a pulse
    trigger_pin.value(1)
    utime.sleep_us(10)
    trigger_pin.value(0)

    # Wait for the echo signal and calculate the distance based on the time it took for the echo to return
    pulse_start_time = utime.ticks_us()
    while echo_pin.value() == 0:
        pulse_start_time = utime.ticks_us()
    while echo_pin.value() == 1:
        pulse_end_time = utime.ticks_us()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = pulse_duration / 58

    # Map the distance value to a value between 0 and 255 for the neopixel
    neopixel_value = int(machine.map(
        distance, min_distance, max_distance, 0, 255))

    # Set the color of the neopixel based on the distance value
    if distance < max_distance:
        pixels[0] = (255, 0, 0)  # Red for parking spot occupied
    else:
        pixels[0] = (0, 255, 0)  # Green for parking spot available

    utime.sleep(0.1)
