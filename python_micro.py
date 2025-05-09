def add(x,y):
    return (x+y)
def sub(x,y):
    return (x-y)
def mul(x,y):
    return (x*y)
    
def div(x,y):
    return (x/y)
    
def intdiv(x,y):
    return (x//y)
    
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
def mpow(x,y):
    return (x**y)
    
def Inverse(n):
	return (1/n)
	
flag=True
while (True):
    choice=int(input('''\nEnter choice: 
		>> 1 Addition
		>> 2 Subtraction
		>> 3 Multiplication
		>> 4 Division
		>> 5 Inverse
		>> 6 Foctorial
		>> 7 Power
		>> 8 Exit 
                     
        >>Enter your Choice here ->'''))

    if choice==1:
        a=int(input("\nEnter Number-1: "))
        b=int(input("Enter Number-2: "))
        print("Addition = ",add(a,b))
    elif choice==2:
        a=int(input("\nEnter Number-1: "))
        b=int(input("Enter Number-2: "))
        print("Subtraction = ",sub(a,b))
    elif choice==3:
        a=int(input("\nEnter Number-1: "))
        b=int(input("Enter Number-2: "))
        print("Multiplication = ",mul(a,b))
    elif choice==4:
        a=int(input("\nEnter Number-1: "))
        b=int(input("Enter Number-2: "))
        print("Division = ",div(a,b))
    elif choice==5:
        n=int(input("\nEnter Number-1: "))
        print("Inverse = ",Inverse(n),"=","1/",n)
    elif choice==6:
        x=int(input("\nEnter Number-1: "))
        print("Foctorial = ",factorial(x))
    elif choice==7:
        a=int(input("\nEnter Number-1: "))
        b=int(input("Enter Number-2: "))
        print(mpow(a,b))
    elif choice==8:
        break
    else:
        print('Invalid choice')
