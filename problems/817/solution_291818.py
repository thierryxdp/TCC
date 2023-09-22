def acima_da_media(lista):
    ''' '''
    media = sum(lista) / len(lista)
    list.append(lista,media)
    list.sort(lista)
    indice = list.index(lista,media)
    if lista[indice] = media:
        lista = lista[:indice+1:-1]
    else:
        lista = lista[:indice:-1]
    list.reverse(lista)
    return lista