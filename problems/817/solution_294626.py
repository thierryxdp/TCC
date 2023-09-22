def acima_da_media(lista):
    tamanho_lista = len(lista)
    media = int(round(sum(lista)/tamanho_lista,0))
    if media in lista:
        lista.sort()
        """if lista[0] == media:
            lista.pop(0)"""
        lista.pop(0)
        posicao = lista.index(media)
        return lista[posicao:]
    else:
        lista.append(media)
        lista.sort()
        posicao = lista.index(media)
        return lista[posicao+1:]