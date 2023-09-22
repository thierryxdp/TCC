def media_matriz(m):
    """Retorna a média de todos os números da matriz.
    list -> int"""
    somafinal=0
    d=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            soma = m[i][j]
            somafinal = somafinal+soma
            d += 1
    somafinal=somafinal/d
    return round(somafinal,2)