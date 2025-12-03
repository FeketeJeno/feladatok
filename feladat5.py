#Kérj be egy N számot, majd számold ki a 1..N közötti számok összegét.

osszSzam = 0
szam1 = int(input("Kérek egy számot:"))
for i in range(1,szam1 + 1):
    osszSzam = osszSzam + i
print(f"A számok összege: {osszSzam}")



