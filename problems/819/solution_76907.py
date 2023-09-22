def filtraMultiplos(l,n):
    multiplos = []
    proximo = 0
    while proximo <len(l):
        if l[proximo]/n == l[proximo]//n:
            multiplos = multiplos + [l[proximo],]
        proximo = proximo + 1
    return multiplos