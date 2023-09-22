def media_matriz(matriz):
    '''Função que tendo como entrada uma matriz, retorna a média de todos
    os numeros da matriz.
    list -> float'''
    soma= 0
    qtd= len(matriz)*len(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma= soma + matriz[i][j]
    media= soma/qtd
    return round(media,2)