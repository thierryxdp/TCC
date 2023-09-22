def acima_da_media(lista):
    lista.sort()
    indice = lista.index(lista)
    return lista[indice+1:]