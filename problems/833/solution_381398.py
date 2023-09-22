def conta_numero(n,matriz):
    """Esta é a função que dada uma matriz e um número retorna quantas vezes esse número aparece na matriz, list, int -> int"""
    vezes = 0

    for l in range(len(matriz)):
        for c in range(len(matriz[l])):

            if matriz[l][c] == n:
                vezes = vezes + 1

    return vezes