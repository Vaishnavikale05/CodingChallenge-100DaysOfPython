#Largest among the three numbers

a=int(input("Enter No1:"))
b=int(input("Enter No2:"))
c=int(input("Enter No3:"))


if(a>b) and (a>c):
    print(a," is greater")
elif(b>a) and(b>c):
    print(b," is greater")
else:
    print(c," is greater")