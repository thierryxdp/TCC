def filtra(ls,detector):
    r = []
    for e in ls:
        if detector(e):
            r.append(e)
    return r 

def filtra_multiplos(ls,n):
    return filtra(ls, lambda x: x%n == 0