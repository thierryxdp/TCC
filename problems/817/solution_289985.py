def acima_da_media(notas):
    '''Função que retorna uma lista ordenada com as notas que ficaram acima da média'''
    media=sum(notas)/len(notas)
    return notas[media+1:]