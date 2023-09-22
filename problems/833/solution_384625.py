def conta_numero(n,m):
    """Retorna quantas vezes aquele número aparece na matriz.
    int,list -> int"""
    r = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == n:
                r += 1
    return r