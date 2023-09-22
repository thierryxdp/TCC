def acima_da_media(lista):
    
#retorna uma lista ordenada com as notas que ficaram acima da média, dada a lista como entrada

    soma = sum(lista)
    totalTermos = len(lista)
    media = soma // totalTermos
    lista.append(media)
    list.sort(lista)
    posicao = lista.index(media)

    return lista[posicao+lista.count(media):]