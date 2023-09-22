def conta_numero(n,m):
    """Retorna quantas vezes aquele número aparece na matriz.
    int,list -> int"""
    r = 0
    for j in range(len(m)):
        for i in range(len(m[i][j])):
            if m[i][j] == n:
                r += 1
    return r