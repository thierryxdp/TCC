def media_matriz(matriz):
    '''Dada uma matriz de inteiros (não vazia), retorna a média de todos
    os números da matriz (com 2 casas decimais de precisão)
    
    list -> float'''

    numLinhas = len(matriz)
    numColunas = len(matriz[0])

    numElementos = numLinhas*numColunas
    somaElementos = 0

    for i in range(numLinhas):
        for j in range(numColunas):
            somaElementos = somaElementos + matriz[i][j]

    media = somaElementos/numElementos

    return round(media, 2)