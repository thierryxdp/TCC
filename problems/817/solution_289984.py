def acima_da_media(notas):
    '''Função que retorna uma lista ordenada com as notas que ficaram acima da média'''
    posicao=sum(notas)/len(notas)
    media=notas[posicao+1:]
    return media