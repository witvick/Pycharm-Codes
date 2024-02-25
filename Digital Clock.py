from tkinter import *
import time

root = Tk()
root.title("Digital Clock")

def get_time():
    timeVar = time.strftime("%H:%M:%S")
    clock.config(text=timeVar)
    clock.after(200, get_time)  # Corrected the function call

clock = Label(root, font=('Calibri', 60), bg='grey', fg='white')
clock.pack()

get_time()  # Start the clock
root.mainloop()

