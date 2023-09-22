def conta_numero(n ,m):
    contador = 0
    i = 0
    j = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            if m[i][j] == n:
                contador += 1
            j += 1
        i += 1
    return contador