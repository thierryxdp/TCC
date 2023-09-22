def acima_da_media(notas):
    '''Retorna uma lista ordenada com as notas que ficaram acima da media'''
    
    list.sort(notas)
    x = list.count(notas,)
    media = sum(notas)/x
    
    return media