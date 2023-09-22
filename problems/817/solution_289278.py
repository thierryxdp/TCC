def acima_da_media(lista):
    media = sum(lista)/len(lista)
    list.sort(lista)
    posicao = list.index(lista,media)
    return lista[(media+1):]