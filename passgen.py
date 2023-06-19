import string
import random
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

def generate_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_special_chars = special_chars_var.get()
    special_chars = special_chars_entry.get()

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_special_chars:
        characters += special_chars

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=password)

def copy_to_clipboard():
    password = password_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")

# Length selection
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = ttk.Entry(root)
length_entry.insert(0, "10")  # Default length
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Uppercase checkbox
uppercase_var = tk.IntVar()
uppercase_checkbox = ttk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=0, padx=5, pady=5)

# Special characters checkbox
special_chars_var = tk.IntVar()
special_chars_checkbox = ttk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var)
special_chars_checkbox.grid(row=2, column=0, padx=5, pady=5)

# Special characters entry
special_chars_entry = ttk.Entry(root)
special_chars_entry.grid(row=2, column=1, padx=5, pady=5)
special_chars_entry.config(state="disabled")

def toggle_special_chars():
    if special_chars_var.get():
        special_chars_entry.config(state="normal")
    else:
        special_chars_entry.config(state="disabled")

special_chars_checkbox.config(command=toggle_special_chars)

# Generate password button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Password label
password_label = ttk.Label(root, text="")
password_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Copy to clipboard button
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
