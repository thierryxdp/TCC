def maiores(lista:list, n:int)->list:
    lista.append(n)
    lista.sort()
    aux = lista.index(n)
    return lista[aux+1:]
from math import ceil
def acima_da_media(lista:list)->list:
    n = ceil(sum(lista)/len(lista))
    return maiores(lista, n)