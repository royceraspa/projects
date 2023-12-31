import tkinter as tk
def on_button_click(value):
    current_entry = entry_var.get()
    if value == 'Enter':
        check_password(current_entry)
        entry_var.set('')
    elif value == 'C':
        entry_var.set('')
    elif len(current_entry) < 4 and value.isdigit():
        entry_var.set(current_entry + value)
def check_password(password_attempt):
    correct_password = '2003'
    if password_attempt == correct_password:
        result_label.config(text="ACCESS GRANTED", fg="green")
    else:
        result_label.config(text="ACCESS DENIED", fg="red")
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

# Add keypad buttons to the Frame
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

# Label to display access result
# Label to display access result with padding
result_label = tk.Label(root, text="", fg="white", bg="black", font=("Helvetica", 20))
result_label.pack(pady=20)

# Place widgets in a vertical layout
entry_widget.pack(side=tk.TOP)
keypad_frame.pack(side=tk.TOP)
result_label.pack(side=tk.TOP)
# Place widgets in a vertical layout with additional padding
entry_widget.pack(side=tk.TOP, padx=20)
keypad_frame.pack(side=tk.TOP, padx=20)
result_label.pack(side=tk.TOP, padx=20)

# Bind the Escape key to exit the application
root.bind("<Escape>", lambda event: root.destroy())
# Start the main loop
root.mainloop()
