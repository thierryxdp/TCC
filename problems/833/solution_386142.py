def conta_numero(numero,matriz):
    """dados um numero inteiro e uma matriz de tamanho qualquer, a função retor-
na quantas vezes o numero apareceu na matriz;
    int, list -> int"""
    vezes = 0
    for i in range(len(matriz)):
        for j in matriz[i]:
            if j == numero:
                vezes = vezes + 1
    return vezes