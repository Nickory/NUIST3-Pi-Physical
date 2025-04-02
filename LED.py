
# Import the RPi.GPIO library to control the Raspberry Pi GPIO pins
import RPi.GPIO as GPIO
# Import the time library for adding delays
import time

# Set the GPIO numbering mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)
# Disable GPIO warnings to avoid runtime messages
GPIO.setwarnings(False)
# Set GPIO pin 18 as an output pin
GPIO.setup(18, GPIO.OUT)

# Print message to console
print("LED on")
# Set GPIO pin 18 to HIGH (3.3V) to turn the LED on
GPIO.output(18, GPIO.HIGH)
# Wait for 1 second
time.sleep(1)

# Print message to console
print("LED off")
# Set GPIO pin 18 to LOW (0V) to turn the LED off

GPIO.output(18, GPIO.LOW)
