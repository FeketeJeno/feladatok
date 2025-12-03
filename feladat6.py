#Kérj be 5 darab számot, tedd őket listába, majd számold ki az átlagukat.
lista=[]
#szam1=int(input("Kérem az első számot: "))
#szam2=int(input("Kérem a második számot: "))
#szam3=int(input("Kérem a harmadik számot: "))
#szam4=int(input("Kérem a negyedik számot: "))
#szam5=int(input("Kérem az ötödik számot: "))

#lista=[szam1,szam2,szam3,szam4,szam5]
#print(f"A megadott számok átlaga: {(szam1+szam2+szam3+szam4+szam5)/5}")
ossz=0
for i in range(5):
    lista.append(int(input(f"Kérem a {i+1}. számot! ")))

                           
for i in range(5):
    ossz = ossz + lista[i]

print(f"Az öt szám összege: {ossz}.")

