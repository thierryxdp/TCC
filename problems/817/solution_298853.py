def acima_da_media(lista):
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    listafinal = list.index(lista,media)
    if len(lista) == 1:
        return lista[:]
    else:
        return lista[listafinal+1:]