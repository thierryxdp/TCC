def acima_da_media(lista):
    """Função que dada uma lista, mostra os números acima da média"""
    """list -> list"""
    media = (sum(lista)) / len(lista)
    if len(lista) < 2:
        return []
    elif (media in lista) == True:
        lista.sort()
        posicao = lista.index(media)
        return lista [posicao+1:]
    else:
    	lista.append(media)
        lista.sort()
        posicao = lista.index(media)
        return lista[posicao+1:]