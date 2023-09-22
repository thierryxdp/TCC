def media_matriz(matriz):
    '''Função que retorna a média de todos os números da matriz, dado a matriz;list->float'''
    quantidade=len(matriz)*len(matriz[0])
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma=soma+matriz[i][j]
    media=soma/quantidade
    return round(media,2)