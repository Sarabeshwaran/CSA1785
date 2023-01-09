Input:

rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))
print("Enter the elements of Matrix:")
matrix= [[int(input()) for i in range(column)] for i in range(rows)]
print("-------Your  Matrix is---------")
for n in matrix:
    print(n)
    result =[[0 for i in range(rows)] for j in range(column)]
    for r in range(rows):
       for c in range(column):
           result[c][r] = matrix[r][c]
print("Transpose matrix is: ")
for r in result:
    print(r)

Output:

Enter the Number of rows : 2
Enter the Number of Columns: 2
Enter the elements of Matrix:
3
2
4
3
-------Your  Matrix is---------
[3, 2]
[4, 3]
Transpose matrix is: 
[3, 4]
[2, 3]
