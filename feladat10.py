#Írj programot, ami egy listát buborékrendezéssel növekvő sorrendbe tesz .
lista=[]
def bubble_sort(lista):
    x=len(lista)
    for i in range(x - 1):
        for j in range(0, x - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1],lista[j]
    return lista
rendezetlen = [5, 1, 4, 2, 8]
print(f"A számok az alábbi sorrendben vannak az előre megadott tömbben: {rendezetlen}")
rendezett = bubble_sort(rendezetlen)
print("A számok növekvő sorrendben:", rendezett)
