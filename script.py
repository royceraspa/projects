import RPi.GPIO as GPIO
import time

# Set GPIO mode and pin
GPIO.setmode(GPIO.BCM)
touch_pin = 17

# Set up GPIO pin as input
GPIO.setup(touch_pin, GPIO.IN)

def touch_detected(channel):
    print("Touch detected!")

# Add event detection
GPIO.add_event_detect(touch_pin, GPIO.FALLING, callback=touch_detected, bouncetime=300)

try:
    print("Waiting for touch...")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    # Cleanup
    GPIO.cleanup()
