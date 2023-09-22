def media_matriz (matriz):
    '''Dada uma matriz de inteiros não vazia, retorna a média de todos os números na matriz, 
    matriz->float'''
    soma = 0
    for elemento in range(matriz):
        for elem in range(matriz[0]):
            soma = soma + matriz[elemento[elem]]
    return round(soma/(len(matriz) * len(matriz[0])), 2)