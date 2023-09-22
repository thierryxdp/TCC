def media_matriz(matriz):
    '''uma função que dada uma matriz, retorna a média de todos os números da matriz
    com duas casas decimais de precisão.
    matriz -> float'''
    contador = 0
    for a in matriz:
        for b in a:
            contador += b
    quant = len(matriz)*len(matriz[0])
    total = round(contador/quant, 2)
    return total