import tkinter as tk
from tkinter import *
import bmi 
import bp 
import hr

#create tkinter window
window = tk.Tk()

#create window size
window.geometry("400x400")
window.title("Health Tracker Application")

# adding buttons function
def second_window():
    calculate_bmi = bmi.main()
    
def third_window():
    calculate_bp = bp.main()

def fourth_window():
    calculate_hr = hr.main()

#adding label
l1 = tk.Label(window, text="Health Tracker", font=("Arial",28))
l1.grid(row = 0, column = 0)
l1.place(x=100,y=10)

#adding button
b1=tk.Button(window,text="BMI",width=14, font=("Arial",20), command=second_window)
b1.place(x=110,y=100)

b2=tk.Button(window,text="MAP",width=14, font=("Arial",20), command=third_window)
b2.place(x=110,y=180)

b3=tk.Button(window,text="HRmax",width=14, font=("Arial",20), command=fourth_window)
b3.place(x=110,y=260)

# run application
window.mainloop()




 