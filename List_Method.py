Input:
  
string=input("Enter elements:")
a=string.split()
print("The List is :",a)
a[0]=1
print(a)
a.append(7)
print(a)
a.extend([5,6,7])
print(a)
del a[5]
print(a)

Output:

Enter elements:1 2 3 4
The List is : ['1', '2', '3', '4']
[1, '2', '3', '4']
[1, '2', '3', '4', 7]
[1, '2', '3', '4', 7, 5, 6, 7]
[1, '2', '3', '4', 7, 6, 7]
