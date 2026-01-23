import webbrowser
import os
import tkinter as tk
from tkinter import messagebox

# PATCH MANAGEMENT LAB: VULNERABLE GUI VERSION
# Goal: Use Bandit to find the flaws and patch them.

def validate_login():
    username = entry_user.get()
    password = entry_pass.get()

    # VULNERABILITY 1: Hardcoded plaintext credentials
    # Bandit will flag this as a high-severity security risk.
    if username == "admin" and password == "SuperSecret123":
        messagebox.showinfo("Success", "Access Granted! Opening Patch Page...")
        open_patch_page()
    else:
        messagebox.showerror("Error", "Access Denied. Invalid credentials.")

def open_patch_page():
    # VULNERABILITY 2: Hardcoded absolute file path
    # This exposes system architecture and is not portable.
    file_path = os.path.abspath("E:\\cybersecurity\\patch_mgmt.html")
    
    if os.path.exists(file_path):
        webbrowser.open(f"file://{file_path}")
    else:
        messagebox.showwarning("Warning", f"Path not found: {file_path}")

# tkinter GUI
root = tk.Tk()
root.title("Secure Login Portal")
root.geometry("300x200")

tk.Label(root, text="Username:").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack(pady=5)

tk.Button(root, text="Login", command=validate_login).pack(pady=20)

root.mainloop()
