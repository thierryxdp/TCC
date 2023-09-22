def acima_da_media(lista):
    a=(sum(lista))/(len(lista))
    list.insert(lista,0,a)
    list.sort(lista)
    return lista[list.index(lista,a)+2:]