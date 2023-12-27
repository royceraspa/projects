Skip to content
royceraspa
/
projects

Type / to search

Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Commit
Update gui.py
 main
@royceraspa
royceraspa committed 1 hour ago 
1 parent cb9ca1b
commit 1d92c17
Showing 1 changed file with 11 additions and 6 deletions.
  17 changes: 11 additions & 6 deletions17  
gui.py
@@ -49,24 +49,29 @@ def check_password(password_attempt):
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
0 comments on commit 1d92c17
@royceraspa
Comment
 
Leave a comment
 
 You’re receiving notifications because you’re watching this repository.
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact
Manage cookies
Do not share my personal information
Update gui.py · royceraspa/projects@1d92c17
