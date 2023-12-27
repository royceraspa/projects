import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

def on_exit(event):
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("My GUI App")

# Set fullscreen mode
root.attributes("-fullscreen", True)

# Hide the mouse cursor
root.config(cursor="none")

# Set a black background
root.configure(bg="black")

# Create widgets
label = tk.Label(root, text="Hello, GUI!", fg="white", bg="black", font=("Helvetica", 24))

# Create a Frame for the keypad
keypad_frame = tk.Frame(root, bg="black")

# Define keypad buttons
keypad_buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', 'Enter'
]

# Function to handle keypad button clicks
def on_keypad_click(value):
    print(f"Key pressed: {value}")

# Add keypad buttons to the Frame
for row in range(4):
    for col in range(3):
        index = row * 3 + col
        button_value = keypad_buttons[index]
        button = tk.Button(keypad_frame, text=button_value, width=5, height=2,
                           command=lambda value=button_value: on_keypad_click(value),
                           fg="black", bg="white", font=("Helvetica", 16))
        button.grid(row=row, column=col, padx=5, pady=5)

# Place widgets in a vertical layout
label.pack(side=tk.TOP, pady=20)
keypad_frame.pack(side=tk.TOP)

# Bind the Escape key to the exit function
root.bind("<Escape>", on_exit)

# Start the main loop
root.mainloop()
