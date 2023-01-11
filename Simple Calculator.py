Input:

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
print("Select The Operation You Want: ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
while True:
    operation=input("Enter the operation you want(a,s,m,d): ")
    if operation in ('a','s','m','d'):
        n1=float(input("Enter the First Number:"))
        n2=float(input("Enter the Second Number:"))
        if operation=='a':
            print(n1,"+",n2,"=",add(n1,n2))
        elif operation=="s":
            print(n1,"-",n2,"=",subtract(n1,n2))
        elif operation=="m":
            print(n1,"*",n2,"=",multiply(n1,n2))
        elif operation=="d":
            print(n1,"/",n2,"=",division(n1,n2))
        break
    else:
        print("Invalid Input")
        print("Enter your Choice 1.continue(yes),2.discontinue(no):")
        option=input("choice:")
        if option==("yes"):
            print("program continue")
        elif option==("no"):
            print("program discontinue")
            break
            
Output:

Select The Operation You Want: 
1.Addition
2.Subtraction
3.Multiplication
4.Division
Enter the operation you want(a,s,m,d): 5
Invalid Input
Enter your Choice 1.continue(yes),2.discontinue(no):
choice:yes
program continue
Enter the operation you want(a,s,m,d): a
Enter the First Number:5
Enter the Second Number:4
5.0 + 4.0 = 9.0
