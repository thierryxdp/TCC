def conta_numero(n,m):
    z=0
    for i in m:
        quantidade=i.count(n)
        z=quantidade+z
    return z