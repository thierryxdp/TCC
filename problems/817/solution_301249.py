from math import floor

def maiores(lista,n):
    limite = len(lista)
    i = 0
    while i < limite:
        if lista[i] < n:
            del lista[i]
            limite = limite - 1
        else:
            i = i + 1
    list.sort(lista)
    return lista

def acima_da_media(lista):
    media = sum(lista) / (len(lista) + 1)
    acima = maiores(lista,media_arr))
    


acima_da_media([8,5,7,10,4,6,9,10])