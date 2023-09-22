def acima_da_media(lista):
    media = sum(lista)/len(lista)
    if len(lista) == 1:
        list.clear(lista)
        return lista
    elif media in lista:
        list.del(lista,[listafinal])
        return[listafinal+1:]
    else:
        list.append(lista,media)
        list.sort(lista)
        listafinal = list.index(lista,media)
        return lista[listafinal+1:]