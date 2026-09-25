correct_username = "admin"
correct_password = "Python123"
username = input("Enter your username: ")
password = input("Enter your password: ")
has_length = len(password) >= 8
has_uppercase = any(char.isupper() for char in password)
has_number = any(char.isdigit() for char in password)
if username == correct_username and password == correct_password:
    print("Login successful!")
    print("Access granted.")
elif username != correct_username or password != correct_password:
    print("Login failed.")
    print("Access denied.")
if has_length and has_uppercase and has_number:
    print("Password meets the security requirements.")
else:
    print("Password does not meet the security requirements.")