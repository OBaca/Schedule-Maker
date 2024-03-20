from tkinter import Tk, Label, IntVar
from customtkinter import *

def check_availability():
    availability = []
    for day, var in zip(days_of_week, day_vars):
        availability.append((day, var.get()))
    print("Worker's availability:")
    for day, available in availability:
        print(f"{day}: {'Available' if available else 'Not Available'}")

# Create Tkinter window
root = CTk()
root.title("Worker's Schedule")

# Days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Variables to store availability for each day
day_vars = [IntVar() for _ in range(len(days_of_week))]

# Schedule box layout
for i, day in enumerate(days_of_week):
    label = Label(root, text=day)
    label.grid(row=i, column=0)
    checkbox = CTkCheckBox(root, variable=day_vars[i], onvalue=1, offvalue=0,text="")
    checkbox.grid(row=i, column=1)

# Button to check availability
check_button = CTkButton(root, text="Check Availability", command=check_availability)
check_button.grid(row=len(days_of_week), columnspan=2)

root.mainloop()