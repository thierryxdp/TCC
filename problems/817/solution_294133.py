import math
def acima_da_media(lista):
    n = sum(lista)/len(lista)
    n1 = ceil(n)     
    list.append(lista,n1)
    list.sort(lista)
    a = list.index(lista,n)
    return lista[a+1:]