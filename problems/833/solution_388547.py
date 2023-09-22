def conta_numero(numero,matriz):
    """Retorna quantas vezes um numero dado
    como parametro aparece na matriz
    int, list -> int"""
    valor = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                valor += 1
    return valor