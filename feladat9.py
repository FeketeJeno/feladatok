#Adott egy lista számokkal. Készíts új listát, amelyben csak a páros számok szerepelnek.
lista = [12, 23, 34, 45, 56, 67, 78, 89, 100]
list = []
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        list.append(lista[i])

print(f"A listában szereplő számok:{lista}")
print(f"A listéban szereplő páros számok?{list}")
