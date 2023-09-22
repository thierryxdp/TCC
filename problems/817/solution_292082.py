def acima_da_media(lista):
    media = sum(lista)/len(lista)
    lista1 = lista+[media]
    list.sort(lista1)
    posicao = list.index(lista1,media)
    return lista1[posicao+1:]