password = input("Enter your password:")
uppercase_count = 0
digit_count = 0
special_count = 0
special_characters = "@#$%!&"
for character in password:
    if character.isupper():
        uppercase_count+=1
    if character.isdigit():
        digit_count+=1
    if character in special_characters:
        special_count+=1
if (len(password)==13
    and uppercase_count>=1
    and digit_count==3
    and special_count==1):
    print ("Access Granted")
else:
    print ("Access Denied")