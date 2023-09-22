def acima_da_media(lista):
    nullist = []
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    ind = list.index(lista,media)
    if len(lista) > 2:
        return lista[ind+1:]
    else:
        return nullis