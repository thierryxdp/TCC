def acima_da_media(lista):
    #list->list
    list.sort(lista)
    media = sum(lista)/len(lista)
    sair = len(lista)
    while sair>0:
        if lista[0]<=media:
            list.remove(lista,lista[0])
            sair = len(lista)
        else:
            sair = 0
    return(lista)