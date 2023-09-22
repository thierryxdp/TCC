def acima_da_media(lista):
    media= int(sum(lista)/len(lista))
    listanova=lista+[media]
    list.sort(listanova)
    listafinal=listanova[media:]
    return listafinal