import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("My GUI App")
root.geometry("1024x600")

# Create widgets
label = tk.Label(root, text="Hello, GUI!")
button = tk.Button(root, text="Click me!", command=on_button_click)

# Place widgets in the window
label.pack(pady=20)
button.pack()

# Start the main loop
root.mainloop()
