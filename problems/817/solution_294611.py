def acima_da_media(lista):
    tamanho_lista = len(lista)
    media = int(round(sum(lista)/tamanho_lista,0))
    if media in lista:
        lista.sort()
        posicao = lista.index(media)
        return lista[posicao+1:]
    elif:
        lista.append(media)
        lista.sort()
        posicao = lista.index(media)
        return lista[posicao+1:]