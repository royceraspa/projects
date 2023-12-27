import RPi.GPIO as GPIO
import time

# Set GPIO mode and pin
GPIO.setmode(GPIO.BCM)
water_pin = 18

# Set up GPIO pin as input
GPIO.setup(water_pin, GPIO.IN)

def water_detected(channel):
    print("Water detected!")

# Add event detection
GPIO.add_event_detect(water_pin, GPIO.FALLING, callback=water_detected, bouncetime=300)

try:
    print("Waiting for water...")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    # Cleanup
    GPIO.cleanup()
