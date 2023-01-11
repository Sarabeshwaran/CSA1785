Input:

string=input("Enter elements:")
a=string.split()
print("The List is :",a)
string=input("Enter elements:")
b=string.split()
print("The List is :",b)
print("operations")
c=list(set(a)|set(b))
print("union operation  ",c)
d=list(set(a)&set(b))
print("intersection operation  ",d)
e=list(set(a)-set(b))
print("difference operation  ",e)
f=list(set(a)^set(b))
print("symmetric operation  ",f)

Output:

Enter elements:1 2 4 3 5
The List is : ['1', '2', '4', '3', '5']
Enter elements:3 5 6 7 2
The List is : ['3', '5', '6', '7', '2']
operations
union operation   ['5', '2', '1', '6', '3', '4', '7']
intersection operation   ['5', '2', '3']
difference operation   ['4', '1']
symmetric operation   ['4', '1', '6', '7']
