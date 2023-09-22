def acima_da_media:
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    lista1 = lista[list.index(media)+1 :]
    return lista1