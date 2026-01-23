import webbrowser
import os
#import subprocess   removed for cmd execution security reasons 

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "SuperSecret123":
        print("Access Granted! Welcome to the system.")
        # cmd = input("Enter system command: ")
        # subprocess.Popen(cmd, shell=True) removed for cmd execution security reasons
        open_patch_page()
    else:
        print("Access Denied.")

def open_patch_page():
    file_path = os.path.abspath(r"E:\cybersecurity\patch_mgmt.html")
    webbrowser.open(f"file://{file_path}")

login()
