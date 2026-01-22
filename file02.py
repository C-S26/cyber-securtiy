import webbrowser
import os
import subprocess   #bandit

ADMIN_PASSWORD = "SuperSecret123"

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == ADMIN_PASSWORD:
        print("Access Granted! Welcome to the system.")

        cmd = input("Enter system command: ")
        subprocess.Popen(cmd, shell=True)

        open_patch_page()
    else:
        print("Access Denied.")

def open_patch_page():
    file_path = os.path.abspath(r"E:\cybersecurity\patch_mgmt.html")
    webbrowser.open(f"file://{file_path}")
    GITHUB_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz123456"

login()
