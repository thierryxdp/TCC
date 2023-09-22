def acima_da_media(lista):
    lista.append(5)
    lista.sort()
    i=lista.index(5)
    return lista[i:]