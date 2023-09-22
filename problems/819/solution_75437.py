def filtraMultiplos(m,n):
    multiplos = []
    proximo = 0
    while proximo < len(m):
        if m[proximo]%n == 0:
            multiplos = multiplos + [m[proximo]]
        proximo = proximo + 1
    return multiplos