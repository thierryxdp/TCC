def acima_da_media(lista):
    '''retorna uma lista ordenada, dada uma lista;
    list => list'''
    media = int(sum(lista) / len(lista))
    return maiores(lista, media)