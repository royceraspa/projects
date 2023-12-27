import tkinter as tk
import threading

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
        reset_after_delay()
    else:
        result_label.config(text="ACCESS DENIED", fg="red")

def reset_result_label():
    result_label.config(text="")  # Clear the result label

def reset_after_delay():
    threading.Timer(5, reset_result_label).start()

def flash_button(value):
    for child in keypad_frame.winfo_children():
        if child.cget("text") == value:
            child.configure(bg="grey")
            root.after(100, lambda c=child: c.configure(bg="black"))  # Flash for 100ms

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
entry_widget = tk.Entry(root, textvariable=entry_var, font=("Helvetica", 20), justify='center', bd=5, relief='solid', fg="white", bg="black", width=4)
entry_widget.pack(side=tk.TOP, pady=20)

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

# Add keypad buttons to the Frame
for row in range(4):
    for col in range(3):
        index = row * 3 + col
        button_value = keypad_buttons[index]
        button = tk.Button(keypad_frame, text=button_value, width=5, height=2,
                           command=lambda value=button_value: on_button_click(value),
                           fg="white", bg="black", bd=4, relief='solid', font=("Helvetica", 16))
        button.grid(row=row, column=col, padx=5, pady=5)

# Label to display access result
result_label = tk.Label(root, text="", fg="white", bg="black", font=("Helvetica", 20))
result_label.pack(side=tk.TOP, pady=20)

# Bind the Escape key to exit the application
root.bind("<Escape>", lambda event: root.destroy())

# Start the main loop
root.mainloop()
