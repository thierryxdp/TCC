def acima_da_media(lista):
    """..."""

    
    media = (sum(lista)//len(lista))
    list.append(lista,media)
    list.sort(lista)
    x = list.index(lista,media)

    return lista[-1:x+1:-1]