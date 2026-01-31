





import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Select at least one character type")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def on_generate():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length")
        return

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
        result_entry.select_range(0, tk.END)
        result_entry.focus()
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showwarning("Warning", "No password to copy")


# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("650x420")  # increased window size
root.resizable(False, False)

# Title
header = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"))
header.pack(pady=10)

# Length Frame
length_frame = tk.Frame(root)
length_frame.pack(pady=5)

tk.Label(length_frame, text="Password Length:", font=("Arial", 11)).pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, width=10, font=("Arial", 11))
length_entry.pack(side=tk.LEFT, padx=8)
length_entry.insert(0, "12")

# Options Frame
options_frame = tk.LabelFrame(root, text="Include Characters", padx=10, pady=10)
options_frame.pack(pady=10)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=upper_var).grid(row=0, column=0, sticky="w", padx=10)
tk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=lower_var).grid(row=1, column=0, sticky="w", padx=10)
tk.Checkbutton(options_frame, text="Digits (0-9)", variable=digits_var).grid(row=2, column=0, sticky="w", padx=10)
tk.Checkbutton(options_frame, text="Symbols (!@#$)", variable=symbols_var).grid(row=3, column=0, sticky="w", padx=10)

# Buttons Frame
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

generate_btn = tk.Button(buttons_frame, text="Generate Password", command=on_generate, width=20, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
generate_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(buttons_frame, text="Copy", command=copy_to_clipboard, width=10, font=("Arial", 11))
copy_btn.grid(row=0, column=1, padx=10)

# Result Frame (INCREASED)
result_frame = tk.LabelFrame(root, text="Generated Password", padx=15, pady=15)
result_frame.pack(pady=15, fill=tk.X, padx=20)

# Entry + Scrollbar container
entry_frame = tk.Frame(result_frame)
entry_frame.pack(fill=tk.X)

scrollbar = tk.Scrollbar(entry_frame, orient=tk.HORIZONTAL)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

result_entry = tk.Entry(
    entry_frame,
    font=("Arial", 14, "bold"),  # bigger font
    width=60,                    # much wider box
    justify="center",
    xscrollcommand=scrollbar.set
)
result_entry.pack(side=tk.TOP, fill=tk.X, expand=True)

scrollbar.config(command=result_entry.xview)

# Footer
footer = tk.Label(root, text="Made with Python Tkinter", font=("Arial", 9), fg="gray")
footer.pack(side=tk.BOTTOM, pady=5)

root.mainloop()
