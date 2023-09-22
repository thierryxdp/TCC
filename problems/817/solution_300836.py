def acima_da_media(lista,n):
    list.insert(lista,0,n)
    list.sort(lista)
    del lista[0:list.index(lista,n)+1]
    return lista