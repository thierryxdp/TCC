def media_matriz(matriz):
    '''função quedada matriz nao vazia calcula a média de todos os termos presentes nela
    list->float'''
    soma=0
    media=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma += matriz[i][j]
            media = soma/((i+1)*(1+j))
    return round(media,2)