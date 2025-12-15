import tkinter as tk

# Prices of services
services = {
    "Oil change": 30.00,
    "Lube job": 20.00,
    "Radiator flush": 40.00,
    "Transmission flush": 100.00,
    "Inspection": 35.00,
    "Muffler replacement": 200.00,
    "Tire rotation": 20.00
}

# Function to calculate total charges
def calculate_total():
    total = 0
    for service, var in service_vars.items():
        if var.get() == 1:
            total += services[service]
    total_label.config(text=f"Total Charges: ${total:.2f}")

# Create main window
window = tk.Tk()
window.title("Joe’s Automotive")
window.geometry("300x350")

# Create a frame for checkbuttons
check_frame = tk.Frame(window)
check_frame.pack(pady=10)

# Dictionary to store IntVar for each service
service_vars = {}

# Create check buttons
for service in services:
    var = tk.IntVar()
    chk = tk.Checkbutton(check_frame, text=f"{service} — ${services[service]:.2f}", variable=var)
    chk.pack(anchor='w')
    service_vars[service] = var

# Button to calculate total
total_button = tk.Button(window, text="Calculate Total", command=calculate_total)
total_button.pack(pady=10)

# Label to display total charges
total_label = tk.Label(window, text="Total Charges: $0.00", font=("Arial", 12))
total_label.pack(pady=10)

window.mainloop()