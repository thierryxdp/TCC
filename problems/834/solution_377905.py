def media_matriz(matriz):
    '''Função eu retorna a média de todos os números de uma
    matriz.
    Parâmetros: list -> float'''
    nlin = len(matriz)
    ncol = len(matriz[0])
    contador = 0
    for i in range(nlin):
        for j in range(ncol):
            contador += matriz[i][j]
    return round(contador/(nlin*ncol),2)