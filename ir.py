import RPi.GPIO as GPIO
import time

# Replace with the actual GPIO pin connected to the IR transmitter
ir_transmitter_pin = 17

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ir_transmitter_pin, GPIO.OUT)

# Function to send an IR pulse
def send_ir_pulse():
    GPIO.output(ir_transmitter_pin, GPIO.HIGH)  # Turn on the IR transmitter
    time.sleep(0.5)  # Adjust the sleep duration based on your requirements
    GPIO.output(ir_transmitter_pin, GPIO.LOW)  # Turn off the IR transmitter

# Send IR pulses in a loop
try:
    while True:
        send_ir_pulse()
        time.sleep(1)  # Adjust the sleep duration between pulses if needed

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO on script exit
    GPIO.cleanup()
