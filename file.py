import webbrowser
import os

def login():
    username = input("Enter Username: ")
<<<<<<< HEAD
    password = input("enter password:")
    # input validation added, user name and password
=======
    password =  input("enter password: ")
    #input validation added, username and password.
>>>>>>> 8cd77fcb6332847ef4ebe39e6b229061de9401bd
    if username == "admin" and password == "SuperSecret123": 
        print("Access Granted! Welcome to the system.")
        open_patch_page()
    else:
        print("Access Denied.")

def open_patch_page():
    file_path = os.path.abspath("E:\cybersecurity\patch_mgmt.html")
    webbrowser.open(f"file://{file_path}")
login()
