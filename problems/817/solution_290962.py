def acima_da_media(lista):
    media= sum(lista)/len(lista)
    listanova=lista+[media]
    list.sort(listanova)
    listafinal=listanova[:]
    return listafinal