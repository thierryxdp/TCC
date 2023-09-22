def acima_da_media(lista):
    media_notas = sum(lista)/len(lista)
    list.append(lista,media_notas)
    list.sort(lista)
    posicao=list.index(lista,media_notas)
    list.remove(lista, media_notas)
    return (media_notas, lista[posicao:])