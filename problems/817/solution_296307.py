def acima_da_media(lista):
    '''retorna uma lista com as notas acima da media; list -> list'''
    media = sum(lista)/len(lista)
    b = list.append(lista, media)
    c = list.sort(lista)
    d = list.index(lista, media)
    if len(lista)/2 < media:
        return lista[d+1:]
    if len(lista/2) > media:
        return lista[d+2:]