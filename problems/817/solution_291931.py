def acima_da_media(lista):
    """..."""

    
    media = (sum(lista)/len(lista))
    list.append(lista,media)
    list.sort(lista)
    x = list.index(lista,media)

    return lista[x+1:]