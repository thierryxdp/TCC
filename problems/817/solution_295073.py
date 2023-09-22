def acima_da_media(lista):
    '''Retorna uma lista com as notas que ficaram acima
    da média;
    list -> list'''
    list.sort(lista)
    pos_media = list.index(lista, 7)
    return lista[pos_media:-1]