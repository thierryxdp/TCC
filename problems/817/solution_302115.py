def acima_da_media(lista_notas):
    media = sum(lista_notas) / len(lista_notas)
    lista_notas.append(media)
    organizaLista = sorted(lista_notas)
    indiceMedia = organizaLista.index(media)

    if media not in organizaLista:
        lista_notas.append(media)

    return organizaLista[indiceMedia + 1:]