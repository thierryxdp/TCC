def conta_numero(n,m):
    z=0
    for i in m:
        for h in i:
            if n in h:
                z=z+1
    return z