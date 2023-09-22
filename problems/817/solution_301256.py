from math import floor

def maiores(lista,n):
    limite = len(lista)
    i = 0
    while i < limite:
        if lista[i] <= n:
            del lista[i]
            limite = limite - 1
        else:
            i = i + 1
    list.sort(lista)
    return lista

def acima_da_media(lista):
    media = sum(lista) / len(lista) 
    media_arr = round(media)
    acima = maiores(lista,media_arr)
    return acima