def eh_mult(x,n):
    return X % n == 0


def filtra_multiplos(ls,n):
    r = []
    for x in ls:
        if eh_mult(x,n):
            lista.append(x)
    return r