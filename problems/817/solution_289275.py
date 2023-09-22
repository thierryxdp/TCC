def acima_da_media(lista):
    '''Retorna uma lista apenas com as notas acima da da media;
    list -> list'''
    media = (sum(lista))/(len(lista)) + 0.000000001
    list.append(lista,media)
    list.sort(lista)
    return lista[list.index(lista,media)+1:]