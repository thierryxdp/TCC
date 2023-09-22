def media_matriz(matriz):
    '''retorna a media dos numeros da matriz. list(list)->float'''
    media = 0
    soma = 0
    linha  = len(matriz)
    coluna = len(matriz[0])
    for x in matriz:
        media += soma/coluna
        for y in matriz[x]:
            soma += y
    media = media/linha
    return media