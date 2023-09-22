def media_matriz(matriz):
    '''função que retorna a média de todos os números da matriz'''
    media = 0
    for x in range (len (matriz)):
        for y in range (len(matriz[x])):
            media = media + matriz[x][y]
            linha = len(matriz)
            coluna = len(matriz[0])
            z = linha*coluna
    return round(media/z,2)