def acima_da_media(lista):
    """ lista -> lista  - Faz- se o cálculo da média através formula soma / tamanho da lista
    se a media estiver na lista, organizo a lista e a parto a partir da posicao da media.
    se ela não estiver na lista, eu adiciono, coloco em ordem e corto a partir do termo ordenado +1
    que vai me dar a lista com os valores maiores"""
    tamanho_lista = len(lista)
    media = int(sum(lista)/tamanho_lista)
    if media in lista:
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
        return lista[posicao+1:]