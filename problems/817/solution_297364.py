def acima_da_media(lista):
    list.sort(lista)
    media = sum(lista) // len(lista)
    posicao = list.index(lista,media)
    del lista [:posicao+1]
    return lista