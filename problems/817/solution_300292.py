def acima_da_media(lista):
    media = sum(lista)//len(lista)
    lista.append(media)
    lista_ordenada = sorted(lista)
    indice_media = lista_ordenada.index(media)
    lista_nova = lista_ordenada[indice_media + 1:].copy()

    if media in lista_nova:
        del lista_nova[0]

    return lista_nova