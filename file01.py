def login():
    username = input("Enter Username: ")
    if username == "admin" and "SuperSecret123": 
        print("Access Granted! Welcome to the system.")
    else:
        print("Access Denied.")

login()
