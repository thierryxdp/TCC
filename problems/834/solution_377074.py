def media_matriz(matriz):
    '''Retorna a media de todos os elementos de uma matriz'''
    #list -> float
    elementos = []
    for linha in matriz:
        for Aij in linha:
            list.append(elementos, Aij)
    soma = sum(elementos)
    total = len(matriz)*len(matriz[0])
    media = soma/total
    return round(media, 2)