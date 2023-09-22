def filtraMultiplos(lista,n):
    multiplos = ()
    proximo = 0
    while proximo < len(lista):
        if t[proximo] / n == 0:
            multiplos = multiplos + (t[proximo])
        proximo = proximo + 1
    return multiplos