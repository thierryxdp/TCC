def acima_da_media(lista):
    media = (sum(lista))/len(lista)
    media1 = int(media)
    list.append(lista,media1)
    list.sort(lista)
    posicao = list.index(lista,media1)
    return lista[posicao:]