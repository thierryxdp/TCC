import math
def acima_da_media(lista):
    n = sum(lista)/len(lista)
    list.append(lista,n)
    list.sort(lista)
    a = list.index(lista,n,3)
    return lista[a+1:]