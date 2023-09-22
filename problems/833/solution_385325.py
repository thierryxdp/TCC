def conta_numero(numero,matriz):
    '''Função que recebe um número inteiro e uma matriz de inteiros
    de tamanho qualquer como entrada e retorna quantas vezes
    aquele número aparece na matriz. int,list(list)->int'''
    quantidade=0
    for i in range(len(matriz)):
        for j in range(len(matrix[0])):
            if matriz[i][j] == numero:
                quantidade= quantidade + 1
    return quantidade