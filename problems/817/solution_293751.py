def acima_da_media(lista):
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    ind = list.index(lista,media)
    listaf=lista[ind+1:]
    return listaf