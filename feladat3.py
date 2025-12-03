#Kérj be három számot, és írd ki melyik a legnagyobb.
szam1 = int(input("Kérem az első számot: "))
szam2 = int(input("Kérem a második számot: "))
szam3 = int(input("Kérem a harmadik számot: "))

if szam1>szam2 and szam1>szam3:
    print("Az első szám a legnagyobb.")
elif szam2>szam1 and szam2>szam3:
    print("A második szám a legnagyobb.")
else:
    print("A harmadik szám a legnagyobb.")
    