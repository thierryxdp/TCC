def acima_da_media(lista):
    list.sort(lista)
    n = sum(lista)/2
    x = list.index(lista,n)
    return lista[x+1:]