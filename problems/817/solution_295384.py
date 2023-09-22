def acima_da_media(lista):
    media = (sum(lista))/len(lista)
    list.append(lista,media)
    list.sort(lista)
    indice = int(media)
    return lista[indice:]