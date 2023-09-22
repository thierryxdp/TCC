def acima_da_media(media):
    media = int(sum(lista)/len(lista))
    indMedia=lista.index(media)
    numerolist=lista[indMedia+1:].copy()
    lista.append(media)
    lista.sort()
    if media in numerolist:
        del numerolist[0]
    return numerolist