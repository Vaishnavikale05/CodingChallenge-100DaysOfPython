#Program to swap two numbers using Third variable
a=int(input("Enter a number :"))
b=int(input("Enter a number :"))

print("Numbers before Swapping :-\n a=",a," b=",b)
temp=a
a=b
b=temp
print("Numbers after Swapping :-\n a=",a," b=",b)


#swapping without using third variable
print("Numbers before Swapping :- a=",a," b=",b)

a,b=b,a  #left,right=right,left

print("Numbers after Swapping :- a=",a," b=",b)