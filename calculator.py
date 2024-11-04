import tkinter as tk
from tkinter import ttk

# Function to handle button click and update the expression
def button_click(value):
    current_text = entry.get()
    if current_text == "ERROR":
        current_text = ""
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

# Function to handle the equals button click and evaluate the expression
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERROR")

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the expression or result
entry = ttk.Entry(root, font=('Arial', 16), justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
]

# Create number and operation buttons
for (text, row, col) in buttons:
    ttk.Button(root, text=text, command=lambda t=text: button_click(t), width=10).grid(row=row, column=col, sticky="nsew")

# Clear button
ttk.Button(root, text="C", command=clear, width=10).grid(row=4, column=3, sticky="nsew")

# Equal button
ttk.Button(root, text="=", command=calculate, width=10).grid(row=5, column=0, columnspan=4, sticky="nsew")

# Configure row and column weights for responsive layout
for i in range(6):  # Adjusted to include an extra row for "="
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

# Start the Tkinter event loop
root.mainloop()
