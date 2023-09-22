def acima_da_media:
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    posicao = list.index(media)
    lista1 = lista[posicao+1:]
    return lista1