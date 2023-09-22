def conta_numero(numero, matriz):
    """Dado um número inteiro e uma matriz de tamanho qualquer, conta e retorna quantas vezes
    aquele número aparece na matriz; int, list -> int"""
    contador1 = 0
    while contador1 < len(matriz):
        contador2 = 0
        while contador2 < len(matriz[contador1]):
            if matriz[[contador2]] == numero:
                numerov += 1
            contador2 += 1
        contador1 += 1
    return numerov