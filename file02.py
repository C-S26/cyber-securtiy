import webbrowser
import os

def login():
    username = input("Enter Username: ")
    if username == "admin" and "SuperSecret123": 
        print("Access Granted! Welcome to the system.")
        open_patch_page()
    else:
        print("Access Denied.")

def open_patch_page():
    file_path = os.path.abspath("E:\cybersecurity\patch_mgmt.html")
    webbrowser.open(f"file://{file_path}")

login()
