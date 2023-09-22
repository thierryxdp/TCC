def acima_da_media(lista):
    '''Retorna uma lista apenas com as notas acima da da media;
    list -> list'''
    media = int((sum(lista))/(len(lista)))
    list.append(lista,media)
    list.sort(lista)
    return lista[list.index(lista,media)+1:]