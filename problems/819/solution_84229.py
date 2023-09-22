def filtraMultiplos(l, n):
    multiplos = []
    for val in l:
        if val%n==0:
            multiplos.append(val)
    return multiplos