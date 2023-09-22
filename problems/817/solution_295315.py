def acima_da_media(lista):
    lista.append(7)
    lista.sort()
    x=lista.index(7)
    return lista[x+1:]