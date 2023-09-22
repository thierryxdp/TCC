def acima_da_media(lista):

    soma = sum(lista)
    totalTermos = len(lista)
    media = soma // totalTermos
    lista.append(media)
    list.sort(lista)
    posicao = lista.index(media)

    return lista[posicao+lista.count(media):]


print(acima_da_media([0,2,4,6,9]))