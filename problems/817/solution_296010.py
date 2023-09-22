def acima_da_media(lista):
    """ A função retorna uma lista com notas acima da media;
    list -> list """
    nullist = []
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    ind = list.index(lista,media)
    if 0 in lista:
        return lista[ind+2:]
    elif len(lista) > 2:
        return lista[ind+1:]
    else:
        return nullist