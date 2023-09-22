def conta_numero(n, matriz):
    """
    Retorna quantas vezes o número "n" apareceu em uma matriz
    int, list -> int
    """

    s = 0

    for i in range(len(matriz)):
        for j in matriz[i]:
            if j == n:
                s += 1

    return s