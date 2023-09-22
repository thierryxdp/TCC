def conta_numero(numero, matriz):
    """Recebe um número e uma matriz, e conta e retorna o numero de vezes que o
    numero aparece na matriz
    int, list -> int"""
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                contador += 1
    return contador