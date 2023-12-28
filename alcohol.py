import tkinter as tk
import RPi.GPIO as GPIO
import time

# Define GPIO pins
D0_PIN = 17  # Digital output pin
A0_PIN = 27  # Analog output pin

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(D0_PIN, GPIO.IN)
GPIO.setup(A0_PIN, GPIO.IN)

def read_alcohol_concentration():
    digital_value = GPIO.input(D0_PIN)
    analog_value = GPIO.input(A0_PIN)
    return digital_value, analog_value

def update_values():
    digital_value, analog_value = read_alcohol_concentration()
    digital_label.config(text=f"Digital Value: {digital_value}")
    analog_label.config(text=f"Analog Value: {analog_value}")
    root.after(1000, update_values)  # Update every 1000 milliseconds (1 second)

# GUI setup
root = tk.Tk()
root.title("Alcohol Concentration Detector")

# Labels to display values
digital_label = tk.Label(root, text="Digital Value: ")
digital_label.pack()

analog_label = tk.Label(root, text="Analog Value: ")
analog_label.pack()

# Run the GUI update loop
update_values()

# Start the GUI
root.mainloop()

# Cleanup GPIO on program exit
GPIO.cleanup()
