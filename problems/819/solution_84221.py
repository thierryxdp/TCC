def filtraMultiplos(x, n):
    multiplos = ()
    y = 0
    while proximo<len(x):
        if x[proximo]%n==0:
            multiplos = multiplos + (x[y],)
        y = y + 1
    return multiplos