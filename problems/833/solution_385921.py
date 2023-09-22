def conta_numero (numero, matriz):
    """Retorna quantas vezes um numero pararece na matriz . int, list -> int"""
    quantidade = 0
    for i in range (len (matriz)):
        for j in range (len (matriz[i])):
            if matriz[i][j] == numero:
                quantidade = quantidade + 1
    return quantidade