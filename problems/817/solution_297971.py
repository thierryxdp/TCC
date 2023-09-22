def acima_da_media(lista):
    lista.append(6)
    lista.sort()
    index = lista.index(6)
    return lista[index:]