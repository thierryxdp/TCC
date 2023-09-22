def conta_numero(x,y):
    n=0
    for c in y:
        n=n+c.count(x)
    return n