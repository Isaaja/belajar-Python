#Membuat Output
print("Hello coy") 
"""
Ini Komentar
"""
#Membuat Variabel dan perkondisian
x = 5
y = 8
if x > y:
    print("hehe")
if x < y:
    print("hahha")
#Casting
#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)   #x will be '3'
y = int(3)   #y will be '3'
z = float(3) #z will be '3.0'

#Get The Type
x = 4.0
y = "isa"
z = 4

print(type(x))
print(type(y))
print(type(z))

#Variable Names
x = "isa iant"
#Nama variabel tidak boleh diawali dengan angka , - , dan space
# contoh 2x = "isa" 
print(x)

#Many Values to Multiple Variables
x,y,z = "isa", 5 , 4.0

print(x,y,z)
print (x)
print (y)
print (z)
#One Value to Multipe Variables
x = y = z = "Isa ganteng"
print (x)
print (y)
print (z)

#Unpack a Collection
Band = ["Dewa 19", "Peterpan", "Noah"]
x,y,z = Band

print(x)
print(y)
print(z)

#Global Variables
x = "data scientist"
def myfunction():
    x = "data analyst"
    print("Saya akan menjadi seorang " + x)
myfunction()

print("saya akan menjadi seorang " + x)

#Global Keyword
x = "Data Analyst"
def myfunc():
    global x
    x = "Data Scientist"
myfunc()

print ("Saya akan menjadi seorang " +x)

#Type Data
x = ("apple", "banana", "cherry")
print(type(x)) #tuple
x = ["apple", "banana", "cherry"]
print(type(x)) #list
x = {"name" : "John", "age" : 36}
print(type(x)) #dict

#Number

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))