#Adj meg egy listát tetszőleges egész számokkal, majd írd ki
#a legnagyobb számot
#a legkisebb számot

tomb=[10,4,8,15,6]

max = tomb[0]
for i in range(len(tomb)):
    if tomb[i] > max:
        max = tomb[i]

print(f"A tömb legnagyobb eleme: {max}")

min = tomb[0]

for i in range(len(tomb)):
    if tomb[i] < min:
        min = tomb[i]

print(f"A legkisebb eleme a tömbnek a {min}.")

