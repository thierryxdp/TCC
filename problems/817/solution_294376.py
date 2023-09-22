def maiores (lista,n):
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    return lista[a+1:]
def acima_da_media(lista):
    n=ceil((sum (lista))/len (lista))
    return maiores(lista,n)