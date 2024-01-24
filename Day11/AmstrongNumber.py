#Amstrong number

num=int(input("Enter a number :"))
sum=0
temp=num
while(num>0):
    digit=num%10
    cube=digit**3
    sum=sum+cube
    num=num//10

if(sum==temp):
    print("Amstrong number")
else:
    print("Not an Amstrong Number")