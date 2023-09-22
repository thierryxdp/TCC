def acima_da_media(lista):
    media= int(sum(lista)/len(lista))+1
    listanova=lista+[media]
    list.sort(listanova)
    posicao=list.index(listanova,media)
    listafinal=listanova[posicao:]
    return listafinal