def acima_da_media(lista):
    media = (sum(lista))/len(lista)
    list.append(lista,media)
    list.sort(lista)
    return lista[media:]