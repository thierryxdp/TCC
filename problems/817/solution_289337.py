def acima_da_media(lista):
    media = sum(lista)/len(lista)
    lista.append(media)
    lista.sort
    posicao = lista.index(media) + lista.count(media)
    return lista[posicao:]