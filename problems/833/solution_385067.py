def conta_numero(numero, matriz):
    contador = 0
    for lista in range(len(matriz)):
        contador = contador + matriz.count(numero)
    return contador