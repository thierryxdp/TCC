def acima_da_media(lista):
    list.append(lista,3)
    list.sort(lista)
    x=list.index(lista,3)
    lista=lista[x:]
    del lista[0]
    return lista