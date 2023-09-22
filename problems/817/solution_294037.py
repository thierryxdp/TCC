def acima_da_media(lista):
    """..."""
    media = sum(lista)/ len(lista)
    if media not in lista:
        list.append(lista,media)
    list.sort(lista,media)
    indice = list.index(lista,media)
    lista_media = lista[indice+1:]
    
    return lista_media