def filtramultiplos (lista,n):
    multiplos = []
    proximo = 0
    while proximo<len(l):
        if lista[proximo]%n==0:
            multiplos = multiplos + [lista[proximo]]
        proximo = proximo + 1
    return multiplos