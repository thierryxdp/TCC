def acima_da_media(lista):
    media = int(sum(lista))/int(len(lista))
    list.append(lista,media)
    list.sort(lista)
    return lista[list.index(lista,media):]