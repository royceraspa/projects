import tkinter as tk
import RPi.GPIO as GPIO
import threading
import time

def on_button_click(value):
    current_entry = entry_var.get()

    if value == 'Enter':
        check_password(current_entry)
        entry_var.set('')
    elif value == 'C':
        entry_var.set('')
    elif len(current_entry) < 4 and value.isdigit():
        entry_var.set(current_entry + value)
        flash_button(value)

def check_password(password_attempt):
    correct_password = '2003'

    if password_attempt == correct_password:
        result_label.config(text="ACCESS GRANTED", fg="green")
        control_rgb_led(True)  # Turn on the RGB LED with green color
        reset_after_delay()
    else:
        result_label.config(text="ACCESS DENIED", fg="red")
        control_rgb_led(False)  # Turn on the RGB LED with red color

def control_rgb_led(access_granted):
    if access_granted:
        GPIO.output(R_PIN, GPIO.LOW)  # Turn off the red color
        GPIO.output(G_PIN, GPIO.HIGH)  # Turn on the green color
    else:
        GPIO.output(R_PIN, GPIO.HIGH)  # Turn on the red color
        GPIO.output(G_PIN, GPIO.LOW)   # Turn off the green color

def reset_rgb_led():
    control_rgb_led(False)  # Turn on the RGB LED with red color
    result_label.config(text="")  # Clear the result label

def reset_after_delay():
    threading.Timer(5, reset_rgb_led).start()

def flash_button(value):
    button = None

    for child in keypad_frame.winfo_children():
        if child.cget("text") == value:
            button = child
            break

    if button:
        button.configure(bg="grey")
        root.after(100, lambda: button.configure(bg="black"))  # Flash for 100ms

# GPIO setup
GPIO.setmode(GPIO.BCM)
V_PIN = 5  # Connect to the V (Voltage) pin of the RGB LED
R_PIN = 6  # Connect to the R (Red) pin of the RGB LED
G_PIN = 19  # Connect to the G (Green) pin of the RGB LED

GPIO.setup(V_PIN, GPIO.OUT)
GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(G_PIN, GPIO.OUT)

# Set initial states
GPIO.output(V_PIN, GPIO.HIGH)  # Turn on the voltage
GPIO.output(R_PIN, GPIO.HIGH)  # Turn on the red color
GPIO.output(G_PIN, GPIO.LOW)   # Turn off the green color

# Create the main window
root = tk.Tk()
root.title("Password Entry")

# ... (rest of the code remains unchanged)
