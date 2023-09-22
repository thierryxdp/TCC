def acima_da_media(lista):
    '''Retorna uma lista com as notas que ficaram acima da media
    list -> list'''
    soma=sum(lista)
    numero=len(lista)
    media=(soma/numero)+0.0000000000000001
    lista.append(media)
    lista.sort()
    posicao=list.index(lista,media)
    listafinal=lista[posicao+1:]
    return listafinal