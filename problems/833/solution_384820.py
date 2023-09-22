def conta_numero(n, matriz):
    """ Função que dado um numero e uma matriz de numeros
    inteiros, conta e retorna a quantidade de vezes que o
    numero aparece
    Entrada: lista
    Saida: int """
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == n:
                total = total + 1
    return total