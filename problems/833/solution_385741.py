def conta_numero(numero, matriz):
    return matriz.count(matriz.count(numero) for numero in matriz)