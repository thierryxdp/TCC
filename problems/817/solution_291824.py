def acima_da_media(lista):
    ''' '''
    media = sum(lista) / len(lista)
    list.append(lista,media)
    list.sort(lista)
    indice = list.index(lista,media)
    lista = lista[:indice:-1]
    list.reverse(lista)
    if (media in lista):
        list.remove(lista,media)
    else:
        lista = lista
    return lista