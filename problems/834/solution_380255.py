def media_matriz(matriz):
    m = matriz
    numerador = 0
    divisor = len(m)*len(m[0])
    for l in range(0, len(m)):
        for c in range(0, len(m[0])):
            numerador += m[l][c]
    total = numerador/divisor
    return round(resultado,2)