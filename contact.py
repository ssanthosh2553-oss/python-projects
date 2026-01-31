import tkinter as tk
from tkinter import messagebox

FILE_NAME = "contacts.txt"

# ---------- FUNCTIONS ----------

def load_contacts():
    listbox.delete(0, tk.END)
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")
                listbox.insert(tk.END, data[0] + " - " + data[1])
    except FileNotFoundError:
        pass


def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name == "" or phone == "":
        messagebox.showwarning("Error", "Name and Phone are required")
        return

    with open(FILE_NAME, "a") as file:
        file.write(name + "|" + phone + "|" + email + "|" + address + "\n")

    clear_fields()
    load_contacts()
    messagebox.showinfo("Success", "Contact Added Successfully")


def get_selected_contact():
    try:
        index = listbox.curselection()[0]
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
        data = lines[index].strip().split("|")

        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)

        entry_name.insert(0, data[0])
        entry_phone.insert(0, data[1])
        entry_email.insert(0, data[2])
        entry_address.insert(0, data[3])
    except:
        pass


def update_contact():
    try:
        index = listbox.curselection()[0]
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        lines[index] = (
            entry_name.get() + "|" +
            entry_phone.get() + "|" +
            entry_email.get() + "|" +
            entry_address.get() + "\n"
        )

        with open(FILE_NAME, "w") as file:
            file.writelines(lines)

        clear_fields()
        load_contacts()
        messagebox.showinfo("Success", "Contact Updated")
    except:
        messagebox.showwarning("Error", "Select a contact to update")


def delete_contact():
    try:
        index = listbox.curselection()[0]
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        del lines[index]

        with open(FILE_NAME, "w") as file:
            file.writelines(lines)

        clear_fields()
        load_contacts()
        messagebox.showinfo("Success", "Contact Deleted")
    except:
        messagebox.showwarning("Error", "Select a contact to delete")


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)


# ---------- GUI DESIGN ----------

root = tk.Tk()
root.title("Contact Management System")
root.geometry("520x420")
root.resizable(False, False)

# Left Frame
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10)

tk.Label(frame_left, text="Contacts", font=("Arial", 14, "bold")).pack()

listbox = tk.Listbox(frame_left, width=30, height=18)
listbox.pack()
listbox.bind("<<ListboxSelect>>", lambda e: get_selected_contact())

# Right Frame
frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, padx=10)

tk.Label(frame_right, text="Name").pack()
entry_name = tk.Entry(frame_right, width=30)
entry_name.pack()

tk.Label(frame_right, text="Phone").pack()
entry_phone = tk.Entry(frame_right, width=30)
entry_phone.pack()

tk.Label(frame_right, text="Email").pack()
entry_email = tk.Entry(frame_right, width=30)
entry_email.pack()

tk.Label(frame_right, text="Address").pack()
entry_address = tk.Entry(frame_right, width=30)
entry_address.pack()

tk.Button(frame_right, text="Add Contact", width=20, command=add_contact).pack(pady=5)
tk.Button(frame_right, text="Update Contact", width=20, command=update_contact).pack(pady=5)
tk.Button(frame_right, text="Delete Contact", width=20, command=delete_contact).pack(pady=5)
tk.Button(frame_right, text="Clear", width=20, command=clear_fields).pack(pady=5)

load_contacts()
root.mainloop()
