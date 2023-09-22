def acima_da_media(lista):
    lista.insert(lista,lista)
    lista.sort()
    indice = lista.index(lista)
    return lista[indice+1:]