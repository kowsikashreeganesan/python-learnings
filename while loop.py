password = "" 
attempt = 0
while password != "cyber123" and attempt <= 3:
    password = input("Enter your passwoed:")
    attempt += 1
    if password == "cyber123":
        print("Access Granted")
    else:
        print("Access Denied")