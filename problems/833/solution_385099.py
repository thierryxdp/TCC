def conta_numero(numero:int,matriz:list) -> int:
    """comentário"""
    vezes = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                vezes += 1
    return vezes