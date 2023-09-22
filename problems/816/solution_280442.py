def maiores(lista, n):
    lista1 = []
    for i in lista:
        if i > n:
            list.insert(lista1, 0, i)
    lista1.sort()

    return lista1


def acima_da_media(lista):
    media = sum(lista) / len(lista)
    return maiores(lista, media)