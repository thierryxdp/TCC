def media_matriz(matriz):
    '''
    	Função que faz a média de todos os numeros de uma matriz, não vazia, com precisão de duas casas decimais.
        list -> float
    '''
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma += matriz[i][j]
    return round(soma/(len(matriz)*len(matriz[0])),2)