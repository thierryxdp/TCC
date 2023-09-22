def acima_da_media(lista):
    list.sort(lista)
    a=list.index(lista, 6)
    del lista[0:a] 
    return lista