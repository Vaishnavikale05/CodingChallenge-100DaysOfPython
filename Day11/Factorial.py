#Factorial of a number using for loop

num=int(input("Enter a number :"))

if(num<0):
    print("Factorial doesn't exist for negative number..")
if(num==0):
    print("Factorisl of 0 is : 1")
if(num>0):
    f=1
    for i in range(1,num+1):
       f=f*i
    print("Factorial of ",num," is ",f)

    
#Factorial using Recursion

def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

num=int(input("Enter a number :"))
print("Factorial of ",num," is ",fact(num))