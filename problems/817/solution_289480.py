def acima_da_media(lista):
    """funcao que retorna uma lista ordenada com as notas da turma acima da media;
    list -> list"""

    media_total = sum(lista)/len(lista)

    if media_total in lista:
        lista.sort()
        posicao = lista.index(media_total)
        return lista[posicao+1:]

    else:
        lista.append(media_total)
        lista.sort()
        posicao = lista.index(media_total)
        return lista[posicao+1:]