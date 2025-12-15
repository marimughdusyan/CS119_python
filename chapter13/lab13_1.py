# Mari Mughdusyan
# CS 119 programming in python
# chapter 13 lab 1

import tkinter as tk

# Function to display the info
def show_info():
    info_label.config(text="Mari Mughdusyan\n123 Some Street\nCalifornia, USA")

# Create the main window
window = tk.Tk()
window.title("Name and Address")
window.geometry("350x150")  # Adjusted window size

# Frame to hold buttons side by side
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Show Info button
show_button = tk.Button(button_frame, text="Show Info", command=show_info)
show_button.pack(side="left", padx=5)

# Quit button
quit_button = tk.Button(button_frame, text="Quit", command=window.destroy)
quit_button.pack(side="left", padx=5)

# Label to display the info
info_label = tk.Label(window, text="", font=("Arial", 12))
info_label.pack(pady=10)

# Run the main event loop
window.mainloop()