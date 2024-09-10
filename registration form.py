import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    event = event_var.get()
    
    # Simple validation
    if not name or not email or not phone or not event:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    # Print to console (or you can process the data further)
    print(f"Full Name: {name}")
    print(f"Email Address: {email}")
    print(f"Phone Number: {phone}")
    print(f"Selected Event: {event}")
    
    # Show confirmation message
    messagebox.showinfo("Registration Successful", "Registration successful! Thank you for signing up.")
    
    # Clear the form
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    event_var.set('')

# Create the main window
root = tk.Tk()
root.title("Event Registration")

# Create and place labels and entry fields
tk.Label(root, text="Full Name:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email Address:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Phone Number:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
entry_phone = tk.Entry(root)
entry_phone.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Select Event:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
event_var = tk.StringVar(value='')
event_menu = tk.OptionMenu(root, event_var, 
                          "Tech Conference", 
                          "Workshop", 
                          "Networking Event", 
                          "Webinar")
event_menu.grid(row=3, column=1, padx=10, pady=10)

# Submit button
submit_button = tk.Button(root, text="Register", command=submit_form)
submit_button.grid(row=4, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
