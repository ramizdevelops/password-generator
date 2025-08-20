import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        result_var.set("⚠️ Enter a number")
        return

    characters = string.ascii_letters  # A-Z, a-z
    if digits_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if length < 4:
        result_var.set("⚠️ Min length is 4")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    result_var.set(password)
    status_var.set("")

def copy_to_clipboard():
    if result_var.get():
        root.clipboard_clear()
        root.clipboard_append(result_var.get())
        root.update()
        status_var.set("✅ Copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("🔑 Password Generator")
root.geometry("420x300")
root.configure(bg="#f0f4f7")  # light background

# Password length
tk.Label(root, text="Password Length:", bg="#f0f4f7", fg="#333", font=("Arial", 11)).pack(pady=5)
length_entry = tk.Entry(root, width=10, font=("Arial", 11))
length_entry.insert(0, "12")
length_entry.pack()

# Options
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Digits (0-9)", variable=digits_var, bg="#f0f4f7", font=("Arial", 10)).pack()
tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=symbols_var, bg="#f0f4f7", font=("Arial", 10)).pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password,
          bg="#4CAF50", fg="white", font=("Arial", 11), relief="flat", padx=10, pady=5).pack(pady=10)

# Result
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, width=30, font=("Courier", 13), justify="center")
result_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard,
          bg="#2196F3", fg="white", font=("Arial", 11), relief="flat", padx=10, pady=5).pack(pady=5)

# Status
status_var = tk.StringVar()
tk.Label(root, textvariable=status_var, fg="green", bg="#f0f4f7", font=("Arial", 10, "italic")).pack(pady=5)

root.mainloop()