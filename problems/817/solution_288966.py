def acima_da_media(notas):
    '''acima_da_media recebe uma lista e devolve outro lista
    a funcao acima_da_media recebe uma lista e devolve uma nova lista com
    os valores maiores que a media entre elas
    list --> list'''
    somaelem=sum(notas)
    media=somaelem//len(notas)
    list.sort(notas)
    return notas[list.index(int notas,media)+1:]