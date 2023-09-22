def acima_da_media(lista):
    list.append(lista,6)
    list.sort(lista)
    x=list.index(lista,6)
    lista=lista[x:]
    del lista[0]
    return lista