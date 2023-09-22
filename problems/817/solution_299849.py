def acima_da_media(lista):
    media = int(sum(lista)/len(lista))
    
    lista.append(media)
    lista.sort()
    indMedia=lista.index(media)
    numerolist=lista[indMedia+1:].copy()
    if media in numerolist:
        del numerolist[0]
    return numerolist