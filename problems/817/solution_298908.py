def acima_da_media(lista):
    if len(lista) == 1:
        list.clear(lista)
        return lista
    elif:
        media = sum(lista)/len(lista)
        list.append(lista,media)
        list.sort(lista)
        listafinal = list.index(lista,media)
        return lista[listafinal+1:] 
    elif media in lista:
        list.del(lista,[listafinal])
        return[listafinal+1:]