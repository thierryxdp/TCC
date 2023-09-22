def conta_numero(n, m):
    """retorna quantas vezes o numero aparece na matriz"""
    l = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            l.append(matriz[i][j])
    return l.count(n)