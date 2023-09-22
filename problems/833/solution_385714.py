def conta_numero(numero,matriz):
    """ Função que dado um número inteiro e uma matriz
        de inteiros de tamanho qualquer, conta e retorna
        quantas vezes aquele número aparece na matriz;
        int, list[list] -> int"""
    quantidade_vezes = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                quantidade_vezes = quantidade_vezes + 1
    return quantidade_vezes