import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("My GUI App")

# Set fullscreen mode
root.attributes("-fullscreen", True)

# Hide the mouse cursor
root.config(cursor="none")

# Create widgets
label = tk.Label(root, text="Hello, GUI!")
button = tk.Button(root, text="Click me!", command=on_button_click)

# Place widgets in a vertical layout
label.pack(side=tk.TOP, pady=20)
button.pack(side=tk.TOP)

# Start the main loop
root.mainloop()
