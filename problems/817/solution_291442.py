def acima_da_media(lista):
    list.sort(lista)
    a=list.index(lista, 6)
    list.del(lista[0:a])
    return lista