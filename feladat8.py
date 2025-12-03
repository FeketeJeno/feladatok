#Kérj be egy számot és döntsd el, hogy benne van-e az előre adott listában.
szam = 0

lista = [12,10,5,4,23,88,45,43,33,21]

szam = int(input("Kérem a számot: "))

vane = False

for i in range(len(lista)):
    if lista[i] == szam:
        vane = True
        break

if vane == True:
    print("Van találat.")
else:
    print("Nincs találat.")
