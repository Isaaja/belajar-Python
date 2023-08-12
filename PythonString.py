#Get the character at position 1 (remember that the first character has the position 0):
x = "isa iant maulana"
print(x[1])

#Looping Through a String
for x in "Isa iant":
    print(x)

#String Length
#To get the length of a string, use the len() function.
x = "isa"
print(len(x))

#Check String bisa menggunakan in
x = "isa iant"
print("in" in x) #false

#contoh lagi
x = "isa iant"
if "iant" in x:
    print("True") #True

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
x = "isa iant"
print("iant" not in x)

"""
Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
x = "isaiant"
print(x[2:5]) #menampilkan karakter huruf index 2 - 4 
print (x[:5]) #menampilkan karakter huruf index awal-5
print (x[5:]) #menampilkan karakter huruf index 5-akhir
#Note: The first character has index 0.

#Upper Case (menjadikan sebuah kalimat menjadi huruf kapital)
x = "Isa Iant"
print (x.upper())
#Lower Case (menjadikan sebuah kalimat menjadi huruf kecil)
x = "ISA IANT"
print (x.lower())
#Remove Whitespace
txt = " Hello World "
x = txt.strip()
print(x) #kok gangaruh ye
#Replace String (The replace() method replaces a string with another string:)
x = "isa iant"
print(x.replace("i","r"))
#Split String (Metode split() membagi string menjadi substring jika menemukan instance pemisah:)
x = "isa iant"
print(x.split(','))
# String Concatenation
x = "isa"
y = " iant"
z = x + y
print(x+y)
#String Format
x = "Data Scientist"
y = "Saya siap jadi seorang {}"
print(y.format(x))

x = "Data Scientist"
y = "Data Analyst"
z = "Saya siap jadi seorang {} dan {}"
print(z.format(x,y))

#Escape Characters

x = "Isa iant Maulana \"adalah\" Seorang Data Scientist"
print(x) #untuk menambahkan petik 2 didalam string

