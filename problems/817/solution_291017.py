def acima_da_media(lista):
    import math
    media= math.ceil((sum(lista)/len(lista)))
    listanova=lista+[media]
    list.sort(listanova)
    posicao=list.index(listanova,media)
    listafinal=listanova[posicao:]
    list.remove(listafinal,media)
    if media==(sum(lista)/len(lista)):
        return listafinal[1:]
    else:
        return listafinal