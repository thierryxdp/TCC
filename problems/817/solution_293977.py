def acima_da_media (lista):
    b = lista[:]
    media = sum(lista) / len(lista)
    list.append(lista, media)
    list.sort(lista)
    a = list.index(lista, media)
    if media not in b:
        return lista[a+1:]
    elif media in b:
        return lista[a+2:]