#Defining a List
marks =[10,20,"Lucy",True,"Hello"]

#Displaying a list
print(marks)

#Knowing the type of variable and accessing List elements
print(type(marks))
print(type(marks[3]))
print(marks[1:3])
print(marks[3:])

#finding if element is present in list or not
if "Lucy" in marks:
   print("yes")

#Traversing in list using for loop
for i in marks:
    print(i)
    
#Deleting elements in List by using
#1)del keyword:-
del marks[1]
print(marks)

#2)pop() method:-
marks.pop()
print(marks)

#3)remove() method:-
marks.remove(True)
print(marks)

#4)clear() method:-
marks.clear()
print(marks)

#Updating List :-

#creating a list using inbuild range function
newL=list(range(1,5))
print(newL)

#1)insert() :-adds the element at specified index and specified value
newL.insert(5,23)
print(newL)

#2)append() :-adds an element to the end of the list
newL.append(45)
print(newL)

#3)extend() :-adds all elemnts of one list to another
newL2=["hii","okay",78]
newL.extend(newL2)
print(newL)

#4)index() :-It returns the first index of the searched_element
newL.insert(4,78)
print(newL)

f=newL.index(78)
print(f)

#5)reverse() :-it reverses the index of the items in the list
print("Before reversing =",newL)
newL.reverse()
print("After reversing =",newL)

#6)sort() :-it sorts the list elements in ascending or decending order
num=[74,34,64,26,94,64,62,60]
print("Before Sorting =",num)
num.sort()
print("After Sorting =",num)
num.sort(reverse=True)
#descending order sorting :- sort(reverse=True)

#operator * :-
newList=newL*2
print(newList)

#Concatenation operator +
newList=newL+["new","added"]
print(newList)

#count() :-counts the number of times the item occured in the list
c=num.count(64)
print(c)

#min() and max()
print("Minimum number in list is:",min(num))
print("Maximum number in lis is :",max(num))

#sum()
print("Sum is :",sum(num))
