#Python List
thislist = ["mangga", "jagung", " pepaya"]
print(thislist)
#Len
thislist = ["mangga", "jagung", " pepaya"]
print(len(thislist))
#Type
thislist = ["mangga", "jagung", " pepaya"]
print(type(thislist))
#Access Item
thislist = ["mangga", "jagung", " pepaya"]
print(thislist[1])
#Negative Indexing
thislist = ["mangga", "jagung", " pepaya"]
print(thislist[-1])
#Range of Indexing
thislist = ["mangga", "jagung", " pepaya"]
print(thislist[0:2])
#Check if item exist
thislist = ["mangga", "jagung", " pepaya"]
if "mangga" in thislist:
    print("ada")
else:
    print ("tidak ada")
#Change item Value
thislist = ["mangga", "jagung", " pepaya"]
thislist[1] = ["anggur"]
print(thislist)
#Insert
thislist = ["mangga", "jagung", " pepaya"]
thislist.insert(2,"anggur")
print(thislist) #To insert a new list item, without replacing any of the existing values, we can use the insert() method.
#Append Items
thislist = ["mangga", "jagung", " pepaya"]
thislist.append("anggur")
print(thislist)#To add an item to the end of the list, use the append() method:
#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #to append elements from another list to the current list, use the extend() method.
#Add any Iterable 
thislist = ["apple", "banana", "cherry"]
tropical = ("mango", "pineapple", "papaya")
thislist.extend(tropical)
print(thislist)#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #remove banana
#Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist) #remove index 0
#Clear the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #The clear() method empties the list. The list still remains, but it has no content.
#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for x in range(len(thislist)):
    print(thislist[x])#Use the range() and len() functions to create a suitable iterable.
#Using a While loop
thislist = ["apple", "banana", "cherry"]
x = 0
while x < len(thislist):
    print(thislist[x])
    x=x+1
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.






