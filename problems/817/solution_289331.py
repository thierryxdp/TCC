def acima_da_media(lista):

    list.sort(lista)
    soma = sum(lista)

    totalTermos = len(lista)
    media = soma//totalTermos
    media = media
    posicao = lista.index(media)


    return lista[posicao+lista.count(media):]

print(acima_da_media([2,5,1,4,3,8,9,7]))