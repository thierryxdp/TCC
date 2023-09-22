def filtraMultiplos(x):
    multiplos = ()
    y = 0
    while proximo<len(x):
        if x[proximo]%2==0:
            multiplos = multiplos + (x[y],)
        y = y + 1
    return multiplos