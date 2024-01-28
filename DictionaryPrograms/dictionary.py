#Dictionary Program

dict1={1:"Arun",2:"Jaya",3:"Sonali","work":"project"}

print(dict1)
print(dict1.keys())
print(dict1.values())

#Traversing a dictionary using for
for i in dict1:
    print(i,dict1[i])

#Removing an element from Dictionary

#1]By pop() :-removes item with a provided key and return the key
dict1.pop(2)
print(dict1)

#2]by popitem() :-used to remove and return an arbitary item (key,value) from dictionary
dict1.popitem()
print(dict1)

#3]by del Keyword:-remove individual items or entire dictionary itself.
del dict1[3]
print(dict1)

#4]by clear() :-all items can be removed at once using clear() method
dict1.clear()
print(dict1)

#Adding an item to dictionary

#1]value can be added to pre existing key
d={"one":"Riyaja","two":"Shreyasha",3:"Mohana"}
print(d)
d['two']="ramlala"
print(d)

#2]Adding a whole key-value item to Dictionary
d[4]="Fuguna"
print(d)

#Membership Test :- we can test if a key is in dictionary or not using keyword in.
#Not for values.
print("two" in d)
print(3 in d)

