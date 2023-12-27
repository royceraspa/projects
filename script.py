import RPi.GPIO as GPIO
import time

# Set GPIO mode and pins
GPIO.setmode(GPIO.BCM)
red_pin = 17
yellow_pin = 22
green_pin = 10

# Set up GPIO pins as output
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

def traffic_light_sequence():
    try:
        while True:
            # Red light
            GPIO.output(red_pin, GPIO.HIGH)
            time.sleep(5)

            # Transition to green (red and yellow off)
            GPIO.output(red_pin, GPIO.LOW)
            GPIO.output(yellow_pin, GPIO.LOW)

            # Green light
            GPIO.output(green_pin, GPIO.HIGH)
            time.sleep(5)

            # Transition to yellow (green off)
            GPIO.output(green_pin, GPIO.LOW)
            GPIO.output(yellow_pin, GPIO.HIGH)
            time.sleep(2)

    except KeyboardInterrupt:
        pass
    finally:
        # Cleanup
        GPIO.cleanup()

if __name__ == "__main__":
    traffic_light_sequence()
