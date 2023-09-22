def filtraMultiplos(x,n):
    return x%n == 0
def fm(ls,n):
    r = []
    for x in ls:
        if filtraMultiplos(x,n):
            r.append(x)
    return r