def media_matriz(matriz):
    '''recebe uma matriz (não vazia) composta de inteiros e
    retorna a média dos termos da matriz; list(list) -> float'''
    soma = 0
    for i in range(len(matriz)):
        for j in matriz[i]:
            soma += j
    return soma/(len(matriz) * len(matriz[0]))