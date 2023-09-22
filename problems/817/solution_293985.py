def media2(lista):
    media_notas = sum(lista)/len(lista)
    list.append(lista,media_notas)
    list.sort(lista)
    posicao=list.index(lista,media_notas)+1
    list.remove(lista,media_notas)
    return (media_notas, lista[posicao:])