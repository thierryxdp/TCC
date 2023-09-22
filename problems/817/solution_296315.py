def acima_da_media(lista):
    '''retorna uma lista com as notas acima da media; list -> list'''
    media = sum(lista)/len(lista)
    b = list.append(lista, media)
    c = list.sort(lista)
    d = list.index(lista, media)
    if lista[media] == lista[int(list.index(lista, media)) + 1]:
        return lista[d+2:]
    else:
        return lista[d+1:]