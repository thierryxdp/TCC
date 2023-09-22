def conta_numero(numero, matriz):
    """Funcao que dado um numero e uma matriz retorna quantas vezes
    o numero aparece na matriz
    int, list --> int"""
    vezes = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero == matriz[i][j]:
                vezes = vezes + 1
    return vezes