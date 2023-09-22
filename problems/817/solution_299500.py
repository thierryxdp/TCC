def acima_da_media(lista):
    media = sum(lista)/len(lista)
    list.append(lista, media)
    list.sort(lista)
    n = list.index(lista, media)
    y = 2
    for n in range(y):
        list.remove(lista, media)
    return lista[n :]