def acima_da_media(notas):
    '''acima_da_media recebe uma lista e devolve outro lista
    a funcao acima_da_media recebe uma lista e devolve uma nova lista com
    os valores maiores que a media entre elas
    list --> list'''
    totalelem=sum(notas)
    media=totalelem//len(notas)
    list.sort(notas)
    return notas[list.index(notas,media):]