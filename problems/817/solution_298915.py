def acima_da_media(lista):
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    listafinal = list.index(lista,media)
    if len(lista) == 1:
        list.clear(lista)
        return lista
    elif media in lista:
        list.remove(lista,media)
        return lista[listafinal+1:]
    else:
        return lista[listafinal+1:]