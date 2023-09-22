import math
def acima_da_media(lista):
    n = sum(lista)/len(lista)
    n1 = n+1
    list.append(lista,n1)
    list.sort(lista)
    a = list.index(lista,n1)
    return lista[a+1:]