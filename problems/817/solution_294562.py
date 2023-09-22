def acima_da_media(lista):
    tamanho_lista = len(lista)
    media = sum(lista)//tamanho_lista
    lista.append(media)
    lista.sort()
    tamanho_lista = len(lista)
    posicao = lista.index(media)
    return lista[posicao:tamanho_lista]