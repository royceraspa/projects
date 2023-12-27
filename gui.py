import tkinter as tk
import RPi.GPIO as GPIO
import threading
import time

def on_button_click(value):
    current_entry = entry_var.get()

    if value == 'Enter':
        check_password(current_entry)
        entry_var.set('')
        update_circle_display()
    elif value == 'C':
        entry_var.set('')
        reset_circle_display()
    elif len(current_entry) < 4 and value.isdigit():
        entry_var.set(current_entry + value)
        update_circle_display()
        flash_button(value)

def check_password(password_attempt):
    correct_password = '2003'

    if password_attempt == correct_password:
        result_label.config(text="ACCESS GRANTED", fg="green")
        control_traffic_light(True)  # Turn on the green LED
        reset_after_delay()
    else:
        result_label.config(text="ACCESS DENIED", fg="red")
        control_traffic_light(False)  # Turn on the red LED

def control_traffic_light(access_granted):
    if access_granted:
        GPIO.output(RED_PIN, GPIO.LOW)   # Turn off the red LED
        GPIO.output(GREEN_PIN, GPIO.HIGH)  # Turn on the green LED
    else:
        GPIO.output(RED_PIN, GPIO.HIGH)   # Turn on the red LED
        GPIO.output(GREEN_PIN, GPIO.LOW)  # Turn off the green LED

def reset_traffic_light():
    control_traffic_light(False)  # Turn on the red LED
    result_label.config(text="")  # Clear the result label

def reset_after_delay():
    threading.Timer(5, reset_traffic_light).start()

def flash_button(value):
    button = None

    for child in keypad_frame.winfo_children():
        if child.cget("text") == value:
            button = child
            break

    if button:
        button.configure(bg="grey")
        root.after(100, lambda: button.configure(bg="black"))  # Flash for 100ms

def update_circle_display():
    entry_value = entry_var.get()

    for i, circle in enumerate(circle_widgets):
        if i < len(entry_value):
            circle.config(bg="grey")
        else:
            circle.config(bg="black")

def reset_circle_display():
    for circle in circle_widgets:
        circle.config(bg="black")

# GPIO setup
GPIO.setmode(GPIO.BCM)
RED_PIN = 17  # Replace with the actual GPIO pin for the red LED
GREEN_PIN = 18  # Replace with the actual GPIO pin for the green LED
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

# Create the main window
root = tk.Tk()
root.title("Password Entry")

# Set fullscreen mode
root.attributes("-fullscreen", True)

# Hide the mouse cursor
root.config(cursor="none")

# Set a black background
root.configure(bg="black")

# Entry widget to display the password input
entry_var = tk.StringVar()
entry_widget = tk.Entry(root, textvariable=entry_var, font=("Helvetica", 20), justify='center', bd=5, relief='solid', fg="white", bg="black", width=4, state="disabled")
entry_widget.pack(pady=20)

# Create a Frame for the keypad
keypad_frame = tk.Frame(root, bg="black")

# Define keypad buttons
keypad_buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', 'Enter',
    'C'  # Clear button
]

# Add keypad buttons to the Frame with circular appearance
for row in range(4):
    for col in range(3):
        index = row * 3 + col
        button_value = keypad_buttons[index]
        button = tk.Button(keypad_frame, text=button_value, width=5, height=2,
                           command=lambda value=button_value: on_button_click(value),
                           fg="white", bg="black", bd=4, relief='solid', font=("Helvetica", 16))

        # Make buttons circular by setting oval shape
        button.config(width=5, height=2)
        button['border'] = '0'

        button.grid(row=row, column=col, padx=5, pady=5)

# Create circles for display
circle_widgets = [tk.Label(keypad_frame, bg="black", width=2, height=1, bd=2, relief="solid") for _ in range(4)]
for i, circle in enumerate(circle_widgets):
    circle.grid(row=4, column=i, padx=5, pady=5)

# Label to display access result with padding
result_label = tk.Label(root, text="", fg="white", bg="black", font=("Helvetica", 20))
result_label.pack(pady=20)

# Bind the Escape key to exit the application
root.bind("<Escape>", lambda event: root.destroy())

# Center and place widgets in a vertical layout
entry_widget.pack(side=tk.TOP, pady=20)
keypad_frame.pack(side=tk.TOP)
result_label.pack(side=tk.TOP, pady=20)

# Initialize the traffic light as red
control_traffic_light(False)

# Start the main loop
root.mainloop()

# Cleanup GPIO
GPIO.cleanup()
