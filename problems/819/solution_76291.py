def filtraMultiplos(l,n):
    """ essa função calculará todos os multiplos de n na lista l
    entrada -> lista,int
    saida -> lista"""
    multiplos = []
    proximo = 0
    while proximo < len(l):
        if l[proximo]%n == 0:
            multiplos = multiplos + [l[proximo],]
        proximo = proximo + 1
    return multiplos