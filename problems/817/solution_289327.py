def acima_da_media(lista):

    list.sort(lista)
    soma = sum(lista)

    totalTermos = len(lista)
    media = soma//totalTermos
    media = media

    posicao = lista.index(media)

    return lista[media+lista.count(media):]