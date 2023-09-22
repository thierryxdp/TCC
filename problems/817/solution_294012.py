def acima_da_media(lista):
    media_notas = sum(lista)/len(lista)
    list.append(lista,media_notas)
    list.sort(lista)
    int.posicao =list.index(lista, media_notas)+ 1
    return (lista[posicao:])