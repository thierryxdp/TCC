def filtraMultiplos(l):
    multiplos = []
    proximo = 0 
    numero = n
    while proximo <len(l):
        if l[proximo]/n == l[proximo]//n:
            multiplos = multiplos + [l[proximo],]
        proximo = proximo + 1
    return multiplos