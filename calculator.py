a=int(input("enter first number:"))
b=int(input("enter second number="))
print("select operation")
print("1. addition ")
print("2. subtraction")
print("3. multiplication")
print("4. division")
choice =int(input("enter your choice to perform operation (1-4)" ))
if choice==1:
    print("addition=",a+b)
elif choice==2:
    print("subtraction=",a-b)
elif choice==3:
    print("multiplication=",a*b)    
elif choice==4:
    if b!=0:
        print("division=",a / b)
    else:
        print("zero division")
else:
    print("invalid choice")        