def acima_da_media(lista):
    soma = sum(lista)
    media = (soma)/(len(lista))
    list.append(lista,media)
    list.sort(lista)
    posicao = list.pop(lista,media)
    del lista[:media+1]
    return posicao