def acima_da_media(notas):
    '''função que dada uma lista com as notas, retorna uma lista ordenada com as notas que ficaram acima da média'''
    media = sum(notas)/len(notas)
    maiores(notas,media)
    return maiores (notas, media)