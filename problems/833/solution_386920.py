def conta_numero(n,m):
    d=0
    for i in range len(m):
        for f in range len(m[0]):
            if m[i][f]==n:
                d=d+1
    return d