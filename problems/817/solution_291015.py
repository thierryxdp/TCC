def acima_da_media(lista):
    import math
    media= math.ceil((sum(lista)/len(lista)))
    listanova=lista+[media]
    list.sort(listanova)
    posicao=list.index(listanova,media)
    lista_q=listanova[posicao:]
    list.remove(lista_q,media)
    if media==(sum(lista)/len(lista)):
        return lista_q[1:]
    else:
        return lista_q