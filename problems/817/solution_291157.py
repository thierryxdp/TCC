def acima_da_media(lista):
    list.append(lista,7)
    list.sort(lista)
    x=list.index(lista,7)
    lista=lista[x:]
    del lista[0]
    return lista