import math
def acima_da_media(lista):
    n = sum(lista)/len(lista)
    list.append(lista,n+1)
    list.sort(lista)
    a = list.index(lista,n)
    return lista[a+1:]