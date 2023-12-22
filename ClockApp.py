import tkinter as tk
from time import strftime

def update_time():
    string_time = strftime('%H:%M:%S %p')
    label.config(text=string_time)
    label.after(1000, update_time)  # Update time every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Clock App")

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Run the update_time function to initialize the clock
update_time()

# Run the main loop
root.mainloop()
