def media_matriz(matriz):
    '''
    Funcaoo que recebe uma matriz e
    retorna a media de todos os numeros da matriz.
    list -> float
    '''
    soma = 0
    elem = 0
    for i in range(len(matriz)):
        lista_linha =  matriz[i]
        for j in range(len(lista_linha)):
            soma = soma + matriz[i][j]
            elem = elem + 1
    media = soma/elem
    return round(media, 2)