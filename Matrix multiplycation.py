# In this i took inputs from users and i have checked if columns of 1st matrix is eual to second matrix and after that only the program will run otherwise it will show invali entry.
r1=int(input("enter the no. of rows in matrix 1:"))
c1= int(input("columns no.:"))

r2= int(input("no. rows in matrix 2:"))
c2= int(input("no.of columns in matrix 2: "))

if c1 == r2:
    print("Enter the value in matrix 1 ")
    mat1 = []

    for j in range(0, r1):
        col = []

        for i in range(0, c1):
            a = int(input())
            col.append(a)

        mat1.append(col)
    print(mat1)

    print("enter values in matrix 2  ")
    mat2 = []

    for l in range(0, r2):
        el = []
        for o in range(0, c2):
            b = int(input())
            el.append(b)

        mat2.append(el)

    print(mat2)

    result = []

    for w in range(0, r1):
        re = []
        for u in range(0, c2):
            c = 0
            re.append(c)

        result.append(re)

    for i in range(0, len(result)):
        for j in range(0, len(result[0])):
            for k in range(0, len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    print("final result after multiplycation is: ")

    for row in result:
        print(row)









else:
    print("matrix multiplication is not possible since column of 1st matrix is not same as row of seconf matrix")