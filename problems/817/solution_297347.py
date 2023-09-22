def acima_da_media(lista):
    list.sort(lista)
    del lista [:2]
    return sum(lista)