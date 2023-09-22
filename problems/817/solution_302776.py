def maiores(lista,n):
    list.append(lista, n)
    list.sort(lista)
    x=list.index(lista,n)
    del lista[x]
    c=lista[x:]
    return c
def acima_da_media(lista):
    x=(sum(lista))/(len(lista))
    z=maiores(lista,x)
    return z