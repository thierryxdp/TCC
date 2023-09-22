def faltante(n):
    prox=1
    if 1 not in n:
        return 1
    while prox<len(n):
        if n[prox] != prox + 1:
            return n[prox]-1
        prox=prox+1
    return n[prox-1]+1