def acima_da_media(lista):
    '''Retorna uma lista com as notas que ficaram acima
    da média;
    list -> list'''
    media = sum(lista)
    list.append(lista,media)
    list.sort(lista)
    posicao_media= list.index(lista,media) / len(lista)
    new_list= lista[posicao_media+1:]
    return new_list