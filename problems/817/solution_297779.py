def acima_da_media(lista):
    media = int(sum(lista))/int(lista.count(' '+1))
    list.append(lista,media)
    list.sort(lista)
    return lista[list.index(lista,media)+1:]