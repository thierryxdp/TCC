def acima_da_media(lista):
    media = sum(lista)/int(lista.count(' '+1))
    list.sort(lista)
    return lista[list.index(lista,media)+1:]