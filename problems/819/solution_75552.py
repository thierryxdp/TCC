def filtraMultiplos(listi,n):
    multiplos = []
    proximo = 0
    while proximo < len(listi):
        if listi[proximo]%n == 0:
            multiplos = multiplos + [listi[proximo]]
        proximo = proximo + 1
    return multiplos