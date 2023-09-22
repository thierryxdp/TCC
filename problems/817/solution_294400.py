import math
def maiores (lista,n):
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    return lista[a+1:]
def acima_da_media(lista):
    if len (lista)%2!=0:
        n=math.ceil(len (lista)/2)
        return maiores(lista,n)
	else:
        n=len (lista)//2
        return maiores(lista,n+1)