def filtraMultiplos(x,n):
    i = 0
    while i < len(x):
        if not x[i] % n == 0:
            del x[i]
        i += 1
    return x