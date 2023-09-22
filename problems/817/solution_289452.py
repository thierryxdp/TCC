def acima_da_media(lista):
    lista1 = lista+[5]
    list.sort(lista1)
    posicao = list.index(lista1,7)
    return lista1[posicao+1:]