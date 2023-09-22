def acima_da_media(lista):
    import math
    media= math.ceil((sum(lista)/len(lista)))
    listanova=lista+[media]
    list.sort(listanova)
    posicao=list.index(listanova,media)
    lista_q=listanova[posicao:]
    listafinal=list.remove(lista_q,media)
    return lista_q