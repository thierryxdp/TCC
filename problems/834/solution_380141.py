def media_matriz(m):
    contador = 0
    acumulador = 0
    i = 0
    j = 0
    if len(m) != 0:
        while i < len(m):
            j = 0
            while j < len(m[i]):
                acumulador += m[i][j]
                contador += 1
                j += 1
            i += 1
        return round((acumulador / contador), 2)