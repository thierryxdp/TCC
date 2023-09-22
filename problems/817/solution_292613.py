def acima_da_media(lista):
    media=sum(lista)/len(lista)
    if media in lista:
        del lista[lista.index(media)]
    lista.append(media)
    lista.sort()
    lista=lista[lista.index(media)+1:]