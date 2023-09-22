def acima_da_media(lista):
    tamanho_lista = len(lista)
    media = int(sum(lista)/tamanho_lista)
    return media
    """if media in lista:
        lista.sort()
        posicao = lista.index(media)
        if lista[0] == media:
            lista.pop(0)
        lista.pop(posicao)
        return lista[posicao:]
    else:
        lista.append(media)
        lista.sort()
        posicao = lista.index(media)
        return lista[posicao+1:]"""