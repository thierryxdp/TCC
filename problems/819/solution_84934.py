def filtramultiplos (l,n):
    multiplos = []
    proximo = 0
    while proximo<len(l):
        if l[proximo]%n==0:
            multiplos = multiplos + [l[proximo]]
            proximo= proximo + 1
        return multiplos