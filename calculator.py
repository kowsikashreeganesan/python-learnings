a= int(input("Enter your num1:"))
b= int(input("Enter your num2:"))
operator = input("Enter your operator(+, -, *, /, //, **, %, <, >, ==):")
if operator == "+":
   print ("Result:", a+b)
elif operator == "-": 
    print ("Result:", a-b)
elif operator == "*":
    print ("Result:", a*b)
elif operator == "/": 
    if b != 0:
        print("Result:", a/b)
    else:
        print("Result: Cannot be divided by zero")    
elif operator == "//": 
    print ("Result:", a//b)
elif operator == "**":
    print ("Result:", a**b)
elif operator == "%":
    print ("Result:", a%b)
elif operator == "<":
    print ("Result:", a<b)
elif operator == "<":
    print ("Result:", a<b)
elif operator == ">":
    print ("Result:", a>b)
elif operator == "==":
    print ("Result:", a==b)    
else:
    print ("Invalid operator")