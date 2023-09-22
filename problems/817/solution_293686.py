def acima_da_media(lista):
    s = sum(lista)
    l = len(lista)
    n = s // l
    list.sort(lista)
    a = list.index(lista,n)
    return lista[a+1:]