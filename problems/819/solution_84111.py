def multiplo(v, n):
    return (v%n) == 0

def filtraMultiplos(L, n):
    J = []
    for p int L:
        if multiplo(p, n):
            J.append(p)
    return J