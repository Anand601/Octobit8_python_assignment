a=int(input("Total number of element in list :" )) # taking no. of element in the list
list1=[] # making of empty list


# for loop to add element in the list
for i in range(0,a):
    b= int(input("enter the number : "))
    list1.append(b)

print("your list is:",list1) # printing the list

list1.sort() # arranging the list in ascending order

f=int(input("nth large number you want? "))  # taking nth number from the user.

# making sure nth number should not exceed the total number of element in the list otherwise it will show else statement
if f<=a:
    print("your nth largest number is: ",list1[-f])
else:
    print("invalid entry")
