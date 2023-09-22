def maiores(lista,n):
    list.append(lista, n)
    list.sort(lista)
    A = lista.index(n)
    del lista[0:A+2]
    return lista

import math

def acima_da_media(lista1):
    B = math.floor(sum(lista1)/len(lista1))
    return maiores(lista1,B)