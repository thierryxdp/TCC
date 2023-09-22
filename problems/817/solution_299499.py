def acima_da_media(lista):
    media = sum(lista)/len(lista)
    list.append(lista, media)
    list.sort(lista)
    n = list.index(lista, media)
    y = list.count(lista, media)
    for n in range(y):
        list.remove(lista, media)
    return lista[n :]