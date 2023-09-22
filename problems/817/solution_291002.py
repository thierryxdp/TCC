def acima_da_media(lista):
    import math
    media= math.ceil((sum(lista)/len(lista)))
    listanova=lista+[media]
    list.sort(listanova)
    posicao=list.index(listanova,media)
    listafinal=listanova[posicao:]
    return listafinal