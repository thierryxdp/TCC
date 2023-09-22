def acima_da_media(lista):
    media = sum(lista)/len(lista)
    lista = lista+[media]
    list.sort(lista)
    index = list.index(lista, media) + list.count (lista, media)
    notas_acima_media: lista[index:]
    return notas_acima_media