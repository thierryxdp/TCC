def acima_da_media(lista):
    nullist = []
    orlist = lista[:]
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    ind = list.index(lista,media)
    if media in orlist:
        return lista[ind+2:]
    elif len(lista) > 2:
        return lista[ind+1:]
    else:
        return nullist