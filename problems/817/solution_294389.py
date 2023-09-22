import math
def maiores (lista,n):
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    return lista[a+1:]
def acima_da_media(lista):
    n=len (lista)//2+1
    return maiores(lista,n)