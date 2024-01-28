list1=[10,20,30,40,50,60]
print(list1)

print(type(list1))
list1[2]="hello"
print(list1)

#List Operations

#1]Concatination :-combining two lists

list2=[30,20,1,98]
print(list1+list2)

#2]Repitation :-Repeating the same list for multiple times is done using * operator
print(list1*3)

#3]Membersip :-Checking if the item is present in the list and returns true or false
print(30 in list2)

#4]Slicing :-chopping down the list into small sub Lists
print(list1[2:])
print(list1[3:6])
print(list1[:4])
print(list1[-5])
print(list1[:-4])
