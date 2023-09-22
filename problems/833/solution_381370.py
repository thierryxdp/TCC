def conta_numero(numero, matriz):
    """Esta função recebe uma matriz e um numero, e retorna a 
    quantidade de vezes que o numero inserido aparece na matriz.
    Recebe: int, list
    Retorna: int"""
    quantidade = 0
    posmat = 0
    for posmat in range(len(matriz)):
        for i in range(len(matriz[posmat])):
            if numero == (matriz[posmat][i]):
                quantidade = quantidade + 1
            if numero != (matriz[posmat][i]):
                quantidade = quantidade + 0
    return quantidade