def acima_da_media(lista):
    if len(lista) == 1:
        list.clear(lista)
        return lista
    else:
        media = sum(lista)/len(lista)
        list.append(lista,media)
        list.sort(lista)
        listafinal = list.index(lista,media)
        x = list.remove(lista, listafinal)
        return x[listafinal+1]