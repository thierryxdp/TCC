def maiores(lista,n):
    list.append(lista, n)
    list.sort(lista)
    A = lista.index(n)
    del lista[0:A+1]
    return lista

import math

def acima_da_media(lista1):
    B = math.ceil(sum(lista1)/len(lista1))
    if len(lista1) < 1:
     return []
    else:
     return maiores(lista1,B)