def conta_numero(numero,matriz):
    """função que conta e retorna quantas vezes o número n aparece na matriz M
    int, list -> int"""
    qnt = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                qnt += 1
    return qnt