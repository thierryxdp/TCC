def conta_numero(numero, matriz):
    """Esta função recebe uma matriz e um numero, e retorna a 
    quantidade de vezes que o numero inserido aparece na matriz.
    Recebe: int, list
    Retorna: int"""
    quantidade = 0
    for i in range(len(matriz[0])):
        if numero == (matriz[0][i]):
            quantidade = quantidade + 1
        if numero != (matriz[0][i]):
            quantidade = quantidade + 0
    return quantidade