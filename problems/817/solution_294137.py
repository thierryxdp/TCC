import math
def acima_da_media(lista):
    n = sum(lista)/len(lista)
    n1 = math.ceil(n)
    list.append(lista,n)
    list.sort(lista)
    a = list.index(lista,n)
    return lista[a+1:]