from tkinter import *

# Create window
window = Tk()
window.title("Calculator")
window.geometry("250x250")

# create input
num1 = Entry(window)
num1.pack(pady=5)

num2 = Entry(window)
num2.pack(pady=5)

# Result 
result = Label(window, text="Result")
result.pack(pady=10)

# Functions
def add():
    result.config(text=int(num1.get()) + int(num2.get()))

def subtract():
    result.config(text=int(num1.get()) - int(num2.get()))

def multiply():
    result.config(text=int(num1.get()) * int(num2.get()))

def divide():
    result.config(text=int(num1.get()) / int(num2.get()))

# Buttons
Button(window, text="Add", command=add).pack(pady=2)
Button(window, text="Subtract", command=subtract).pack(pady=2)
Button(window, text="Multiply", command=multiply).pack(pady=2)
Button(window, text="Divide", command=divide).pack(pady=2)

# Runs
window.mainloop()
