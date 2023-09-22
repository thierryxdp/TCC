def acima_da_media (lista):
    media=(sum(lista)//len(lista)) + 0.1
    lista.append (media)
    lista.sort()
    lista= lista[lista.index(media) +1:]
    return lista