def maiores(t,n):
    """anndadaid"""
    list.append(t,n)
    list.sort(t)
    maiores = []
    proximo = 0
    while proximo <len(t):
        if t[proximo] > n:
            list.append(t[proximo],maiores)
        proximo = proximo + 1
    return maiores