def acima_da_media(lista):
    tamanho = len(lista)
    media = sum(lista)/tamanho
    lista2 = sorted(lista)
    posicao = lista2.index(media)
    return media