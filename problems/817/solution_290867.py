def acima_da_media(lista):
    a=(sum(lista))/2
    list.insert(lista,0,a)
    list.sort(lista)
    return lista[list.index(lista,a)+1:]