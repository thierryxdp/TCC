def eh_mult(x,n):
    return x%n == 0

def filtra_multiplos(ls,n):
    r = []
    for x in ls:
        if eh_mult(x,n):
            r.append(x)
    return r