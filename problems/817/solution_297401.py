def acima_da_media(lista):
    media = sum(lista) // len(lista)
    list.append(lista,media)
    list.sort(lista)
    posicao = list.index(lista,media)
    del lista [:posicao+1]
    media in lista list.remove(lista, media)
    return lista