def conta_numero (n, matriz):
    """Retorna a quantidade de vezes que um número aparece na matriz..
    Entrada: int, list(list)
    Saída: int
    """
    contador= 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] = n:
                contador += 1
    return contador