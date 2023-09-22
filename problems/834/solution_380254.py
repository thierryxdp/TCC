def media_matriz(m):
    numerador = 0
    divisor = len(m)*len(m[0])
    for i in range(0, len(m)):
        for j in range(0,len(m[0])):
            numerador += m[i][j]
    resultado = numerador/divisor
    return round(resultado,2)